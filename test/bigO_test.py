import unittest
import doctest
from sympy import sqrt, log, Rational, factorial
import bigO
from bigO import O, n


def load_tests(loader, tests, ignore):
  tests.addTests(doctest.DocTestSuite(bigO))
  return tests


def argsort(seq):
  return sorted(range(len(seq)), key=seq.__getitem__)


class TestBigO(unittest.TestCase):

  def setUp(self):
    self.f_time = O(n)
    self.g_time = O(n**2)
    self.h_time = O(sqrt(n))

  def test_ordering_simple(self):
    fastest = min(self.f_time, self.g_time, self.h_time)
    slowest = max(self.f_time, self.g_time, self.h_time)
    self.assertEqual(fastest, self.h_time)
    self.assertEqual(slowest, self.g_time)

  def test_ordering_complex(self):
    funcs = [
        O(2**sqrt(log(n))),
        O(2**(2**n)),
        O(n*log(n)**3),
        O(n**Rational(4,3)),
        O(n**log(n)),
        O(2**n),
        O((n**(1/log(n)))**3),
        O(factorial(n)),
        O(n**(1+1/log(log(n)))),
        O(log(n)**2),
        O(log(n)**log(n)),
        O(3.14**n)
    ]
    order = argsort(funcs)
    expected_order = [6, 9, 0, 2, 8, 3, 10, 4, 5, 11, 7, 1]
    self.assertEqual(order, expected_order)

  def test_composition(self):
    total_time = self.f_time.inside(self.g_time).followed_by(self.h_time)
    self.assertEqual(total_time, O(n**3))

if __name__ == '__main__':
  unittest.main()
