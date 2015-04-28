# bigO

[![PyPI version](https://badge.fury.io/py/bigO.svg)](http://badge.fury.io/py/bigO)
[![Build Status](https://travis-ci.org/perimosocordiae/bigO.svg?branch=master)](https://travis-ci.org/perimosocordiae/bigO)

*Symbolic representation of big-O notation.*

I was [looking for something like this](http://stackoverflow.com/questions/14510216/is-there-a-library-for-programmatic-manipulation-of-big-o-complexities)
but couldn't find it.
So I wrote it, and it turned out to be much simpler than I expected.

Note that this is not the same as [sympy.series.order](http://docs.sympy.org/dev/modules/series.html#order-terms):
that handles terms in series expansions of functions, whereas this library deals with time and/or space complexity.

## Usage

```python
import sympy
from bigO import O, n

f_time = O(n)
g_time = O(n**2)
h_time = O(sympy.sqrt(n))

fastest_asymptotically = min(f_time, g_time, h_time)
# = h_time

total_time = f_time.inside(g_time).followed_by(h_time)
# = O(n**3)
```
