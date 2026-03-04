import sys
import unittest


def main():
    suite = unittest.defaultTestLoader.discover("test", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
