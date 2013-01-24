#!/usr/bin/env python

import unittest
import sympy
from bigO import O, n


class TestBigO(unittest.TestCase):

  def setUp(self):
    self.f_time = O(n)
    self.g_time = O(n**2)
    self.h_time = O(sympy.sqrt(n))

  def test_ordering(self):
    fastest = min(self.f_time, self.g_time, self.h_time)
    slowest = max(self.f_time, self.g_time, self.h_time)
    self.assertEqual(fastest, self.h_time)
    self.assertEqual(slowest, self.g_time)

  def test_composition(self):
    total_time = self.f_time.inside(self.g_time).followed_by(self.h_time)
    self.assertEqual(total_time, O(n**3))

if __name__ == '__main__':
  unittest.main()
