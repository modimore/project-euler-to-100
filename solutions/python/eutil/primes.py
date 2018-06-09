"""Prime number utility module for Project Euler"""

# Currently finding primes one at a time using
# trial division. This has been working best out
# of the two approaches I have on P07 and P10.

class PrimeCache(object):
    def __init__(self):
        self._primes = [2,3]
        self._primes_set = set(self._primes)

    def __getitem__(self, index):
        while len(self._primes) <= index:
            self._extend_sequence()
        return self._primes[index]
    
    def __contains__(self, value):
        while self._primes[-1] < value:
            self._extend_sequence()
        return value in self._primes_set

    def __iter__(self):
        return PrimesIterator(primes=self)
    
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
    
    def _find_primes(self):
        p = self._primes[-1]
        limit = p**2
        candidates = set(range(p, limit, 2))
        for p in self._primes[1:]:
            candidates -= set(range(p, limit, p))
        
        self._primes.extend(sorted(candidates))
        self._primes_set |= candidates

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
    it = iter(_global_prime_cache)
    p = next(it)
    while p < n:
        yield p
        p = next(it)

primes = _global_prime_cache

# This function works very quickly.
# If you know what your limit is it's the best solution I've
# seen, but I don't know how to cache it quite yet.
def get_primes_fast(n):
    p = 3
    primes = {2} | set(range(3, n, 2))
    last = n
    while last > len(primes):
        last = len(primes)
        primes -= set(range(p*2, 2*n, p))
        p += 2
        while not p in primes:
            p += 2
    
    return primes
