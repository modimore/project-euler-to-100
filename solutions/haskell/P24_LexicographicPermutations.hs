lex_perms :: [a] -> [[a]]
lex_perms   [] = []
lex_perms x:[] = [x]
lex_perms x:xs = map (\l -> x:l) (lex_perms xs)

main = do
    let index = 1000000
    return ()
