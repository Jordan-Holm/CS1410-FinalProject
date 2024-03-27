from player import Player
from Menu_Choices import menu_choices

def create_player():
    '''Creates a Player class object using user input for the name & a default amount of money at $100'''
    name = input("Enter your name: ")
        
    return Player(name, 100)

def main():
    player = create_player()

    menu_choices(player)

if __name__ == "__main__":
    main()