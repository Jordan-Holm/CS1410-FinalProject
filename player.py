class Player():
    def __init__(self, name:str, money:float):
        self.name = name
        self.money = float(money)
        self.cur_bet: float

    def adjust_money(self, amount_to_adjust:float):
        '''Adjust class objects money variable by the given "amount_to_adjust" variable when called'''
        self.money += amount_to_adjust

    def show_money(self):
        '''Displays the class object current money amount. Formated to 2 decimal places'''
        print(f"${self.money:.2f}")

    def get_cur_bet(self):
        return self.cur_bet

    def set_cur_bet(self):
        while True:
            try:
                bet = float(input("Place your bet: "))
                if bet > 0 and bet <= self.money:
                    self.cur_bet = bet
                    break
            except ValueError:
                print("Bet must be a valid number")

    def player_win(self, bet, modifier=1):
        '''Adds money to player's money based on modifier'''
        if modifier > 1:
            print(f"{modifier}x modifier!\nYou won ${bet * modifier}")
        else:
            print(f"You won ${bet * modifier}")
        self.adjust_money(self.get_cur_bet())

    def player_lose(self, bet):
        '''Removes money from player when they lose'''
        print(f"You lost ${-bet}")
        self.adjust_money(-self.get_cur_bet())

    def player_tie(self, bet):
        '''Doesn't add/subtract from player's money, just returns current bet'''
        print(f"your bet of ${bet} was returned")

    def __str__(self):
        return f"{self.name}: {self.show_money()}"

    def __repr__(self):
        return f"Player({self.name}, {self.money})\nPlayer.adjust_money(-10)\nPlayer.show_money()\nPlayer.set_cur_bet()\nPlayer.get_cur_bet()"