module EulerUtil.Primes (primesTo) where
-- Generate primes up to m
primesTo :: Int -> [Int]
primesTo m
    | m <  2 = []
    | m == 2 = []
    | otherwise = 2 : sieve [3,5..m]
        where sieve [] = []; sieve (x:xs) = x : sieve (filter (\n-> mod n x /= 0) xs)
