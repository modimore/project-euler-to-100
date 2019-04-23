"""Project Euler Solutions
Problem 32: Pandigital products
Solved by: Quinn Mortimer (modimore)
"""
def all_permutations(seq):
    if len(seq) < 2:
        yield seq[:]
    else:
        for p_seq in all_permutations(seq[1:]):
            first = seq[:1]
            for i in range(len(seq)):
                yield p_seq[:i] + first + p_seq[i:]

if __name__ == "__main__":
    # note: not using itertools because itertools.permutations
    # yields a tuple for each permutation, as opposed to
    # preserving the type of the original sequence.
    all_pandigital_products = set()
    for perm in all_permutations("123456789"):
        a, b, c = perm[0:1], perm[1:5], perm[5:9]
        if int(a) * int(b) == int(c):
            all_pandigital_products.add(int(c))
        a, b, c = perm[0:2], perm[2:5], perm[5:9]
        if int(a) * int(b) == int(c):
            all_pandigital_products.add(int(c))
    print(sum(all_pandigital_products))
