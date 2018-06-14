modexp _ 0 _ = 1
modexp base 1 lim = mod base lim
modexp base 2 lim = mod ((modexp base 1 lim)^2) lim
modexp base pow lim
    | mod pow 2 == 0 = modexp (modexp base 2 lim) (div pow 2) lim
    | otherwise = modexp (base * (modexp base (pow-1) lim)) 1 lim

main = do
    -- This is actually a bit faster sometimes, but without
    -- infinite size integers it could get a bit dicey on correctness.
    --putStrLn . show $ mod (sum (map (\x -> x^x) [1..1000])) (10^10)
    -- This should work with larger integers even with a smaller integer
    -- type because modular exponentiation will let us keep the ints small.
    putStrLn . show $ foldl (\x y -> mod (x+y) (10^10)) 0 (map (\x-> modexp x x (10^10)) [1..1000])
