import System.Environment (getArgs)
import EulerUtil.Numbers(factorial, digitList)

-- Find the sum of all numbers which are equal to the sum of factorials
-- of their digits.

-- Oddly enough, the memoized version of the factorial function performs
-- worse in this scenario. Maybe because only factorials up to 9 are calculated
-- and because indexing into the list has a linear cost too.

main = do
    let max = (length (digitList fact9)) * fact9 where fact9 = factorial 9
    putStrLn (show max)
    let matches = filter (\x -> x == sum (map factorial (digitList x))) [10..max]
    putStrLn (show matches)
    putStrLn . show $ sum matches
