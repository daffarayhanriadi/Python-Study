"""

Run with : 

python -m <package_name>.<module_name> # if without __main__.py file

or 

python -m <package_name> # if with __main__.py file
 
"""
def main():
    from .player import Player
    from .deck import Deck

    # War Game Logic
    player_one = Player("One")
    player_two = Player("Two")

    # Setup New Game
    new_deck = Deck()
    new_deck.shuffle()

    # Split the Deck between players
    print(len(new_deck.all_cards) // Player.amount)  # 26
    for _ in range(len(new_deck.all_cards) // Player.amount):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    print(len(new_deck.all_cards))  # Should be 0
    print(player_one.all_cards)  # 26
    print(player_two.all_cards)  # 26

    # Play the Game
    game_on = True
    round_num = 0

    while game_on:
        round_num += 1
        print(f"Round {round_num}")

        # Check to see if a player is out of cards:
        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break
        elif len(player_two.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break

        # Otherwise, the game is still on!
        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:

                # Player One gets the cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                # No longer at "war", time for next round
                at_war = False

            # Player Two has higher card
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # Player One gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                # No longer at "war", time for next round
                at_war = False

            # Player One and Player Two DRAW!
            else:
                print("WAR!")

                # Check to see if a player is out of cards
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins!, Player One Loses!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins!, Player Two Loses!")
                    game_on = False
                    break
                else:  # Otherwise, we're still at war, so we'll add the next cards
                    for _ in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

    print(len(player_one.all_cards))
    print(len(player_two.all_cards))
    print(player_one_cards[-1])
    print(player_two_cards[-1])
    
if __name__ == "__main__":
    main()