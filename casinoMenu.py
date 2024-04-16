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

class MainMenuScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)
        game_list = [BlackJackScreen(), SlotScreen()]
        print(game_list)
        game_table = self.ids.gametable
        game_table.clear_widgets()

        for game in game_list:
            game_button = Button(text=game.game_name, font_size = 30)
            game_table.add_widget(game_button)

class SystemManager(ScreenManager):
    ...

class CasinoGame(Widget):
    pass

class CasinoApp(App):
    def build(self):
        casino = SystemManager(transition=NoTransition())
        casino.current = "CreatePlayer"

        return casino

if __name__ == "__main__":
    CasinoApp().run()