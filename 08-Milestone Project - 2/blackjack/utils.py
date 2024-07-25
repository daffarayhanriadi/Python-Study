# function for taking bets
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips!, You have: {chips.total}")
            else:
                break


## function for taking bets (another way)
# def take_bet():
#     while True:
#         try:
#             player_chips.bet = int(input("How many chips would you like to bet? "))
#         except:
#             print("Sorry, please provide an integer")
#         else:
#             if player_chips.bet > player_chips.total:
#                 print(f"Sorry, you do not have enough chips!, You have: {player_chips.total}")
#             else:
#                 break


# function for taking hits
def hit(deck, hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# function prompting the Player to Hit or Stand
def hit_or_stand(deck, hand):
    
    # global playing  # to control an upcoming while loop

    while True:
        
        x = input("Hit or Stand? Enter h or s: ")

        if x[0].lower() == "h":
            hit(deck, hand)
            return True
        elif x[0].lower() == "s":
            print("Player Stands, Dealer's Turn")
            return False
        else:
            print("Sorry, i did not understand that, Please enter h or s only!")


# functions to display cards
def show_some(player, dealer):
    
    # Show only ONE of the dealer's cards
    print("\nDEALER'S HAND: ")
    print("First card hidden!")  # dealer.cards[0]
    print(dealer.cards[1])

    # Show all (2 cards) of the player's hand/cards
    print("\nPLAYER'S HAND: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    # Show all the dealer's cards
    print("\nDEALER'S HAND: ", *dealer.cards, sep="\n")

    # Calculate and display Dealer's value (J + K == 20)
    print(f"Value of DEALER'S HAND is: {dealer.value}")

    # Show all the player's cards
    print("\nPLAYER'S HAND: ", *player.cards, sep="\n")

    # Calculate and display Player's value (J + K == 20)
    print(f"Value of PLAYER'S HAND is: {player.value}")


# functions to handle end of game scenarios
def player_busts(player, dealer, chips):
    print("PLAYER BUSTS")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS!, DEALER BUSTS!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! PUSH")
