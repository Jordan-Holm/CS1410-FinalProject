from player import Player
import blackJack, slotMachine, coinFlip

def menu_choices(player:Player):

    # Checks if the player still has money to even play
    while True:
        if player.money > 0:
            print("1: BlackJack\n2: Slot Machines\n3: Coin Flip\n4: View Money\n5: Quit")
            try:
                player_input = int(input("Make a choice: "))
                if player_input < 1 or player_input > 5:
                    print("Invalid input, please try again")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input, please try again")
        else:
            print("You're out of cash! Comeback again :)")
            quit()

    match player_input:
        case 1:
            blackJack.play_game(player)
            menu_choices(player)
        case 2:
            slotMachine.play_game(player)
            menu_choices(player)
        case 3:
            pass
        case 4:
            player.show_money()
            menu_choices(player)
        case 5:
            quit()