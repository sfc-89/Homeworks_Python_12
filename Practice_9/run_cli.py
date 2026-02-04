import game as api

if __name__ == '__main__':
    name = input("Welcome to the BlackJack Redux Game!\nWhat is your name?:")
    action = input("\n1 - to play, 2 - to exit: ")
    while action == "1":
        game = api.CLI_Game(name)
        result = game.play()
        if result["winner"] == "draw":
            action = input(f"\nDraw! \n\nPress 1 to play new round, 2 to exit: ")
        else:
            action = input(f"\nWinner is {result['winner']}! \n\nPress 1 to play new round, 2 to exit: ")
