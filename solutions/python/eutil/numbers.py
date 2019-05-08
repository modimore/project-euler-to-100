from math import sqrt

def digit_list(n, base=10):
    if  n < 0:
        return digit_list(-n)
    if n == 0:
        return [0]
    
    digit_list = []
    while n > 0:
        digit_list.append(n%base)
        n //= base
    return digit_list[::-1]

class NaturalSequenceCache:
    def __init__(self, definition):
        self._definition = definition
        self._elements = []
    
    def __getitem__(self, index):
        while len(self._elements) <= index:
            self._elements.append(self._definition(len(self._elements)+1))
        return self._elements[index]
    
    def __iter__(self):
        return NaturalSequenceIterator(self)

class NaturalSequenceIterator:
    def __init__(self, seq):
        self._sequence = seq
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self._sequence[self._index]
        self._index += 1
        return value

def triangle_number(n):
    return n * (n+1) // 2

def is_triangle_number(m):
    n = (-1 + sqrt(8*m+1)) // 2
    return m == triangle_number(n)

class TriangleNumberCache(NaturalSequenceCache):
    def __init__(self):
        super().__init__(triangle_number)
    
    def __contains__(self, n):
        return is_triangle_number(n)

def square_number(n):
    return n*n

def is_square_number(m):
    n = sqrt(m)
    return n == int(n)

class SquareNumberCache(NaturalSequenceCache):
    def __init__(self):
        super().__init__(square_number)
    
    def __contains__(self, n):
        return is_square_number(n)

def pentagon_number(n):
    return n * (3*n-1) // 2

def is_pentagon_number(m):
    n = (1 + sqrt(24*m+1)) // 6
    return m == pentagon_number(n)

class PentagonNumberCache(NaturalSequenceCache):
    def __init__(self):
        super().__init__(pentagon_number)
    
    def __contains__(self, n):
        return is_pentagon_number(n)

def hexagon_number(n):
    return n * (2 * n - 1)

def is_hexagon_number(m):
    n = (1 + sqrt(8*m+1)) // 4
    return m == hexagon_number(n)

class HexagonNumberCache(NaturalSequenceCache):
    def __init__(self):
       super().__init__(hexagon_number)
    
    def __contains__(self, n):
        return is_hexagon_number(n)

def heptagon_number(n):
    return n * (5*n-3) // 2

def is_heptagon_number(m):
    n = (sqrt(40*m + 9) + 3) / 10
    return m == heptagon_number(n)

def octagon_number(n):
    return n * (3*n-2)

def is_octagon_number(m):
    n = (1 + sqrt(3*m+1)) / 3
    return octagon_number(n) == m

triangle_numbers = TriangleNumberCache()
pentagon_numbers = PentagonNumberCache()
hexagon_numbers = HexagonNumberCache()
