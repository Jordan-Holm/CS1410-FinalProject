from kivy.uix.screenmanager import Screen
from kivy.app import App
from player import Player

class PlaceBetScreen(Screen):
    def place_bet(self, player: Player, game: str):
        player.set_cur_bet(self.ids.bet_input.float)

        App.get_running_app().root.current = game