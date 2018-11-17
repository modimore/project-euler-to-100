from eutil.primes import primes, primes_below
from math import inf

def check_pair(m, n):
    s0, s1 = str(m), str(n)
    return int(s0+s1) in primes and int(s1+s0) in primes

def make_group(group, cache, avail, target):
    if target == 0:
        yield group
    if len(avail) < target:
        return
    
    for n in sorted(avail):
        for _group in make_group(group | {n}, cache, avail & cache[n], target-1):
            yield _group

def solve(n_primes=5):
    pair_cache = {}
    
    best_group, best = None, inf
    
    for p in primes:
        if p > best:
            break
        
        cache_p = set()
        to_beat = best - p
        for _p in primes_below(p):
            if _p <= to_beat and check_pair(p, _p):
                cache_p.add(_p)
                pair_cache[_p].add(p)
        pair_cache[p] = cache_p
        
        if len(cache_p)+1 < n_primes:
            continue
        if sum(sorted(cache_p)[:n_primes-1]) > to_beat:
            continue
        
        for group in make_group({p}, pair_cache, cache_p, n_primes-1):
            group_total = sum(group)
            if group_total < best:
                best_group, best = group, group_total
    
    return best

if __name__ == "__main__":
    from sys import argv
    N = 5
    try: N = int(argv[1])
    except: pass
    primes.to(100000)
    print("Solution:", solve(N))
