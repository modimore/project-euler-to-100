-- Project Euler Problem 56 Solution

import EulerUtil.Numbers (digitList)

-- solve :: Integral a => a -> a -> a
solve lim_a lim_b = foldl max 0 (map (sum.digitList) [ a^b | a<-[1..lim_a-1], b<-[0..lim_b-1]])

main = do
    putStrLn . show $ solve 100 100
