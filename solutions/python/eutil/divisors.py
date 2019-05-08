from math import sqrt

def find_proper_divisors(n):
    if n < 2:
        return []
        
    divisors_n = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors_n.add(i)
    
    divisors_n = divisors_n | set(n // x for x in divisors_n)
    divisors_n.add(1)
    
    return sorted(divisors_n)
