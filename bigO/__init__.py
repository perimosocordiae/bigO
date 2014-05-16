'''Symbolic manipulation of Big-O complexities.'''

import sympy


class BigO(object):
  def __init__(self, expr):
    self.expr = sympy.sympify(expr)
    assert len(self.expr.free_symbols) <= 1, (
        'Too many variables: %s' % self.expr)

  def __eq__(self, other):
    return self.expr == other.expr or 0 < self._limit(other) < sympy.oo

  def __gt__(self, other):
    return self._limit(other) == sympy.oo

  def __lt__(self, other):
    return self._limit(other) == 0

  def _limit(self, other):
    ratio = self.expr/other.expr
    assert len(ratio.free_symbols) == 1, (
        'Ambiguous var in limit ratio: %s' % ratio)
    return sympy.limit(ratio, list(ratio.free_symbols)[0], sympy.oo)

  def inside(self, other):
    return BigO(self.expr * other.expr)

  def followed_by(self, *others):
    return max(self, *others)

  def __str__(self):
    return "O(%s)" % self.expr

# definitions for concision, if desired
O = BigO
n = sympy.Symbol('n', positive=True)
