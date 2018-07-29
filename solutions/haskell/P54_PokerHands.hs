-- Project Euler Problem 54 Solution

import Data.List (group, groupBy, sort, sortOn)

data CardSuit = Clubs | Diamonds | Hearts | Spades deriving Eq
data CardFace = Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King | Ace
    deriving (Eq, Ord, Enum)
data Card = Card { suit :: CardSuit, face :: CardFace }

data PokerHandRank = HighCard | Pair | TwoPair | ThreeOfAKind | Straight | Flush | FullHouse | FourOfAKind | StraightFlush | RoyalFlush
    deriving (Eq, Ord, Enum)

data PokerHand = PokerHand { cards :: [Card], rank :: PokerHandRank, rankContext :: [CardFace] }

rankHand :: [Card] -> (PokerHandRank, [CardFace])
rankHand cards
    | hasFlush && hasStraight && (face . head) sortedCards == Ace = (RoyalFlush, map face sortedCards)
    | maxGroupSize == 4 = (FourOfAKind, context)
    | (sort . (map length)) groupedCards == [2, 3] = (FullHouse, context)
    | hasFlush = (Flush, map face sortedCards)
    | hasStraight = (Straight, map face sortedCards)
    | maxGroupSize == 3 = (ThreeOfAKind, context)
    | (length . (filter (==2)) . (map length)) groupedCards == 2 = (TwoPair, context)
    | maxGroupSize == 2 = (Pair, context)
    | otherwise = (HighCard, map face sortedCards)
    where
        hasFlush = isFlush cards
        hasStraight = isStraight cards
        sortedCards = reverse $ sortOn face cards
        groupedCards = groupBy (\a b -> face a == face b) $ sortOn face cards
        maxGroupSize = maximum (map length groupedCards)
        context = (map face) . (map head) . reverse . (sortOn length) $ groupedCards

isFlush :: [Card] -> Bool
isFlush = (==1) . length . group . map suit

isStraight :: [Card] -> Bool
isStraight cards = helper . sort . (map face) $ cards
    where
        helper (x:[]) = True
        helper (x:y:zs) = succ x == y && helper (y:zs)

isWin :: PokerHand -> PokerHand -> Bool
isWin hand1 hand2
    | rank hand1 == rank hand2 = compareContext (rankContext hand1) (rankContext hand2)
    | otherwise = rank hand1 > rank hand2
    where
        compareContext [] [] = False
        compareContext (c1:context1) (c2:context2)
            | c1 == c2 = compareContext context1 context2
            | otherwise = c1 > c2

cardFace :: Char -> CardFace
cardFace '2' = Two
cardFace '3' = Three
cardFace '4' = Four
cardFace '5' = Five
cardFace '6' = Six
cardFace '7' = Seven
cardFace '8' = Eight
cardFace '9' = Nine
cardFace 'T' = Ten
cardFace 'J' = Jack
cardFace 'Q' = Queen
cardFace 'K' = King
cardFace 'A' = Ace

cardSuit :: Char -> CardSuit
cardSuit 'C' = Clubs
cardSuit 'D' = Diamonds
cardSuit 'H' = Hearts
cardSuit 'S' = Spades

parseCard :: [Char] -> Card
parseCard [f, s] = Card (cardSuit s) (cardFace f)

parseHand :: [String] -> PokerHand
parseHand cardStrings =
    let cards = map parseCard cardStrings
        (ranking, rankContext) = rankHand cards
    in PokerHand cards ranking rankContext

parseHands :: [String] -> (PokerHand, PokerHand)
parseHands cardStrings
    | length cardStrings == 10 = (parseHand (take 5 cardStrings), parseHand (drop 5 cardStrings))
    | otherwise = error "Wrong number of cards dealt."

main = do
    dealtLines <- readFile "P54_Input.txt"
    let count = length . (filter (\p -> isWin (fst p) (snd p))) $ map parseHands $ map words (lines dealtLines)
    putStrLn . show $ count
