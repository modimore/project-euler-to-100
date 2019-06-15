"""Project Euler Solutions
Problem 54: Poker hands
Solved by: Quinn Mortimer (modimore)
"""

# Define a value for the poker hands (in best-to-worst order)
ROYAL_FLUSH = 9
STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
PAIR = 1
HIGH_CARD = 0

# Define the value of each card face
face_to_value = {str(x): x for x in range(2, 10)}
face_to_value.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})

def evaluate_poker_hand(cards):
    """Provides a value that can be compared to compare card hands.
    
    The evaluation of the hand provided by this method is a tuple
    of integers, the first of which denotes the type of hand so that
    the cards in each type would only be compared against themselves.
    
    Then as much context-specific information as is needed to break
    ties when coming up against another hand of the same type. So for a
    pair of 2s, the value 2 would be the context provided.
    
    All hands have the descending values of all cards attached to the
    end, since that is the universal tie-breaking method.
    """
    
    cards_ord = sorted(cards, reverse=True)
    suits = {card.suit for card in cards}
    high = cards_ord[0].value
    
    is_flush = len(suits) == 1
    is_straight = all(
        cards_ord[i].value == cards_ord[i-1].value-1 for i in range(1,len(cards)))
    
    cards_by_value = {card.value: [] for card in cards}
    for card in cards:
        cards_by_value[card.value].append(card)
    
    quads, triples, pairs = [], [], []
    for value in sorted(cards_by_value.keys(),
            key=lambda g: (len(cards_by_value[g]), g), reverse=True):
        if len(cards_by_value[value]) == 4:
            quads.append(cards_by_value[value])
        elif len(cards_by_value[value]) == 3:
            triples.append(cards_by_value[value])
        elif len(cards_by_value[value]) == 2:
            pairs.append(cards_by_value[value])
    
    if is_flush and is_straight:
        evaluation = [ROYAL_FLUSH if high == 14 else STRAIGHT_FLUSH]
    elif len(quads) == 1:
        evaluation = [FOUR_OF_A_KIND, quads[0][0].value]
    elif len(triples) == 1 and len(pairs) == 1:
        evaluation = [FULL_HOUSE, triples[0][0].value, pairs[0][0].value]
    elif is_flush:
        evaluation = [FLUSH]
    elif is_straight:
        evaluation = [STRAIGHT]
    elif len(triples) == 1:
        evaluation = [THREE_OF_A_KIND, triples[0][0].value]
    elif len(pairs) == 2:
        evaluation = [TWO_PAIR, pairs[0][0].value, pairs[1][0].value]
    elif len(pairs) == 1:
        evaluation = [PAIR, pairs[0][0].value]
    else:
        evaluation = [HIGH_CARD]
    
    evaluation.extend(card.value for card in cards_ord)
    
    return tuple(evaluation)

class Card:
    """Simple comparable card type."""
    def __init__(self, info):
        self.face, self.suit = info[:-1], info[-1]
        self.value = face_to_value[self.face]
    
    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __repr__(self):
        return "<{}:{}{}>".format(self.__class__, self.face, self.suit)

class PokerHand:
    """Simple comparable poker hand type."""
    def __init__(self, cards):
        self.cards = cards
        self._evaluation = evaluate_poker_hand(cards)
    
    def __eq__(self, other):
        self_cards = sorted(self.cards)
        other_cards = sorted(other.cards)
        return all(self_cards[i] == other_cards[i] for i in range(len(self_cards)))
    
    def __lt__(self, other):
        return self._evaluation < other._evaluation
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return self._evaluation > other._evalation
    
    def __ge__(self, other):
        return self > other or self == other

def solve(filename="P54_Input.txt"):
    p1_wins = 0
    with open(filename, "r") as hands_file:
        for row in hands_file:
            if len(row.split()) == 0:
                continue
            
            cards = [Card(s) for s in row.split()]
            p1_hand, p2_hand = PokerHand(cards[:5]), PokerHand(cards[5:])
            if p2_hand < p1_hand:
                p1_wins += 1
    return p1_wins

if __name__ == "__main__":
    print("Solution:",solve())
