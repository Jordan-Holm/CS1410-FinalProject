from player import Player
import blackJack

def create_player():
    '''Creates a Player class object using user input for the name & a default amount of money at $100'''
    name = input("Enter your name: ")
        
    return Player(name, 100)

def menu_choices(player:Player):
    print("1: BlackJack\n2: Slot Machines\n3: Coin Flip\n4: View Money\n5: Quit")

    player_input = input("Make a choice: ")

    match player_input:
        case "1":
            blackJack.play_game(player)
        case "2":
            pass
        case "3":
            pass
        case "4":
            player.show_money()
            menu_choices(player)
        case "5":
            quit()

def main():
    player = create_player()

    menu_choices(player)

if __name__ == "__main__":
    main()