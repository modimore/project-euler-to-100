module EulerUtil.NumberTheory (phi)
where

import EulerUtil.Primes (isPrime, primes)

-- Euler's Totient Function
phi n
    | n == 1 = 1
    | isPrime n = n-1
    | otherwise = div (phi m * phi p * g) (phi g)
        where
            p = head (dropWhile (\p -> mod n p /= 0) primes)
            m = div n p
            g = gcd m p
