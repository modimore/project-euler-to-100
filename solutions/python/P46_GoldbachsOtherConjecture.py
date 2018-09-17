from math import sqrt
from eutil.primes import primes

def find_goldbach_disprover():
    n = 1
    found = False
    while not found:
        n += 2
        if n in primes:
            continue
        
        any_matches = False
        for p in primes:
            if p >= n:
                break
            i = sqrt((n-p)//2)
            if i == int(i):
                any_matches = True
                break
        if not any_matches:
            break
    return n

if __name__ == "__main__":
    print("First Goldbach Disprover:", find_goldbach_disprover())

