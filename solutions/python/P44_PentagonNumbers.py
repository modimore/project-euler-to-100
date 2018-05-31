from __future__ import print_function
from math import sqrt

def pentagon_number(n):
    return n * (3*n-1) // 2

def is_pentagon_number(m):
    n = (1 + sqrt(24*m+1)) // 6
    return m == pentagon_number(n)

class PentagonNumberCache:
    def __init__(self):
        self._pentagon_numbers = [pentagon_number(1)]
    
    def __contains__(self, n):
        return is_pentagon_number(n)
        #while self._pentagon_numbers[-1] < n:
        #    self._find_next()
        #return n in self._pentagon_numbers
    
    def __getitem__(self, i):
        while len(self._pentagon_numbers) <= i:
            self._find_next()
        return self._pentagon_numbers[i]
    
    def _find_next(self):
        self._pentagon_numbers.append(pentagon_number(len(self._pentagon_numbers)+1))

pentagon_numbers = PentagonNumberCache()

if __name__ == "__main__":
    try:
        from math import inf
    except:
        from sys import maxint
        inf = maxint
    pair = (None, None, inf)
    found = False
    k = 1
    while not found:
        P_k = pentagon_numbers[k]
        j = k - 1
        while 0 <= j:
            P_j = pentagon_numbers[j]
            S, D = P_k + P_j, P_k - P_j
            if D > pair[2]:
                break
            if D in pentagon_numbers and S in pentagon_numbers:
                pair = min(pair, (k, j, D), key=lambda p: p[2])
                found = True
                break
            j -= 1
        if found: break
        if 3 * k + 1 > pair[2]:
            break
        k += 1
    print("Minimum difference:", pair[2])
