from unittest import TestSuite

try:
    import test_fscache
except ImportError:
    from . import test_fscache

def test_suite():
  suite = TestSuite()
  suite.addTest(test_fscache.test_suite())
  return suite
