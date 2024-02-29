from player import Player
from games import blackJack, slotMachine, coinFlip

def main():
    player = create_player()

def create_player():
    '''Creates a Player class object using user input for the name & a default amount of money at $100'''
    name = input("Enter your name: ")
        
    return Player(name, 100)

if __name__ == "__main__":
    main()