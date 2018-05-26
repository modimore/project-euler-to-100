def triangle_number(n):
    return n * (n+1) // 2

class TriangleNumberCache:
    def __init__(self):
        self._triangle_numbers = [triangle_number(1)]
    
    def __contains__(self, n):
        while self._triangle_numbers[-1] < n:
            self._find_next()
        return n in self._triangle_numbers
    
    def __getitem__(self, i):
        while len(self._triangle_numbers) <= i:
            self._find_next()
        return self._triangle_numbers[i]
    
    def _find_next(self):
        self._triangle_numbers.append(triangle_number(len(self._triangle_numbers)+1))

triangle_numbers = TriangleNumberCache()

_ord_a = ord('a')
_all_letters = set("abcdefghijklmnopqrstuvwxyz")
def char_to_int(c):
    c = c.lower()
    if c not in _all_letters:
        return 0
    return ord(c) - _ord_a + 1

def is_triangle_word(w):
    word_value = 0
    for c in w:
        word_value += char_to_int(c)
    return word_value in triangle_numbers

if __name__ == "__main__":
    with open("P42_Input.txt") as f:
        count_triangle_words = 0
        for w in f.read().split(","):
            if is_triangle_word(w):
                count_triangle_words += 1
    
    print(count_triangle_words)
