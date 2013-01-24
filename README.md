# bigO

*Symbolic representation of big-O notation.*

I was [looking for something like this](http://stackoverflow.com/questions/14510216/is-there-a-library-for-programmatic-manipulation-of-big-o-complexities)
but couldn't find it.
So I wrote it, and it turned out to be much simpler than I expected.

## Usage

    import sympy
    from bigO import O, n

    f_time = O(n)
    g_time = O(n**2)
    h_time = O(sympy.sqrt(n))

    fastest_asymptotically = min(f_time, g_time, h_time)
    # = h_time
    
    total_time = f_time.inside(g_time).followed_by(h_time)
    # = O(n**3)
