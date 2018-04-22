import System.Environment (getArgs)

find_divisors :: Int -> [Int]
find_divisors 0 = []
find_divisors 1 = []
find_divisors n = 1 : low_divisors ++ [ div n p | p <- reverse low_divisors, div n p /= p ]
    where low_divisors = [ p | p <- takeWhile (\x -> x*x <= n) [2..], (mod n p) == 0 ]

is_abundant :: Int -> Bool
is_abundant n = n < sum (find_divisors n)

main = do
    args <- getArgs
    let limit = read (head args)
    let abundant_nums = filter (is_abundant) [1..limit]
    let abundant_sums = [ m + n | m <- abundant_nums, n <- abundant_nums, m + n <= limit ]
    putStrLn . show $ sum (filter (\m -> not (elem m abundant_sums)) [1..limit])
