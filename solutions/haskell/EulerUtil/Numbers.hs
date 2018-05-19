module EulerUtil.Numbers (
    digitList,
    factorial,
    fact_memo
) where

-- Return a list of the digits in a (non-negative) integer
-- digitList :: Integral a => a -> [a]
digitList :: Int -> [Int]
digitList n
    | n < 10 = n:[]
    | otherwise = digitList (div n 10) ++ [mod n 10]

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

fact_memo n = (map factorial [0..]) !! n
