-- Project Euler Solutions
-- Problem 71: Ordered Fractions
-- Solved by: Quinn Mortimer (modimore)
import System.Environment (getArgs)
import Data.List (maximumBy)

solve d =
    extractNum $ maximumBy compareTup (map makeTup [1..d])
    where
        compareTup (_,_,x) (_,_,y) = compare x y
        makeTup d = let n = div (3*d-1) 7 in (d, n, fromIntegral n / fromIntegral d)
        extractNum (_,n,_) = n

main = do
    args <- getArgs
    let dMax = if null args then 1000000 else (read :: String -> Int) (head args)
    putStrLn . show $ solve dMax
