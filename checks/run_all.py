#!/usr/bin/env python3
"""Reproduce the research certificates without mutating the checkout.

Python 3.10+, standard library only. Integer and structural report fields
are exact; floating entropy evaluations allow a documented 1e-10 tolerance.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TOL = 1e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compare(expected, actual, path: str = "report") -> None:
    """Compare JSON recursively, with tolerance only for floating fields."""
    require(type(expected) is type(actual), f"Type mismatch at {path}")
    if isinstance(expected, dict):
        require(expected.keys() == actual.keys(), f"Key mismatch at {path}")
        for key in expected:
            compare(expected[key], actual[key], f"{path}.{key}")
    elif isinstance(expected, list):
        require(len(expected) == len(actual), f"Length mismatch at {path}")
        for index, (left, right) in enumerate(zip(expected, actual)):
            compare(left, right, f"{path}[{index}]")
    elif isinstance(expected, float):
        require(math.isfinite(expected) and math.isfinite(actual),
                f"Non-finite float at {path}")
        require(math.isclose(expected, actual, rel_tol=TOL, abs_tol=TOL),
                f"Float mismatch at {path}: {expected} != {actual}")
    else:
        require(expected == actual, f"Value mismatch at {path}")


def check_imports() -> int:
    manifest = json.loads((ROOT / "docs/SOURCE_MANIFEST.json").read_text())
    for item in manifest["unchanged_imports"]:
        path = (ROOT / item["path"]).resolve()
        require(path.is_relative_to(ROOT), "Source path escapes repository")
        data = path.read_bytes()
        require(len(data) == item["bytes"], f"Size changed: {item['path']}")
        require(hashlib.sha256(data).hexdigest() == item["sha256"],
                f"Imported source changed: {item['path']}")
    return len(manifest["unchanged_imports"])


def check_links() -> int:
    count = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        require(text.count("```") % 2 == 0, f"Unclosed code fence: {path}")
        require("sandbox:/" not in text, f"Session-only link in public document: {path}")
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", text):
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            require(resolved.is_relative_to(ROOT), f"Link escapes repository: {target}")
            require(resolved.exists(), f"Missing link in {path}: {target}")
            count += 1
    return count


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def expect_exception(kind, function) -> None:
    try:
        function()
    except kind:
        return
    raise AssertionError(f"Expected {kind.__name__}")


def check_interfaces() -> int:
    exact = load_module("a1_exact_contract", ROOT / "checks/verify_exact.py")
    bounded = load_module("a1_bounded_contract", ROOT / "checks/verify_bounded_error.py")
    expect_exception(ValueError, lambda: exact.parameters(2))
    expect_exception(ValueError, lambda: exact.encode(8, 3))
    oracle = exact.RawBitOracle(1, 3)
    expect_exception(IndexError, lambda: oracle.read(0))
    require(oracle.read(1) == 1 and oracle.reads == 1, "Exact oracle convention changed")
    expect_exception(RuntimeError, lambda: oracle.read(2))
    raw = bounded.RawBitOracle(1, 3)
    expect_exception(IndexError, lambda: raw.read(3))
    require(raw.read(0) == 1 and raw.calls == 1, "Bounded oracle convention changed")
    expect_exception(AssertionError, lambda: raw.read(1))
    expect_exception(ValueError, lambda: bounded.majority_error(2))
    expect_exception(ValueError, lambda: bounded.decode_majorities(
        0, 1, 1, 3, bounded.RawBitOracle(0, 3)))
    return 10


def execute(script: Path, cwd: Path, arguments: list[str]) -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0")
    result = subprocess.run([sys.executable, str(script), *arguments], cwd=cwd,
                            env=env, text=True, capture_output=True, timeout=240)
    if result.returncode:
        raise RuntimeError(f"{script.name} failed:\n{result.stdout}\n{result.stderr}")


def check_report(expected: Path, actual: Path) -> bool:
    compare(json.loads(expected.read_text()), json.loads(actual.read_text()))
    return expected.read_bytes() == actual.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--include-conjunction", action="store_true")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        raise RuntimeError("Python 3.10 or newer is required")
    if not __debug__:
        raise RuntimeError("Run without -O: assertion checks must remain enabled")
    sys.dont_write_bytecode = True
    report = {"status": "PASS", "imported_files": check_imports(),
              "local_document_links": check_links(),
              "interface_checks": check_interfaces(), "suites": {}}
    with tempfile.TemporaryDirectory(prefix="a1-reproduce-") as directory:
        tmp = Path(directory)
        suites = (("exact_parity", "verify_exact.py"),
                  ("bounded_error", "verify_bounded_error.py"))
        for name, filename in suites:
            print(f"Checking {name} ...", flush=True)
            output = tmp / f"{name}.json"
            execute(ROOT / "checks" / filename, tmp, ["--output", str(output)])
            identical = check_report(ROOT / "results" / f"{name}.json", output)
            report["suites"][name] = {"matches_recorded_report": True,
                                     "byte_identical_this_environment": identical}
        if args.include_conjunction:
            print("Checking separate conjunction exploration ...", flush=True)
            source = ROOT / "explorations/conjunction"
            copied = tmp / "verify_conjunction.py"
            shutil.copyfile(source / "verify.py", copied)
            execute(copied, tmp, [])
            for filename in ("verification_results.json", "four_feature_decoder.json"):
                identical = check_report(source / filename, tmp / filename)
                report["suites"][f"conjunction/{filename}"] = {
                    "matches_recorded_report": True,
                    "byte_identical_this_environment": identical}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
