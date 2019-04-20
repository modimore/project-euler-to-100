"""Project Euler Solutions
Problem 26: Reciprocal cycles
Solved by: Quinn Mortimer (modimore)
"""
from eutil.number_theory import gcd_euclidean as gcd

# This one is tricky IMO because it seems like you have to do it
# with integers in a language that has Big Integer support. A really large
# number of base 10 digits is needed to solve this.

LIMIT = 1000
# You can get a lot of different answers based on what you set the
# dividend to. This produced what the server said was the correct solution
# for me, but I tried a couple of others before this.
# Edit: Before I had 10000, but you only need around this many to get the
#       correct answer (value and length of cycle).
MAX = 10**(2950)

def find_longest_recurring(n):
    search_text = str(quot)[::-1].lstrip("0")
    for l in range(1,len(search_text) // 2):
        match = search_text[:l]
        found = True
        for i in range(1, len(search_text) // l - 1):
            if search_text[i*l:i*l+l] != match:
                found = False
                break
        if found:
            return match[::-1]

    return None

best = (None, 0)
for x in range(2, LIMIT):
    if gcd(x, 10) > 1:
        continue
    quot = MAX // x
    longest = find_longest_recurring(quot)
    if longest is None:
        continue
    if len(longest) > best[1]:
        best = (x, len(longest))

print(best)
