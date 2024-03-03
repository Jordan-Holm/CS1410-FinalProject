class Player():
    def __init__(self, name:str, money:float):
        self.name = name
        self.money = float(money)

    def adjust_money(self, amount_to_adjust:float):
        '''Adjust class objects money variable by the given "amount_to_adjust" variable when called'''
        self.money += amount_to_adjust

    def show_money(self):
        '''Displays the class object current money amount. Formated to 2 decimal places'''
        print(f"${self.money:.2f}")

    def __str__(self):
        return f"{self.name}: {self.show_money()}"

    def __repr__(self):
        return f"Player({self.name}, {self.money})\nPlayer.adjust_money(-10)\nPlayer.show_money()"