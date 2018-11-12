from eutil.primes import primes, primes_below

MAX_COEFF = 1000

best_run = (None, None, 0)

#for a in range(-MAX_COEFF+1, MAX_COEFF):
#    for b in range(-MAX_COEFF, MAX_COEFF+1):
#        n = 0
#        f_n = n**2 + a*n + b
#        while f_n in primes:
#            n += 1
#            f_n = n**2 + a*n + b
#        if n > best_pair[1]:
#            best_pair = (a*b, n)

# To get a prime at n=0, b must be prime.
# A lot faster, but I don't know if negative numbers count as prime.
# This skips all of them so if they do it's probably not a correct
# algorithm.
# update: Negative numbers are not prime.
for b in primes_below(MAX_COEFF+1):
    for a in range(-MAX_COEFF+1, MAX_COEFF):
        n = 0
        f_n = n**2 + a*n + b
        while f_n in primes:
            n += 1
            f_n = n**2 + a*n + b
        if n > best_run[2]:
            best_run = (a, b, n)

print(best_run)
