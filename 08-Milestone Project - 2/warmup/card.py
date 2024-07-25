"""

Run with : python -m <package_name>.<module_name>

"""

from .constant import suits, ranks, values

# Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

if __name__ == "__main__":
    two_hearts = Card(suits[0], ranks[0])
    print(two_hearts)  # Two of Hearts
    print(two_hearts.suit)  # Hearts
    print(two_hearts.rank)  # Two
    print(two_hearts.value) # 2
    print(values[two_hearts.rank])  # 2