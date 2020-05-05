"""Project Euler Solutions
Problem 51: Prime digit replacements
Solved by: Quinn Mortimer (modimore)
"""
from math import log, inf
from eutil.numbers import digit_list
from eutil.primes import primes, primes_below

def get_key(i, digits_x):
    key = []
    for j in range(len(digits_x)):
        if 2**j & i > 0:
            key.append(digits_x[j])
        else:
            key.append(None)
    return tuple(key)

def problem51(size=8):
    num_digits = 1
    ans = inf
    
    while True:
        groups = {}
        for i in range(2**num_digits):
            k_i = lambda digits: get_key(i, digits)
            
            for p in primes_below(10**num_digits):
                if int(log(p, 10)) != num_digits-1:
                    continue
                
                digits_p = digit_list(p)
                key = k_i(digits_p)
                
                if len(set(d for k, d in zip(key, digits_p) if k is None)) > 1:
                    continue
                
                if key not in groups:
                    groups[key] = []
                groups[key].append(p)
        
        for group in groups.values():
            if len(group) == size:
                ans = min(ans, min(group))
        
        if ans != inf:
           break 
                
        num_digits += 1
    
    return ans

if __name__ == "__main__":
    print("Solution:", problem51())
