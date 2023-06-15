from card import Card
from carddeck import CardDeck

JOKER = '\U0001F0CF'

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call parent version
        for _ in range(2):
            card = Card(JOKER, "Joker")
            self._cards.append(card)
