from .factorial import factorial
from .primes import primes

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
