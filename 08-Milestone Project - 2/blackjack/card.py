from .constant import suits, ranks


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    two_hearts = Card(suits[0], ranks[0])
    print(two_hearts.suit)
    print(two_hearts.rank)
    print(two_hearts)
