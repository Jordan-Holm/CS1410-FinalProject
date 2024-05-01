from player import Player
import random
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
import random



class CoinFlipScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.game_name = "Coin Flip"
        self.button_heads = None
        self.button_tails = None
        self.button_flip = None

        self.guess = 0
        

    def on_enter(self, *args):
        super().on_enter(*args)

        button_tablet = self.ids.button_tablet
        button_tablet.clear_widgets()
        self.button_heads = Button(text="HEADS", font_size = 64)
        self.button_heads.bind(on_press=self.heads)
        button_tablet.add_widget(self.button_heads)
        self.button_tails = Button(text="TAILS", font_size = 64)
        self.button_tails.bind(on_press=self.tails)
        button_tablet.add_widget(self.button_tails)

    def rand(self):
        new_number = random.randint(1,2)
        return new_number
    
    def heads(self, instance):
        self.guess = 1
        self.flip(self.rand())

    def tails(self, instance):
        self.guess = 2
        self.flip(self.rand())

    def flip(self, number):
        if self.guess == number:
            self.go_to_outcomes('win')
        elif self.guess != number:
            self.go_to_outcomes('lost')
            
    def go_to_outcomes(self, outcome):
        screen_manager = App.get_running_app().root
        screen_manager.current = "Outcomes"
        screen_manager.get_screen("Outcomes").game_outcome = outcome
    

        
        
        

"""
class CoinFlipScreen():
    def __init__(self, coin, guess, bet):
        self.coin = coin
        self.guess = guess
        self.bet = bet
        
    def sign(self):
        if self.coin == 1:
            self.coin = "Heads"
        elif self.coin == 2:
            self.coin = "Tails"

        if self.guess == 1:
            self.guess = "Heads"
        elif self.guess == 2:
            self.guess = "Tails"
        
    def game_results(self, player: Player):
        self.sign()

        print(f"your guess: {self.guess}")
        print(f"Coin Result: {self.coin}")

        if self.guess == self.coin:
            player.player_win(self.bet)
        
        elif self.guess != self.coin:
            player.player_lose(self.bet)
            
def play_game(player: Player):
    player.set_cur_bet()
    bet = player.get_cur_bet()
    
    while True:
        try:
            guess = int(input('1.Heads\n2.Tails\nHeads or Tails? Type a number. ' ))
            if guess == 1 or guess == 2:
                break
        except ValueError:
            print("Invalid option")
        
    coin = CoinFlipScreen(random.randint(1,2), guess, bet)
    coin.game_results(player)
"""