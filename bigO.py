
'''Symbolic manipulation of Big-O complexities.'''

import sympy

n = sympy.Symbol('n', positive=True)


class BigO(object):
  def __init__(self, expr):
    self.expr = expr

  def __eq__(self, other):
    return self.expr == other.expr or 0 < self._limit(other) < sympy.oo

  def __gt__(self, other):
    return self._limit(other) == sympy.oo

  def __lt__(self, other):
    return self._limit(other) == 0

  def _limit(self, other):
    return sympy.limit(self.expr/other.expr, n, sympy.oo)

  def inside(self, other):
    return BigO(self.expr * other.expr)

  def followed_by(self, *others):
    return max(self, *others)

O = BigO  # for concision, if desired
