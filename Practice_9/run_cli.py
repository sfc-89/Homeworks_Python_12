import game as api


if __name__ == '__main__':
    action = input("Welcome to the BlackJack Redux Game!\n1 - to play, 2 - to exit: ")
    while action == "1":
        game = api.CLI_Game()
        result = game.play()
        if result["winner"] == "draw":
            action = input(f"Draw! \nPress 1 to play new round, 2 to exit: ")
        else:
            action = input(f"Winners is {result['winner']}! \nPress 1 to play new round, 2 to exit: ")

# card

# hand
#   - cards = []
#   - prop ->  points
#   - m -> add_card
#   - m -> str

# deck
#   - deck
#   - m -> shuffle
#   - m ->  get_card()

# players
#  abs_player
#
#   bots ???
#   dealer

#   player