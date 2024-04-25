from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App

class Player(Screen):
    def __init__(self, **kwargs):
        self.name = ""
        self.money: float = 100
        self.cur_bet: float
        super().__init__(**kwargs)
        Window.bind(on_key_down = self._keydown)

    def adjust_money(self, amount_to_adjust:float):
        '''Adjust class objects money variable by the given "amount_to_adjust" variable when called'''
        self.money += amount_to_adjust

    def show_money(self):
        '''Displays the class object current money amount. Formated to 2 decimal places'''
        return f"${self.money:.2f}"

    def get_cur_bet(self):
        return self.cur_bet

    def set_cur_bet(self, bet):
        self.cur_bet = bet

    def _keydown(self, *args):
        print(f"Key down {args[3]}")
        # sleep(0.0001)
        name = self.ids.name_input.text
        if name == "":
            print("Need information")
        else:
            create_player = self.ids.create_player
            create_player.disabled = False

    def on_click(self):
        player_instance = App.get_running_app().root.player_instance
        player_instance.name = self.ids.name_input.text
        App.get_running_app().root.current = "MainMenu"

    def player_win(self, bet, modifier=1):
        '''Adds money to player's money based on modifier'''
        if modifier > 1:
            print(f"{modifier}x modifier!\nYou won ${bet * modifier}")
        else:
            print(f"You won ${bet * modifier}")
        self.adjust_money(self.get_cur_bet())

    def player_lose(self, bet):
        '''Removes money from player when they lose'''
        print(f"You lost ${-bet}")
        self.adjust_money(-self.get_cur_bet())

    def player_tie(self, bet):
        '''Doesn't add/subtract from player's money, just returns current bet'''
        print(f"your bet of ${bet} was returned")

    def __str__(self):
        return f"{self.name}: {self.show_money()}"

    def __repr__(self):
        return f"Player({self.name}, {self.money})\nPlayer.adjust_money(-10)\nPlayer.show_money()\nPlayer.set_cur_bet()\nPlayer.get_cur_bet()"