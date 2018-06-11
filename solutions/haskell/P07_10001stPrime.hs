import EulerUtil.Primes (primes)

main = do
    let p10001 = head (drop 10000 primes)
    putStrLn . show $ p10001
