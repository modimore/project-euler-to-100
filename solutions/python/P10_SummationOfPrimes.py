from eutil.primes import primes_below
from sys import argv

N = 2000000

if len(argv) > 1:
    try:
        N = int(argv[1])
    except ValueError:
        pass

print("Summing all primes less than {}...".format(N))

prime_sum = sum(primes_below(N))

print(prime_sum)
