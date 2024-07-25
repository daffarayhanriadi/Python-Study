"""

Run with : python -m <package_name>.<module_name>

"""

import random
from .constant import suits, ranks
from .card import Card

# Deck Class
class Deck:
    def __init__(self):
        # This only happens once upon creation of a new deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)  # This method doesn't return anything

    def deal_one(self):
        return self.all_cards.pop()  # Remove 1 Card

if __name__ == "__main__":
    mydeck = Deck()
    print(len(mydeck.all_cards))  # 52
    print(mydeck.all_cards[0])  # Two of Hearts
    mydeck.shuffle()
    print(mydeck.all_cards[0])  # Different after shuffle
    my_card = mydeck.deal_one()  # Remove 1 Card
    print(my_card)