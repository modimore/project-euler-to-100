-- Solution is correct, but the code could be way better
-- 1. Use command line arguments or run as an interaction
-- 2. Functions are defined somewhat messily
-- 3. Should think a little bit about obvious optimizations
import System.Environment

sum_squares 0 = 0
sum_squares n = n*n + sum_squares (n-1)

square_sum n = let sum_to_n = sum [0..n] in sum_to_n*sum_to_n

sum_square_difference :: Int -> Int
sum_square_difference 0 = 0
sum_square_difference n = (square_sum n) - (sum_squares n)

-- main = do
--     n <- getLine
--     putStrLn $ show (sum_square_difference (read n))
main = do
    n:_ <- getArgs
    putStrLn $ show (sum_square_difference (read n))
