from eutil.primes import primes
from sys import argv

N = 2000000

if len(argv) > 1:
    try:
        N = int(argv[1])
    except ValueError:
        pass

print("Summing all primes less than {}...".format(N))

prime_iterator = iter(primes)
prime_sum = 0

p = next(prime_iterator)
while p < N:
    prime_sum += p
    p = next(prime_iterator)

print(prime_sum)
