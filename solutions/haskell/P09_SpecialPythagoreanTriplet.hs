isPythagoreanTriple :: (Int, Int, Int) -> Bool
isPythagoreanTriple (a, b, c) = (a*a + b*b == c*c)

tripleSum :: Int -> (Int, Int, Int)
tripleSum n = head $ dropWhile (\(a, b, c)-> a + b + c /= n) [(a, b, c) | c<-[1..(div n 2)], b<-[1..c], a<-[1..b], isPythagoreanTriple (a,b,c)]
--tripleSum n = head $ dropWhile (\(a, b, c)-> a + b + c /= n) [(a, b, c) | a<-[1..(div n 2)], b<-[a..n], c<-[b..n], isPythagoreanTriple (a,b,c)]

main = do
    putStrLn . show $ tripleSum 1000
