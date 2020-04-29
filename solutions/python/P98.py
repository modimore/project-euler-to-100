"""Project Euler Solutions
Problem 98: Anagramic Squares
Solved by: Quinn Mortimer (modimore)
"""
from itertools import combinations, permutations
from math import sqrt

def is_square(n):
    sqrt_n = sqrt(n)
    return sqrt_n == int(sqrt_n)

def score(a, b):
    score = 0
    chars = list(set(c for c in a))
    for vals in permutations(range(1, 10), len(chars)):
        char_vals = { char: val for char, val in zip(chars, vals) }
        ax = bx = 0
        for c in a:
            ax = ax * 10 + char_vals[c]
        for c in b:
            bx = bx * 10 + char_vals[c]
        if is_square(ax) and is_square(bx):
            score = max(score, max(ax, bx))
    return score

def ana(words):
    best = 0
    anas = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in anas:
            anas[key] = [word]
        else:
            anas[key].append(word)
    for key in anas:
        if len(anas[key]) == 1:
            continue
        for w1, w2 in combinations(anas[key], 2):
            best = max(best, score(w1, w2))
    return best

def solve(filename="P98_Input.txt"):
    with open(filename) as f:
        words = list(line.strip() for line in f)
    return ana(words)

if __name__ == "__main__":
    print(solve())
