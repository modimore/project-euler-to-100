"""Project Euler Solutions
Problem 65: Convergents of e
Solved by: Quinn Mortimer (modimore)
"""

def e_continued_fraction_elems():
    n = 1
    yield 2
    while True:
        yield 1
        yield n * 2
        yield 1
        n += 1

def normalize_mixed_number(w, n, d):
    return w * d + n, d

def solve(d=100):
    seq = [s for s, _ in zip(e_continued_fraction_elems(), range(d))]
    numer, denom = 0, 1
    for s_i in seq[::-1]:
        denom, numer = normalize_mixed_number(s_i, numer, denom)
    return sum(int(digit) for digit in str(denom))

if __name__ == "__main__":
    from sys import argv
    D = 100
    if len(argv) > 1:
        try:
            D = int(argv[1])
        except ValueError:
            pass
    print(solve(D))
