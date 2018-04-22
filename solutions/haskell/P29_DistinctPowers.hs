import Data.Set as Set (fromList, size)
import System.Environment (getArgs)

generatePowerSet a b = Set.fromList [_b^e | _b<-[2..a], e<-[2..b]]

main = do
    args <- getArgs
    let a:b:[] = take 2 (map (read) args)
    putStrLn . show $ Set.size (generatePowerSet a b)
