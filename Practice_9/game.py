if __name__ != '__main__':
    from deck import Deck
    from players import Player, Dealer


class CLI_Game:

    def __init__(self):
        self.deck = Deck(1)

    def init(self):
        self.player = Player(name="My Name")
        self.dealer = Dealer()

    def check_score(self):
        # TODO
        if self.player.full_points == self.dealer.full_points and self.player.full_points < 21:
            return {"winner": "draw"}
        elif self.dealer.full_points < self.player.full_points <= 21 and self.dealer.full_points < 21:
            return {"winner": self.player.name}
        elif self.dealer.full_points > 21 >= self.player.full_points:
            return {"winner": self.player.name}
        else:
            return {"winner": self.dealer.name}

    def is_going_on(self, action):
        if not action:
            return False
        return True

    def start(self):
        self.deck.shuffle()
        self.player.reset()
        self.dealer.reset()

        self.dealer.take_two_cards([self.deck.get_card(), self.deck.get_card()])
        self.player.take_two_cards([self.deck.get_card(), self.deck.get_card()])

        print(self.dealer)
        print(self.player)

        self.check_score()

    def play_round(self, action):
        if action:
            self.player.take_card(self.deck.get_card())
            print(self.player)
        else:
            while self.dealer.full_points <= self.dealer.max_points:
                self.dealer.take_card(self.deck.get_card())
                print(self.dealer)

    def play(self):
        self.init()
        self.start()
        is_going_on = True

        while is_going_on:
            action = self.player.ask_card()
            self.play_round(action)
            is_going_on = self.is_going_on(action)
        return self.check_score()


if __name__ == '__main__':
    from deck import Deck
    from players import Player, Dealer

    game = CLI_Game()
    game.play()
