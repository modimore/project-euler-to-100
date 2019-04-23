"""Project Euler Solutions
Problem 24: Lexicographic permutations
Solved by: Quinn Mortimer (modimore)
"""
INDEX = 1000000

def lexicographic_permutations(seq):
    if len(seq) < 2:
        yield seq[:]
    else:
        seq = sorted(seq)
        for i in range(len(seq)):
            rest = seq[:]
            first = rest.pop(i)
            for perm in lexicographic_permutations(rest):
                yield [first] + perm

if __name__ == "__main__":
    seq = list(range(10))
    perms = zip(range(INDEX), lexicographic_permutations(seq))
    print("".join(str(e) for e in list(perms)[-1][1]))
