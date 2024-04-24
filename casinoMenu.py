from player import Player
from placebet import PlaceBetScreen
from slotMachine import SlotScreen
from blackJack import BlackJackScreen
from coinFlip import CoinFlipScreen
from Menu_Choices import menu_choices
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.button import Button

player = {}

class MainMenuScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)

        # Get the Player instance
        player_instance = App.get_running_app().root.player_instance

        # Update the money_label text to display the player's money
        money_label = self.ids.moneylabel
        money_label.text = player_instance.__str__()

        game_list = [BlackJackScreen(), SlotScreen()]
        game_table = self.ids.gametable
        game_table.clear_widgets()

        for game in game_list:
            game_button = Button(text=game.game_name, font_size=30)
            game_button.id = game.game_name
            game_table.add_widget(game_button)

class SystemManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_instance = Player()

class CasinoGame(Widget):
    pass

class CasinoApp(App):
    def build(self):
        casino = SystemManager()
        casino.current = "Player"

        return casino

if __name__ == "__main__":
    CasinoApp().run()