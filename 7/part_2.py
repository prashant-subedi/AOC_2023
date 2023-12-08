from collections import Counter, OrderedDict
from functools import total_ordering

@total_ordering
class Card:
    weights = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,  # Weekest card
        "T": 10
    }
    def __init__(self, card_value: str) -> None:
        self.name = card_value
        if card_value.isdigit():
            self.weight = int(card_value)
        else:
            self.weight = self.weights[card_value]

    def __hash__(self) -> str:
        return hash(self.name)
        
    def __eq__(self, other: object) -> bool:
        return self.weight == other.weight

    def __lt__(self, other: object) -> bool:
        return self.weight < other.weight
    
    def __repr__(self):
        return str(self.name) 
    
class Hand:
    def __init__(self, cards: list[Card], rank: int) -> None:
        self.cards = cards
        self.rank = rank

        joker_card = Card("J")
        card_counts = Counter(self.cards)
        if len(card_counts) == 1:
            self.counts = [len(cards)]
            return
        joker_count = card_counts[joker_card]
        self.counts = []
        for card, count in card_counts.most_common():
            if card == joker_card:
                continue
            self.counts.append(count + joker_count)
            joker_count = 0
        

    def __eq__(self, other: object) -> bool:
        return self.cards == self.cards
    

    def __lt__(self, other):
        for count, other_count in zip(self.counts, other.counts):
            if count != other_count:
                return count < other_count
        for card, other_card in zip(self.cards, other.cards):
            if card == other_card:
                continue
            return card < other_card
        return False
        
    @classmethod
    def parse(cls, raw_string: str):
        raw_hand, rank = raw_string.split(" ", 1)
        return cls([Card(i) for i in raw_hand], int(rank))

    def __repr__(self):
        return f"{self.cards}" # | {self.rank}"
    

def main():
    hands = []
    total_ranks = 0
    with open("input.txt") as t:
        for raw_hand in t:
            hands.append(Hand.parse(raw_hand))
    for i, hand in enumerate(sorted(hands)):
        total_ranks+= (i+1) * hand.rank
    print(total_ranks)

if __name__ == "__main__":
    main()