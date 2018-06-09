from eutil.primes import primes

def factor_(n):
    factors = set()
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                factors.add(i)
                n //= i
                break
    return factors

def factor(n):
    factors = set()
    primes_iter = iter(primes)
    p = next(primes_iter)
    while n > 1:
        if p > n:
            break
        elif p == n:
            factors.add(p)
            break
        elif n % p == 0:
            factors.add(p)
            n //= p
            while n % p == 0:
                n //= p
        p = next(primes_iter)
    return factors

def compose_from_prime_factors(num_factors, limit=None):
    if num_factors == 0:
        yield 1
    elif limit is None:
        for p in primes:
            for q in compose_from_prime_factors(num_factors-1, p):
                yield p * q
    else:
        for p in primes:
            if p < limit:
                for q in compose_from_prime_factors(num_factors-1, p):
                    yield p * q
            else:
                raise StopIteration

if __name__ == "__main__":
    import sys
    
    scope = 4
    if len(sys.argv) > 1:
        try:
            scope = int(sys.argv[1])
        except ValueError:
            pass
    
    n = 2
    run = 0
    while run < scope:
        if len(factor(n)) == scope:
            run += 1
        else:
            run = 0
        n += 1
    print(n-scope)
