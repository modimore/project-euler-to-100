def fact_canonical(n):
    if n == 0:
        return 1
    return n * fact_canonical(n-1)

class FactorialCache:
    def __init__(self):
        self._factorials = [1]
    
    def __getitem__(self, n):
        for i in range(len(self._factorials), n+1):
            self._factorials.append(self._factorials[i-1] * i)
        return self._factorials[n]
    
    def __iter__(self):
        return FactorialsIterator(factorials=self)
    
_global_factorial_cache = FactorialCache()

class FactorialsIterator:
    def __init__(self, factorials=_global_factorial_cache):
        self._factorials = factorials
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        index = self._index
        self._index += 1
        return self._factorials[index]
    
    # for Python 2
    next = __next__

def factorial(n):
    return _global_factorial_cache[n]

fact = factorial
