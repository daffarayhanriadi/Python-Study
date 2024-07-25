from .constant import values
from .deck import Deck


class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # card passed in
        # from Deck.deal() -> single Card(suit, rank)

        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        # if total value > 21 and i still have an ace
        # than change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


if __name__ == "__main__":
    test_deck = Deck()
    test_deck.shuffle()

    # Player
    test_player = Hand()
    # Deal 1 card from the deck Card(suit, rank)
    pulled_card = test_deck.deal()
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)
