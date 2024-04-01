from player import Player
import random

class Coin():
    def __init__(self, coin, guess, bet):
        self.coin = coin
        self.guess = guess
        self.bet = bet
        
    def cointoss(self):
        def sign():
            if self.coin == 1:
                self.coin = "Heads"
            elif self.coin == 2:
                self.coin = "Tails"
        def game_lose(player:Player, bet:float):
            player.adjust_money(-bet)
            print(f"It was {self.coin}!You lost ${-bet}.")

        def game_win(player:Player, bet:float):
            player.adjust_money(bet)
            print(f"It was {self.coin}! You won ${bet}!")
            
        def game_results():
            if self.guess == self.coin:
                sign()
                game_win()
            
            elif self.guess != self.coin:
                sign()
                game_lose()
            
def main():
    player.set_cur_bet()
    bet = player.get_cur_bet()
    
    guess = int(input('1.Heads\n2.Tails\nHeads or Tails? Type a number. ' ))
    try:
        guess == 1 or 2 
    except ValueError as e:
        print(e)
        
    coin = Coin(random.randint(1,2), guess, bet)
    coin.cointoss()
      
    
    
if __name__ == "__main__":
    main()
        
            
        