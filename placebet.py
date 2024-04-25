from kivy.uix.screenmanager import Screen
from kivy.app import App
from player import Player

class PlaceBetScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)

        player_instance = App.get_running_app().root.player_instance
        self.player_instance = player_instance
        selected_game = self.selected_game
        print(selected_game)


    def place_bet(self):
        bet_input_text = self.ids.bet_input.text
        bet_amount = float(bet_input_text)

        self.player_instance.set_cur_bet(bet_amount)
        print(self.player_instance.cur_bet)

        App.get_running_app().root.current = self.selected_game