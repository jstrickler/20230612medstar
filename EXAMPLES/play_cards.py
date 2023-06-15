from carddeck import CardDeck
from jokerdeck import JokerDeck

from module import name
import module
#  module.name

deck = CardDeck("Mary")

deck.shuffle()

for _ in range(10):
    card = deck.draw()
    print(card)
print()

print(deck)

print(deck.cards)
print(len(deck))   #   CardDeck.__len__(deck)

print(deck)
print(repr(deck))

deck2 = CardDeck("Fiona")

new_deck = deck + deck2
print(new_deck)
print(len(new_deck))

j1 = JokerDeck("Jerry")
j2 = JokerDeck("Jeannie")

j1.shuffle()
print(f"j1: {j1}")
print(f"len(j1): {len(j1)}")
print(j1.cards)

# print(f"len(j1): {len(j1)}")
