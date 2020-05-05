"""Project Euler Solutions
Problem 34: Digit factorials
Solved by: Quinn Mortimer (modimore)
"""
from math import ceil, log
from eutil.number_theory import factorial as fact

# Using the canonical definition of factorial is about 5 seconds
# slower than this memoised version. This isn't totally unexpected,
# as this algorithm only ever uses factorials for 0-9, which are fairly
# quick to brute-force as often as needed.

def digit_list(n):
    if n < 0:
        return digit_list(-n)
    if n == 0:
        return [0]
    
    digit_list = []
    while n > 0:
        digit_list.append(n%10)
        n //= 10
    return digit_list[::-1]

fact9 = fact(9)
limit = int(ceil(log(1.0*fact9, 10))) * fact9

match_sum = 0
for n in range(10, limit):
    if n == sum(map(fact, digit_list(n))):
        match_sum += n

print("Sum of matches:", match_sum)
