"""Prime number utility module for Project Euler"""
from math import sqrt

class PrimeCache(object):
    def __init__(self):
        self._primes = [2,3]
        self._primes_set = set(self._primes)

    def __getitem__(self, index):
        while len(self._primes) <= index:
            self._extend_sequence()
        return self._primes[index]
    
    def __contains__(self, value):
        if value <= 1:
            return False
        sqrt_v = int(sqrt(value))
        if self._primes[-1] < sqrt_v:
            self._find_primes_to(sqrt_v + 1)
        for p in self._primes:
            if p > sqrt_v:
                break
            if value % p == 0:
                return False
        return True

    def __iter__(self):
        return PrimesIterator(primes=self)
    
    def to(self, target):
        self._find_primes_to(target)
    
    def _extend_sequence(self):
        self._find_next_prime()
    
    def _find_next_prime(self):
       current = self._primes[-1]
       is_prime = False
       while not is_prime:
           is_prime = True
           current += 2
           
           for p in self._primes:
               if current % p == 0:
                   is_prime = False
                   break
               elif p ** 2 > current:
                   break
       
       self._primes.append(current)
       self._primes_set.add(current)
    
    def _find_primes_to(self, limit=None):
        p = self._primes[-1]
        if limit is None:
            limit = p**2
        while limit > p**2:
            self._find_primes_to(p**2)
            p = self._primes[-1]
        
        step = min(limit-p, int(1.5E7))
        start, end = p, p+step
        all_candidates = set()
        while start < limit:
            candidates = set(self._wheel(start, end))
            for p in self._primes[1:]:
                start_p = start if start % p == 0 else start + p - (start % p)
                candidates -= set(range(start_p, end, p))
            
            all_candidates |= candidates
            start, end = end, min(end+step, limit)
        self._primes.extend(sorted(all_candidates))
        self._primes_set |= all_candidates
    
    def _wheel(self, start, stop):
        if start % 2 == 0:
            start += 1
        for x in range(start, stop, 2):
            yield x

_global_prime_cache = PrimeCache()

class PrimesIterator(object):
    def __init__(self, primes=_global_prime_cache):
        self._primes = primes
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        index = self._index
        self._index += 1
        return self._primes[index]
    
    # for Python 2.X
    next = __next__

def primes_below(n):
    _global_prime_cache.to(n)
    it = iter(_global_prime_cache)
    p = next(it)
    while p < n:
        yield p
        p = next(it)

def prime_range(start, stop):
    it = iter(_global_prime_cache)
    p = next(it)
    while p < start:
        p = next(it)
    while p < stop:
        yield p
        p = next(it)

primes = _global_prime_cache

# This function works very quickly.
# This function can be noticeably faster than the PrimesCache class,
# but you need to know a number that all the primes you need will
# be less than to use it.
def get_primes_fast(n):
    p = 3
    primes = {2} | set(range(3, n, 2))
    last = n
    while last > len(primes):
        last = len(primes)
        primes -= set(range(p*2, n, p))
        p += 2
        while not p in primes:
            p += 2
    
    return primes
