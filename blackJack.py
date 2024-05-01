from player import Player
import random
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.clock import Clock

class BlackJackScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.game_name = "Black Jack"
        self.hit_button = None
        self.stand_button =  None

        self.player_cards = []
        self.player_hand_value = 0
        self.dealer_cards = []
        self.dealer_hand_value = 0
        self.deck = []

    def on_enter(self, *args):
        super().on_enter(*args)

        self.player_cards = []
        self.player_hand_value = 0
        self.dealer_cards = []
        self.dealer_hand_value = 0
        self.deck = []
        self.deck = self.generate_cards()

        self.player_cards.append(self.deal_a_card(self.deck))
        self.dealer_cards.append(self.deal_a_card(self.deck))
        self.player_cards.append(self.deal_a_card(self.deck))
        self.player_hand_value = self.calculate_hand_total(self.player_cards)
        self.dealer_hand_value = self.calculate_hand_total(self.dealer_cards)

        player_table = self.ids.player_hand
        player_table.clear_widgets()
        player_card_label = Label(text=", ".join([f"{suit} {value}" for suit, value in self.player_cards]), font_size=12)
        player_handvalue_label = Label(text=str(self.player_hand_value))
        player_table.add_widget(player_card_label)
        player_table.add_widget(player_handvalue_label)

        dealer_table = self.ids.dealer_hand
        dealer_table.clear_widgets()
        dealer_card_label = Label(text=", ".join([f"{suit} {value}" for suit, value in self.dealer_cards]), font_size=12)
        dealer_handvalue_label = Label(text=str(self.dealer_hand_value))
        dealer_table.add_widget(dealer_card_label)
        dealer_table.add_widget(dealer_handvalue_label)

        button_table = self.ids.buttontable
        button_table.clear_widgets()
        self.hit_button = Button(text='Hit')
        self.hit_button.bind(on_press=self.on_player_hit)
        button_table.add_widget(self.hit_button)
        self.stand_button = Button(text="Stand")
        self.stand_button.bind(on_press=self.on_player_stand)
        button_table.add_widget(self.stand_button)

        if self.player_hand_value == 21:
            self.go_to_outcomes('blackjack')

    def on_player_hit(self, instance):
        self.player_cards.append(self.deal_a_card(self.deck))
        self.player_hand_value = self.calculate_hand_total(self.player_cards)

        if self.player_hand_value > 21:
            self.go_to_outcomes('lost')

        player_table = self.ids.player_hand
        player_table.clear_widgets()
        player_card_label = Label(text=", ".join([f"{suit} {value}" for suit, value in self.player_cards]), font_size=12)
        player_handvalue_label = Label(text=str(self.player_hand_value))
        player_table.add_widget(player_card_label)
        player_table.add_widget(player_handvalue_label)
    
    def on_player_stand(self, instance):
        print("Stand")
        if self.hit_button:
            self.hit_button.disabled = True
            self.stand_button.disabled = True

        Clock.schedule_interval(self.dealers_turn, 1.5)

    def dealers_turn(self, dt):
        self.dealer_cards.append(self.deal_a_card(self.deck))
        self.dealer_hand_value = self.calculate_hand_total(self.dealer_cards)

        dealer_table = self.ids.dealer_hand
        dealer_table.clear_widgets()
        dealer_card_label = Label(text=", ".join([f"{suit} {value}" for suit, value in self.dealer_cards]), font_size=12)
        dealer_handvalue_label = Label(text=str(self.dealer_hand_value))
        dealer_table.add_widget(dealer_card_label)
        dealer_table.add_widget(dealer_handvalue_label)

        print(self.dealer_hand_value)
        if self.dealer_hand_value > 21:
            Clock.unschedule(self.dealers_turn)
            self.go_to_outcomes('win')
        elif self.dealer_hand_value >= 17:
            Clock.unschedule(self.dealers_turn)
            self.determine_winner()
     

    def generate_cards(self):
        '''Generates a deck of cards, 1 of each card value for each suit'''
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        card_values = ["A", 2, 3, 4, 5, 6,7, 8, 9, 10, "J", "Q", "K"]

        all_cards = []
        for suit in suits:
            for card in card_values:
                all_cards.append((suit, card))

        return all_cards

    def deal_a_card(self, deck:list):
        '''Randomly picks a card from the deck, removes it so it can't be played twice, then returns that card'''
        card = random.choice(deck)
        deck.remove(card)

        return card

    def calculate_hand_total(self, hand:list):
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
    
    def determine_winner(self):
        if self.player_hand_value > self.dealer_hand_value:
            self.go_to_outcomes('win')
        elif self.player_hand_value < self.dealer_hand_value:
            self.go_to_outcomes('lost')
        else:
            self.go_to_outcomes('tie')
            
    def go_to_outcomes(self, outcome):
        screen_manager = App.get_running_app().root
        screen_manager.current = "Outcomes"
        screen_manager.get_screen("Outcomes").game_outcome = outcome

    # def play_game(self, player:Player):
    #     '''This method will be called in casinoMenu.py to start playing blackjack'''
    #     player.set_cur_bet()
    #     bet = player.get_cur_bet()
        
    #     game_active = True

    #     deck = self.generate_cards()
    #     player_cards = []
    #     player_hand_value = 0
    #     dealer_cards = []
    #     dealer_hand_value = 0

    #     # Deals starting cards out
    #     player_cards.append(self.deal_a_card(deck))
    #     dealer_cards.append(self.deal_a_card(deck))
    #     player_cards.append(self.deal_a_card(deck))
    #     player_hand_value = self.calculate_hand_total(player_cards)
    #     dealer_hand_value = self.calculate_hand_total(dealer_cards)

    #     #Displays starting cards
    #     print("Player: ", player_cards)
    #     print(player_hand_value)
    #     print("Dealer: ", dealer_cards)
    #     print(dealer_hand_value)

    #     # Checks to see if the player hit blackjack
    #     if player_hand_value == 21:
    #         print("BLACK JACK")
    #         player.player_win(bet, 1.5)
    #         game_active = False

    #     #Player's turn to hit or stand
    #     while game_active:
    #         try:
    #             player_choice = int(input("1: Hit\n2:Stand"))

    #             if player_choice == 1:
    #                 player_cards.append(self.deal_a_card(deck))
    #                 print(player_cards)
    #                 player_hand_value = self.calculate_hand_total(player_cards)
    #                 print(player_hand_value)
    #                 if player_hand_value > 21:
    #                     player.player_lose(bet)
    #                     game_active = False
    #             elif player_choice == 2:
    #                 break
    #             else:
    #                 print("Invalid input, please try again")
    #                 print(player_cards)
    #                 print(player_hand_value)
    #                 continue
    #         except ValueError:
    #             print("Invalid input, please try again")

    #     #Dealer's turn to hit or stand
    #     while game_active:
    #         if dealer_hand_value < 17:
    #             dealer_cards.append(self.deal_a_card(deck))
    #             print(dealer_cards)
    #             dealer_hand_value = self.calculate_hand_total(dealer_cards)
    #             print(dealer_hand_value)
    #         elif dealer_hand_value > 21:
    #             player.player_win(bet)
    #             game_active = False
    #         else:
    #             break

    #     # Checks both hand values to determine the winner
    #     if game_active:
    #         if player_hand_value > dealer_hand_value and player_hand_value <= 21:
    #             player.player_win(bet)
    #         elif player_hand_value < dealer_hand_value :
    #             player.player_lose(bet)
    #         else:
    #             player.player_tie(bet)