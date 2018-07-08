import EulerUtil.Numbers (fact_memo)

fact = fact_memo

count_combinations n r
    | r <= n = div (fact n) (fact r * fact (n-r))

main = do
    --putStrLn . show $ map fact [0..100]
    let ct_combinations = length $ filter (>1000000) [ count_combinations n r | n <- [1..100], r <- [1..n] ]
    putStrLn $ show ct_combinations
