"""Helper module for these utilities which are not strictly math-focused."""
import functools

def memoize_series(f):
    """Memoization helper designed for a function that generates a series.
    
    The function should take a non-negative integer as an argument and return
    the item of the series at that conceptual index.
    """
    series = []
    
    @functools.wraps(f)
    def memoized(i):
        for n in range(len(series), i+1):
            series.append(f(n))
        return series[i]
    
    return memoized
