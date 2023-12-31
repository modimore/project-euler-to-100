module EulerUtil.Primes (
    primes,
    primesTo,
    isPrime
) where

primes = 2 : sieve [3,5..]
    where sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0]

primesTo m = takeWhile (<=m) primes

isPrime n = n == head (dropWhile (<n) primes)
