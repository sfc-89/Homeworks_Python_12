
if __name__ != '__main__':
    from deck import Deck
    from players import Player, Dealer


class CLI_Game:

    def __init__(self):
        self.deck = Deck(3)

    def init(self):
        self.player = Player(name="My Name")
        self.dealer = Dealer()

    def is_going_on(self):
        # !TODO
        return True

    def _check_ctate(self):
        pass

    def start(self):
        self.deck.shuffle()
        self.player.reset()
        self.dealer.reset()

        self.dealer.take_two_cards([self.deck.get_card(), self.deck.get_card()])
        self.player.take_two_cards([self.deck.get_card(), self.deck.get_card()])

        print(self.dealer)
        print(self.player)

        self._check_ctate()

    def play_round(self):
        # !TODO
        pass


    def play(self):

        self.init()

        while self.is_going_on():
            #TODO: delete recursion
            self.start()
            self.play_round()
            # TODO: self.show_results()


if __name__ == '__main__':
    from deck import Deck
    from players import Player, Dealer

    game = CLI_Game()
    game.play()


