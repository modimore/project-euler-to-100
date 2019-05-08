from itertools import takewhile

def unique_permutations(seq):
    if len(seq) < 2:
        yield seq[:]
    else:
        seq = sorted(seq)
        idx = 0
        while idx < len(seq):
            el = seq[idx]
            count_el = sum(1 for x in takewhile(lambda x: x == el, seq[idx:]))
            for perm in unique_permutations(seq[:idx]+seq[idx+1:]):
                yield [el] + perm
            idx += count_el
