-- Project Euler Problem 69: Totient Maximum
-- Solved by: Quinn Mortimer (modimore)
import System.Environment (getArgs)
import EulerUtil.Primes (isPrime, primes)

divf a b = (fromIntegral a) / (fromIntegral b)

maximumBy f l = fst $ foldl (\a b -> if snd a >= snd b then a else b) (1,1) (map (\a -> (a, f a)) l)

phi n
    | n == 1 = 1
    | isPrime n = n-1
    | otherwise = div (phi m * phi p * g) (phi g)
        where
            p = head (dropWhile (\p-> mod n p /= 0) primes)
            m = div n p
            g = gcd m p

main = do
    n:_ <- getArgs
    putStrLn . show $ maximumBy (\n -> divf n (phi n)) [2..(read n :: Integer)]
