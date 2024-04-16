from player import Player
import random
from kivy.uix.screenmanager import Screen
class SlotScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.game_name = "Slot Machine"

    def generate_slot_nums():
        num1 = random.randint(1,3)
        num2 = random.randint(1,3)
        num3 = random.randint(1,3)

        return num1, num2, num3

    def check_slot_nums(player:Player, bet:float, num1:int, num2:int, num3:int):
        if num1 == num2:
            if num2 == num3:
                if num1 == 1: #if the player rolls three 1s 2x multiplier
                    player.player_win(bet, 2)
                elif num1 == 2: #if the player rolls three 2s 4x multiplier
                    player.player_win(bet, 4)
                elif num1 == 3: #if the player rolls three 3s 10x multiplier
                    print("JACKPOT!")
                    player.player_win(bet, 10)
            else:
                player.player_tie(bet)
        elif num2 == num3:
            player.player_tie(bet)
        else:
            player.player_lose(bet)

    def play_game(self, player:Player):
        player.set_cur_bet()
        bet = player.get_cur_bet()

        num1, num2, num3 = self.generate_slot_nums()
        print(f"{num1}-{num2}-{num3}")
        self.check_slot_nums(player, bet, num1, num2, num3)