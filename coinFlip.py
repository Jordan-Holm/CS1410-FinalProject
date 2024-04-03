from player import Player
import random

class Coin():
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
        
    coin = Coin(random.randint(1,2), guess, bet)
    coin.game_results(player)