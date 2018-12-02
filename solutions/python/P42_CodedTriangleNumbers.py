"""Project Euler Solutions
Problem 42: Coded triangle numbers
Solved by: Quinn Mortimer (modimore)
"""
from eutil.numbers import triangle_numbers

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
