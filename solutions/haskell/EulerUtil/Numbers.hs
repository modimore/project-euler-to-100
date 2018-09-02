module EulerUtil.Numbers (
    digitList,
    factorial,
    fact_memo
) where

-- Return a list of the digits in a (non-negative) integer
-- digitList :: Integral a => a -> [a]
digitList :: Integral a => a -> [a]
digitList n
    | n < 10 = n:[]
    | otherwise = digitList (div n 10) ++ [mod n 10]

factorial :: Integral a => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)

fact_memo n = (map factorial [0..]) !! n
fact = fact_memo
