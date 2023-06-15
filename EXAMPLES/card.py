
class Card:
    # constructor
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property    # property is a decorator
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # to-string for the interpreter
    def __repr__(self):
        return f"Card('{self._rank}', '{self._suit}')"

    # to-string for the programmer
    def __str__(self):
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    c1 = Card('6', 'Hearts')
    print(f"c1: {c1}\n")
    print(f"c1.rank: {c1.rank}")
    print(f"c1.suit: {c1.suit}")
    print(repr(c1))
    c2 = Card('5', 'Diamonds')
    cards = [c1, c2]
    print(f"cards: {cards}")
    print(f"c2: {c2}")
    
    
