import random
from .card import Card
from .constant import suits, ranks


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
                
        # Alternative
        # self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def __str__(self):

        deck_comp = ""
        for card in self.deck:
            deck_comp += f"\n{card.__str__()}"
        return f"The deck has: {deck_comp}\nTotal = {len(self.deck)} cards"

        ## Alternative
        # card = [str(card) for card in self.deck]
        # return f"{card}\nThere is {len(card)} cards"
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


if __name__ == "__main__":
    test_deck = Deck()
    test_deck.shuffle()
    print(test_deck)
