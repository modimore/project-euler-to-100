"""Project Euler Solutions
Problem 35: Circular primes
Solved by: Quinn Mortimer (modimore)
"""
from eutil.primes import primes

N = 1000000

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try: N = int(sys.argv[1])
        except ValueError: pass
    
    circ_primes_count = 0
    for n in range(1, N):
        s_n = str(n)
        is_circ_prime = True
        for i in range(len(s_n)):
            if int(s_n) not in primes:
                is_circ_prime = False
                break
            s_n = s_n[1:] + s_n[:1]
        if is_circ_prime:
            circ_primes_count += 1
    
    print("Number of circular primes:", circ_primes_count)
