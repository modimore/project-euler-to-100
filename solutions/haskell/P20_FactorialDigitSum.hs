fact 0 = 0
fact 1 = 1
fact n = n * fact (n-1)

digit_sum n
    | n < 0 = digit_sum (-n)
    | n < 10 = n
    | otherwise = (mod n 10) + digit_sum (quot n 10)

factorial_digit_sum n = digit_sum $ fact n

main = do
    putStrLn $ show $ factorial_digit_sum 100
