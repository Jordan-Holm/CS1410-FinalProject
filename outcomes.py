from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.graphics import Color, Rectangle

class OutcomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.game_outcome = ''

    def on_enter(self, *args):
        super().on_enter(*args)
        player_instance = App.get_running_app().root.player_instance
        self.player_instance = player_instance
        
        print(self.game_outcome)

        header = self.ids.header
        header.clear_widgets()
        bet_display = self.ids.bet_outcome
        bet_display.clear_widgets()

        match self.game_outcome:
            case "lost":
                self.player_instance.adjust_money(-self.player_instance.cur_bet) 
                lost_label = Label(text="You Lost", font_size=50)
                header.add_widget(lost_label)
                bet_label = Label(text=f"-${self.player_instance.cur_bet}",color=(1, 0, 0, 1))
                with bet_label.canvas.before:
                    Color(1, 1, 1, 1)
                    self.rect = Rectangle(size=bet_label.size, pos=bet_label.pos)
                bet_label.bind(size=self._update_rect, pos=self._update_rect)
                bet_display.add_widget(bet_label)
            case "win":
                self.player_instance.adjust_money(self.player_instance.cur_bet)
                lost_label = Label(text="You Win", font_size=50)
                header.add_widget(lost_label)
                bet_label = Label(text=f"${self.player_instance.cur_bet}",color=(0, 1, 0, 1))
                with bet_label.canvas.before:
                    Color(1, 1, 1, 1)
                    self.rect = Rectangle(size=bet_label.size, pos=bet_label.pos)
                bet_label.bind(size=self._update_rect, pos=self._update_rect)
                bet_display.add_widget(bet_label)
            case "blackjack":
                self.player_instance.adjust_money(self.player_instance.cur_bet*1.5)
                lost_label = Label(text="Black Jack", font_size=50)
                header.add_widget(lost_label)
                bet_label = Label(text=f"${self.player_instance.cur_bet*1.5}",color=(0, 1, 0, 1))
                with bet_label.canvas.before:
                    Color(1, 1, 1, 1)
                    self.rect = Rectangle(size=bet_label.size, pos=bet_label.pos)
                bet_label.bind(size=self._update_rect, pos=self._update_rect)
                bet_display.add_widget(bet_label)
            case "tie":
                lost_label = Label(text="You Tied", font_size=50)
                header.add_widget(lost_label)
                bet_label = Label(text=f"Your bet of ${self.player_instance.cur_bet} was returned",color=(0, 0, 0, 1))
                with bet_label.canvas.before:
                    Color(1, 1, 1, 1)
                    self.rect = Rectangle(size=bet_label.size, pos=bet_label.pos)
                bet_label.bind(size=self._update_rect, pos=self._update_rect)
                bet_display.add_widget(bet_label)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_menu(self):
        screen_manager = App.get_running_app().root
        screen_manager.current = "MainMenu"