"""Project Euler Solutions
Problem 87: Prime power triples
Solved by: Quinn Mortimer (modimore)
"""
from math import sqrt
from eutil.primes import primes, primes_below

def solve(L=int(5E7)):
    ppts = set()
    for p2 in primes_below(1+int(L**0.5)):
        p22 = p2**2
        if p22 > L:
            break
        
        for p3 in primes_below(1+(L-p22)**(1/3)):
            p22p33 = p22+p3**3
            if p22p33 > L:
                break
            
            for p4 in primes_below(1+(L-p22p33)**0.25):
                ppt = p22p33 + p4**4
                if ppt > L:
                    break
                ppts.add(ppt)
    
    return len(ppts)

if __name__ == "__main__":
    from sys import argv
    L = int(5E7)
    if len(argv) > 1:
        try:
            L = int(argv[1])
        except ValueError:
            pass
        
    print(solve(L))
