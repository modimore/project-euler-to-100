import System.Environment (getArgs)
--import EulerUtil.Primes (primesTo)

primesTo :: Int -> [Int]
primesTo m
    | m <  2 = []
    | m == 2 = [2]
    | otherwise = 2 : sieve [3,5..m]
        where sieve [] = []; sieve (x:xs) = x : sieve (filter (\n-> mod n x /= 0) xs)

main = do
    arguments <- getArgs
    let n = read $ head arguments
    let result = sum $ primesTo n
    putStrLn $ show result
