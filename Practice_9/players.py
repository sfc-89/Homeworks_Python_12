from deck import Hand


class AbstractPlayer:
    def __init__(self, name='Player'):
        self.name = name
        self.hand = Hand()
        self.full_points = 0

    # @property
    # def cards(self):
    #     return self.hand.cards

    def ask_card(self):
        raise NotImplementedError("Method should be implemented")

    def take_card(self, card):
        self.hand.add_card(card)
        self.full_points = self.hand.points

    def __str__(self):
        return f"{self.name}   {str(self.hand)}  {self.full_points} "

    def reset(self):
        self.full_points = 0
        self.hand.reset()


class Player(AbstractPlayer):
    def __init__(self, name='Player'):
        super().__init__(name=name)

    def ask_card(self):
        if self.playing:
            choice = input("Do you want to get a new card?(y/n): ")
            return True if choice=='y' else False

    def take_card(self, card):
        super().take_card(card)
        print(self.hand)

    def take_two_cards(self, cards):
        super().take_card(cards[0])
        super().take_card(cards[1])
        print(self.hand)


class Dealer(AbstractPlayer):
    # TODO: Modify dealer logic
    max_points = 17

    def __init__(self, name="Dealer"):
        super().__init__(name=name)

    def ask_card(self):
        return True if self.full_points < self.max_points else False

    def take_two_cards(self, cards):
        super().take_card(cards[0])
        super().take_card(cards[1])
        print(self.hand)

#TODO: add tests