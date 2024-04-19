from kivy.uix.screenmanager import Screen
from player import Player

class PlaceBetScreen(Screen):
    def place_bet(self, player: Player):
        player.set_cur_bet(self.ids.bet_input.float)