numChangeOptions :: Int -> [Int] -> Int
numChangeOptions amount coins
    | null coins  = 0
    | amount < 0  = 0
    | amount == 0 = 1
    | otherwise   = (numChangeOptions (amount - max_coin) coins) + (numChangeOptions amount smaller_coins)
        where
            max_coin = maximum coins
            smaller_coins = filter (< max_coin) coins

main = do
    let numOptions = numChangeOptions 200 (reverse [1, 2, 5, 10, 20, 50, 100, 200])
    putStrLn $ show numOptions
