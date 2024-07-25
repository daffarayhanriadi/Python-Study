"""

Run with : python -m <package_name>.<module_name>

"""

from .constant import suits, ranks
from .card import Card

# Player Class
class Player:
    
    amount = 0
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []  # New player has no cards
        Player.amount += 1

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

if __name__ == "__main__":
    two_hearts = Card(suits[0], ranks[0])
    daffa = Player("Daffa")
    print(daffa)  # Player Daffa has 0 cards
    daffa.add_cards(two_hearts)
    print(daffa)  # Player Daffa has 1 cards
    daffa.add_cards([two_hearts, two_hearts, two_hearts])
    print(daffa)  # Player Daffa has 4 cards