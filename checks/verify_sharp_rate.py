#!/usr/bin/env python3
"""Small exact checks and explicitly numerical checks for the sharp-rate proof.

No external dependencies. This does not build asymptotic covering codes or
certify a proof. Original records are never handed to a decoder except through
its counted one-read oracle. Outputs are written only to an explicit --output.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, permutations
import json
import math
from pathlib import Path
import sys

LN2 = math.log(2.0)
TOL = 2e-10


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def information(bias: float) -> float:
    if not 0.0 <= bias <= 1.0:
        raise ValueError("bias must lie in [0,1]")
    if bias == 1.0:
        return 1.0
    return ((1+bias)*math.log1p(bias)+(1-bias)*math.log1p(-bias))/(2*LN2)


def logcosh(value: float) -> float:
    value = abs(value)
    return value + math.log1p(math.exp(-2*value)) - LN2


def insert(row: int, pivots: dict[int, int]) -> bool:
    while row:
        p = row.bit_length()-1
        if p not in pivots:
            pivots[p] = row
            return True
        row ^= pivots[p]
    return False


def phi(n: int, rank: int) -> int:
    return n*rank-rank*(rank-1)//2


def check_cells(max_n: int = 5) -> dict:
    """All nonempty fixed-parity cells; correlations/counts are integers."""
    summaries = []
    for n in range(3, max_n+1):
        count = structural = dual_checks = 0
        residuals = []
        for i,j in combinations(range(n),2):
            q = (1<<i) ^ (1<<j)
            residuals.append(sorted({q} | {q^(1<<k) for k in range(n)}))
        lambdas = (0.02, 0.2, 1.0, 3.0)
        constants = [sum(logcosh(lam*k) for k in range(1,n+1))
                     for lam in lambdas]
        info = {(s,v): information(v/s) for s in range(1,(1<<(n-1))+1)
                for v in range(s+1)}
        for parity in (0,1):
            universe = [x for x in range(1<<n) if x.bit_count()%2 == parity]
            signs = [[1-2*((x&a).bit_count()%2) for a in range(1<<n)]
                     for x in universe]
            sums = [0]*(1<<n)
            previous = size = 0
            for code in range(1,1<<len(universe)):
                gray = code^(code>>1)
                changed = gray^previous
                index = changed.bit_length()-1
                direction = 1 if gray&changed else -1
                size += direction
                sums = [a+direction*b for a,b in zip(sums,signs[index])]
                previous = gray
                require(size>0,"empty cell in nonempty Gray enumeration")
                selected = []
                for choices in residuals:
                    row = min(choices,key=lambda a:(-abs(sums[a]),a))
                    selected.append((abs(sums[row]),row))
                selected.sort(key=lambda pair:(-pair[0],pair[1]))
                pivots = {}
                basis_biases = []
                for bias,row in selected:
                    if insert(row,pivots):
                        basis_biases.append(bias)
                total = sum(b for b,_ in selected)
                weighted = sum((n-index)*b for index,b in enumerate(basis_biases))
                require(total<=weighted,"rank-profile majorization failed")
                structural += 1
                # Independently check threshold ranks, not the weighted result.
                for threshold in set(b for b,_ in selected):
                    rows = [row for b,row in selected if b>=threshold]
                    threshold_basis = {}
                    for row in rows:
                        insert(row,threshold_basis)
                    require(len(rows)<=phi(n,len(threshold_basis)),"coverage failed")
                    structural += 1
                deficit = n-math.log2(size)
                require(sum(info[size,b] for b in basis_biases)<=deficit+TOL,
                        "independent-bias entropy budget failed")
                for lam,constant in zip(lambdas,constants):
                    require(lam*total/size <= LN2*deficit+constant+TOL,
                            "finite dual converse failed on a cell")
                    dual_checks += 1
                count += 1
        require(count==2*((1<<(1<<(n-1)))-1),"cell enumeration count mismatch")
        summaries.append({"n":n,"cells":count,"exact_structural_checks":structural,
                          "numerical_dual_checks":dual_checks})
    return {"scope":"all nonempty fixed-total-parity cells, n=3,4,5",
            "counts":summaries,"entropy_and_dual_tolerance":TOL}


def simpson(function, steps: int = 2048) -> float:
    if steps<=0 or steps%2:
        raise ValueError("positive even integration step count required")
    odds = math.fsum(function(j/steps) for j in range(1,steps,2))
    evens = math.fsum(function(j/steps) for j in range(2,steps,2))
    return (function(0.0)+function(1.0)+4*odds+2*evens)/(3*steps)


def bias_at(parameter: float, steps: int = 2048) -> float:
    return 2*simpson(lambda u:u*math.tanh(parameter*u),steps)


def rate_at(parameter: float, steps: int = 2048) -> float:
    return simpson(lambda u:information(math.tanh(parameter*u)),steps)


def solve(error: float, steps: int = 2048) -> tuple[float,float]:
    if not 0.0<error<0.5:
        raise ValueError("fixed error must lie strictly between 0 and 1/2")
    target = 1-2*error
    lo,hi = 0.0,1.0
    while bias_at(hi,steps)<target:
        hi *= 2
    for _ in range(45):
        mid = (lo+hi)/2
        if bias_at(mid,steps)<target:
            lo = mid
        else:
            hi = mid
    parameter = (lo+hi)/2
    return parameter,rate_at(parameter,steps)


def check_curve() -> dict:
    # Check the Legendre identity by its independent entropy expression.
    for w in (0.0,0.01,0.2,1.0,5.0):
        for numerator in range(101):
            b = numerator/100
            require(w*b-LN2*information(b)<=logcosh(w)+TOL,"Fenchel bound")
        b = math.tanh(w)
        require(abs(w*b-LN2*information(b)-logcosh(w))<TOL,"Fenchel equality")
    table = []
    for error in (0.01,0.05,0.1,0.2,0.25,11/32,0.4,0.45,0.49):
        t,r = solve(error)
        t2,r2 = solve(error,4096)
        target = 1-2*error
        require(abs(r-r2)<1e-9 and abs(t-t2)<1e-8,"quadrature disagreement")
        dual = (t*target/2-simpson(lambda u:logcosh(t*u)))/LN2
        compact = (t*target-logcosh(t))/LN2
        require(abs(r-dual)<TOL and abs(r-compact)<TOL,"rate identity")
        old_lower = 1-math.sqrt(1-information(target))
        old_upper = min(information(target),1-math.sqrt(2*error))
        affine = 1-math.sqrt(2*error)
        require(old_lower<r<old_upper and r<affine,"rate comparison")
        # This discretized dual is a lower bound, NOT a finite optimum.
        finite = []
        for n in (64,256,1024):
            bound = (t*(n-1)/(2*n)*target-
                     math.fsum(logcosh(t*k/n) for k in range(1,n+1))/n)/LN2
            require(bound<=r+TOL,"finite bound exceeds its limiting objective")
            finite.append(round(bound,9))
        table.append({"error":error,"parameter":round(t,9),"sharp_rate":round(r,9),
                      "previous_lower":round(old_lower,9),
                      "previous_upper":round(old_upper,9),"affine_rate":round(affine,9),
                      "finite_dual_per_bit_n64_n256_n1024":finite})
    # Equal-quality K=1 recovers the old entropy-rate construction; increasing
    # K supplies finer levels. This is a numerical profile check, not a code.
    profiles = []
    target = 0.8
    for levels in (1,4,16,64,256):
        points = [(j+0.5)/levels for j in range(levels)]
        lo,hi = 0.0,8.0
        for _ in range(50):
            t = (lo+hi)/2
            achieved = 2*math.fsum(u*math.tanh(t*u) for u in points)/levels
            if achieved<target:lo=t
            else:hi=t
        r = math.fsum(information(math.tanh((lo+hi)*u/2)) for u in points)/levels
        profiles.append({"levels":levels,"rate":round(r,9)})
    require(all(a["rate"]>b["rate"] for a,b in zip(profiles,profiles[1:])),
            "graded profile rates should decrease in this tested sequence")
    for gamma in (0.001,0.005,0.01):
        _,r = solve(0.5-gamma)
        require(abs(r/(gamma*gamma)-3/(2*LN2))<0.001,"weak-advantage coefficient")
    return {"table":table,"graded_profiles_at_error_0_1":profiles,
            "numerical_only":True,"integration_steps_compared":[2048,4096]}


class Oracle:
    def __init__(self,x: int,n: int):
        if not 0<=x<1<<n:
            raise ValueError("invalid input")
        self.__x,self.n,self.reads=x,n,0
    def read(self,k: int) -> int:
        if not 0<=k<self.n:
            raise IndexError(k)
        if self.reads:
            raise RuntimeError("second raw read forbidden")
        self.reads+=1
        return (self.__x>>k)&1


def tiny_encode(x: int, permutation: tuple[int,...],mask: int) -> tuple[int,int,int]:
    # y-position a holds original coordinate permutation[a], then is masked.
    y = sum((((x>>old)&1)^((mask>>a)&1))<<a for a,old in enumerate(permutation))
    return x.bit_count()%2, int((y&7).bit_count()>=2),(y>>3)&1


def tiny_decode(memory: tuple[int,int,int],permutation: tuple[int,...],mask: int,
                i: int,j: int,oracle: Oracle) -> int:
    if i==j or not (0<=i<4 and 0<=j<4):
        raise ValueError("invalid pair")
    positions = {old:a for a,old in enumerate(permutation)}
    # Reconstruct the more accurately encoded endpoint, reread the other.
    estimated,read = (i,j) if positions[i]==3 or positions[j]!=3 else (j,i)
    a = positions[estimated]
    prediction = memory[2] if a==3 else memory[1]
    return memory[0]^oracle.read(read)^prediction^((mask>>a)&1)


def check_seeded_decoder() -> dict:
    n = 4
    perms = tuple(permutations(range(n)))
    cases = 0
    for x in range(1<<n):
        for i,j in combinations(range(n),2):
            mistakes = 0
            for perm in perms:
                for mask in range(1<<n):
                    oracle = Oracle(x,n)
                    answer = tiny_decode(tiny_encode(x,perm,mask),perm,mask,i,j,oracle)
                    correct = x.bit_count()%2^((x>>i)&1)^((x>>j)&1)
                    mistakes += answer!=correct
                    require(oracle.reads==1,"decoder did not use exactly one raw read")
                    cases += 1
            require(Fraction(mistakes,len(perms)*(1<<n))==Fraction(1,8),
                    "fixed-input, fixed-query symmetrization failed")
    oracle = Oracle(0,4)
    oracle.read(0)
    try:
        oracle.read(1)
    except RuntimeError:
        pass
    else:
        raise AssertionError("raw-read guard failed")
    return {"input_bits":4,"summary_bits":3,"fixed_input_query_pairs":96,
            "all_mask_permutation_decoder_cases":cases,"error_every_fixed_pair":"1/8",
            "max_raw_reads":1}


def covering_certificate() -> dict:
    # Radii are frozen INTEGERS. All following statements are exact, independent
    # of the numerical optimization that suggested these radii.
    m = 128
    radii = [56,42,29,20,13,8,5,3]
    n = m*len(radii)
    memory = 1
    error = Fraction(0)
    block_bits = []
    for index,radius in enumerate(radii,1):
        volume = sum(math.comb(m,j) for j in range(radius+1))
        centers = min(1<<m,(((m+1)<<m)+volume-1)//volume)
        bits = (centers-1).bit_length()
        block_bits.append(bits)
        memory += bits
        pairs = math.comb(index*m,2)-math.comb((index-1)*m,2)
        error += Fraction(pairs,math.comb(n,2))*Fraction(radius,m)
    target = Fraction(1,10)
    affine_min = next(b for b in range(n+1) if
                      phi(n,b)>=math.comb(n,2)*(1-2*target))
    require(memory==529 and error==Fraction(6245,65472) and error<target,
            "covering existence certificate changed")
    require(affine_min==565 and memory<affine_min,"finite affine separation")
    return {"n":n,"block_size":m,"radii":radii,"block_memory_bits":block_bits,
            "summary_bits_including_parity":memory,"error_upper_bound":str(error),
            "target_error":"1/10","affine_bits_necessary_at_target":affine_min,
            "evidence":"integer arithmetic plus probabilistic covering-existence proof",
            "large_cover_constructed":False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    if sys.version_info<(3,10) or not __debug__:
        raise RuntimeError("Python 3.10+ without -O is required")
    report = {"status":"PASS","rank_profile":check_cells(),"curve":check_curve(),
              "seeded_decoder":check_seeded_decoder(),"covering":covering_certificate()}
    text = json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text,encoding="utf-8")
    else:
        print(text,end="")


if __name__=="__main__":
    main()
