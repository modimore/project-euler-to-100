"""Project Euler Solutions
Problem 95: Amicable chains
Solved by: Quinn Mortimer (modimore)
"""
from eutil.divisors import find_proper_divisors

def next_amicable(n):
    return sum(find_proper_divisors(n))

# This function has been inlined into the solve method
# so we can exit early based on the limit number,
# but it demonstrates the approach taken to find chains.
#def find_amicable_chain(n):
#    n0 = n
#    next_ns = {}
#    while n not in next_ns:
#        nx = next_ns[n] = next_amicable(n)
#        n = nx
#    n0, chain = n, [n]
#    n = next_ns[n]
#    while n != n0:
#        chain.append(n)
#        n = next_ns[n]
#    return chain

def solve(L=int(1E6)):
    chained, seen = set(), set()
    best_chain = []
    best_min = L
    
    for n in range(L):
        if n in chained or n in seen:
            continue
        
        n0 = n
        next_ns = {}
        while n not in next_ns:
            if n > L or n in chained:
                break
            seen.add(n)
            
            nx = next_ns[n] = next_amicable(n)
            n = nx
        
        if n > L or n in chained:
            continue
        
        c0, chain = n, [n]
        c = next_ns[c0]
        while c != c0:
            chain.append(c)
            c = next_ns[c]

        chained |= set(chain)
        
        if any(x > L for x in chain):
            continue
        
        if len(chain) < len(best_chain):
            continue
        if len(chain) > len(best_chain):
            best_chain = chain
            best_min = min(chain)
        elif len(chain) == len(best_chain):
            chain_min = min(chain)
            if chain_min < best_min:
                best_chain = chain
                best_min = chain_min
    
    return best_min

if __name__ == "__main__":
    from sys import argv
    N = int(1E6)
    if len(argv) > 1:
        try:
            N = int(argv[1])
        except ValueError:
            pass
    
    print("Solution:", solve(N))
