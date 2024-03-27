from player import Player
import random

def generate_cards():
    '''Generates a deck of cards, 1 of each card value for each suit'''
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_values = ["A", 2, 3, 4, 5, 6,7, 8, 9, 10, "J", "Q", "K"]

    all_cards = []
    for suit in suits:
        for card in card_values:
            all_cards.append((suit, card))

    return all_cards

def deal_a_card(deck:list):
    '''Randomly picks a card from the deck, removes it so it can't be played twice, then returns that card'''
    card = random.choice(deck)
    deck.remove(card)

    return card

def calculate_hand_total(hand:list):
    '''Verifies each character value card is assigned an integer value'''
    total = 0
    value = 0

    # Goes through each card value to assign proper values to str data types
    for i in hand:
        if i[1] == "J" or i[1] == "Q" or i[1] == "K" :
            value = 10
        elif i[1] == "A":
            value = 11
        else:
            value = i[1]

        total += value

    # Checks to see if the player has an ace in their hand when they went over 21, if they do it'll switch it's value to 1 instead of 11
    if total > 21:
        for i in hand:
            if i[1] == "A":
                total -= 11
                total += 1
                if total < 21:
                    break

    return total

def game_lose(player:Player, bet:float):
    '''Removes money from player when they lose'''
    player.adjust_money(-bet)
    print(f"You lost ${-bet}")

def game_win(player:Player, bet:float, modifier:int=1):
    player.adjust_money(bet * modifier)
    print(f"You won ${bet * modifier}")

def game_tie(player:Player, bet:float):
    print(f"You tied, your bet of ${bet} was returned")

def play_game(player:Player):
    '''This method will be called in casinoMenu.py to start playing blackjack'''
    game_active = True
    while True:
        try:
            bet = float(input("Place your bet: "))
            if bet > 0:
                break
        except ValueError:
            print("Bet must be a valid number")

    deck = generate_cards()
    player_cards = []
    player_hand_value = 0
    dealer_cards = []
    dealer_hand_value = 0

    # Deals starting cards out
    player_cards.append(deal_a_card(deck))
    dealer_cards.append(deal_a_card(deck))
    player_cards.append(deal_a_card(deck))
    player_hand_value = calculate_hand_total(player_cards)
    dealer_hand_value = calculate_hand_total(dealer_cards)

    #Displays starting cards
    print("Player: ", player_cards)
    print(player_hand_value)
    print("Dealer: ", dealer_cards)
    print(dealer_hand_value)

    # Checks to see if the player hit blackjack
    if player_hand_value == 21:
        print("BLACK JACK")
        game_win(player, bet, 1.5)
        game_active = False

    #Player's turn to hit or stand
    while game_active:
        try:
            player_choice = int(input("1: Hit\n2:Stand"))

            if player_choice == 1:
                player_cards.append(deal_a_card(deck))
                print(player_cards)
                player_hand_value = calculate_hand_total(player_cards)
                print(player_hand_value)
                if player_hand_value > 21:
                    game_lose(player, bet)
                    game_active = False
            elif player_choice == 2:
                break
            else:
                print("Invalid input, please try again")
                print(player_cards)
                print(player_hand_value)
                continue
        except ValueError:
            print("Invalid input, please try again")

    #Dealer's turn to hit or stand
    while game_active:
        if dealer_hand_value < 17:
            dealer_cards.append(deal_a_card(deck))
            print(dealer_cards)
            dealer_hand_value = calculate_hand_total(dealer_cards)
            print(dealer_hand_value)
        elif dealer_hand_value > 21:
            game_win(player, bet)
            game_active = False
        else:
            break

    # Checks both hand values to determine the winner
    if game_active:
        if player_hand_value > dealer_hand_value and player_hand_value <= 21:
            game_win(player, bet)
        elif player_hand_value < dealer_hand_value :
            game_lose(player, bet)
        else:
            game_tie(player, bet)