from player import Player
from games import blackJack, slotMachine, coinFlip

def main():
    player = Player("Jordan", 50.5)
    coinFlip.play_game(player)


if __name__ == "__main__":
    main()