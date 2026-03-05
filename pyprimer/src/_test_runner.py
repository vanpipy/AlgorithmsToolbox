import argparse
import os
import sys
import unittest
from pathlib import Path


def _discover_for_target(target: str) -> unittest.TestSuite:
    p = Path(target)
    if p.exists():
        if p.is_dir():
            return unittest.defaultTestLoader.discover(str(p), pattern="test_*.py")
        # treat as single file
        return unittest.defaultTestLoader.discover(str(p.parent), pattern=p.name)
    # fallback: try dotted name loading
    return unittest.defaultTestLoader.loadTestsFromName(target)


def _filter_suite_by_keyword(suite: unittest.TestSuite, keyword: str) -> unittest.TestSuite:
    if not keyword:
        return suite
    filtered = []
    for test in unittest.TestSuite(suite):
        for t in _iter_tests(test):
            if keyword in t.id():
                filtered.append(t)
    return unittest.TestSuite(filtered)


def _iter_tests(suite_or_case):
    if isinstance(suite_or_case, unittest.TestSuite):
        for t in suite_or_case:
            yield from _iter_tests(t)
    else:
        yield suite_or_case


def main():
    parser = argparse.ArgumentParser(prog="tests", description="Run unittest suites with uv")
    parser.add_argument("-s", "--start-directory", default="test", help="start directory for discovery")
    parser.add_argument("-p", "--pattern", default="test_*.py", help="pattern for test discovery")
    parser.add_argument("-k", "--keyword", default="", help="only run tests which match substring")
    parser.add_argument(
        "-t",
        "--target",
        action="append",
        default=[],
        help="test file or directory path (can be repeated). If omitted, use discovery.",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="quiet output")
    args, _ = parser.parse_known_args()

    # ensure cwd on sys.path for module discovery
    if "" not in sys.path and os.getcwd() not in sys.path:
        sys.path.insert(0, "")

    if args.target:
        suites = [ _discover_for_target(t) for t in args.target ]
        suite = unittest.TestSuite(suites)
    else:
        suite = unittest.defaultTestLoader.discover(args.start_directory, pattern=args.pattern)

    if args.keyword:
        suite = _filter_suite_by_keyword(suite, args.keyword)

    verbosity = 1 if args.quiet else 2
    result = unittest.TextTestRunner(verbosity=verbosity).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
