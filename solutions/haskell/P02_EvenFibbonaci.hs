fib_at :: Int -> Integer
fib_at = (map fib [0..] !!)
    where fib 0 = 0
          fib 1 = 1
          fib n = fib_at (n-1) + fib_at (n-2)

-- fib_at :: Int -> Integer
-- fib_at 0 = 0
-- fib_at 1 = 1
-- fib_at n = fib_at (n-1) + fib_at (n-2)

main = do
    let fib_sum = sum $ filter odd $ takeWhile (<4000000) (map fib_at [0..])
    putStrLn $ show fib_sum
