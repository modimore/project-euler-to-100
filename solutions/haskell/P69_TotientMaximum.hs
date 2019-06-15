-- Project Euler Problem 69: Totient Maximum
-- Solved by: Quinn Mortimer (modimore)
import System.Environment (getArgs)
import EulerUtil.NumberTheory (phi)

-- divf a b = (fromIntegral a) / (fromIntegral b)

-- maximumBy f l = fst $ foldl (\a b -> if snd a >= snd b then a else b) (1,1) (map (\a -> (a, f a)) l)

accumulate op [] = []
accumulate op [x] = [x]
accumulate op x0:x1:xs = r0:(accHelper op x1:xs r0)
    where
        r0 = op x0 x1
        accHelper op xs i = []

main = do
    args <- getArgs
    let n = case args of
            [] -> 1000000
            n:_ -> (read n :: Integer)
    -- let result = maximumBy (\n -> divf n (phi n)) [2..n]
    let result = head . takeWhile (<n) (foldl (*) primes)
    putStrLn . show $ result
