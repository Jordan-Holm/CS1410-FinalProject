from player import Player
import random

def generate_slot_nums():
    num1 = random.randint(1,3)
    num2 = random.randint(1,3)
    num3 = random.randint(1,3)

    return num1, num2, num3

def check_slot_nums(player:Player, bet:float, num1:int, num2:int, num3:int):
    if num1 == num2:
        if num2 == num3:
            if num1 == 1: #if the player rolls three 1s 2x multiplier
                # game_win(player, bet)
                player.player_win(bet, 2)
            elif num1 == 2: #if the player rolls three 2s 4x multiplier
                # game_win(player, bet, 4)
                player.player_win(bet, 4)
            elif num1 == 3: #if the player rolls three 3s 10x multiplier
                print("JACKPOT!")
                # game_win(player, bet, 10)
                player.player_win(bet, 10)
        else:
            # game_tie(player, bet)
            player.player_tie(bet)
    elif num2 == num3:
        # game_tie(player, bet)
        player.player_tie(bet)
    else:
        # game_lose(player, bet)
        player.player_lose(bet)

def play_game(player:Player):
    player.set_cur_bet()
    bet = player.get_cur_bet()

    num1, num2, num3 = generate_slot_nums()
    print(f"{num1}-{num2}-{num3}")
    check_slot_nums(player, bet, num1, num2, num3)