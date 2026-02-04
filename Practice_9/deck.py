from random import shuffle

if __name__ != '__main__':
    from const import CARD_VALUES, RANKS, SUITS
# SUITS = ['♠', '♣', '♦', '♥']  # "\u2665", "\u2666", "\u2660", "\u2663"
# RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
#                'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:

    def __init__(self, suit, rank, points, picture=None):
        self.suit = suit
        self.rank = rank
        self.points = points
        self.picture = picture

    def __lt__(self, other):
        # !TODO: Implement comparision
        return RANKS.index(self.rank) < RANKS.index(other.rank)

    def __gt__(self, other):
        return RANKS.index(self.rank) > RANKS.index(other.rank)

    def __str__(self):
        return f"|{self.suit}{self.rank}|"


class Hand:

    def __init__(self):
        self.cards = []
        self.reset()

    @property
    def points(self):
        return self.__points

    def _recalc_points(self):
        score = 0
        for card in self.cards:
            score += card.points
            if card.rank == 'A' and score > 21:
                score -= 10
        self.__points = score

    def _sort(self):
        self.cards.sort()

    def add_card(self, card):
        self.cards.append(card)
        self._sort()
        self._recalc_points()

    def reset(self):
        self.__points = 0
        self.cards.clear()

    def __str__(self):
        return "".join(map(str, self.cards))


class Deck:
    def __init__(self, deck_count=1):

        self.__deck = [Card(suit, rank, value) for suit in SUITS for rank, value in CARD_VALUES.items()] * deck_count

        self.game_deck = []
        self.shuffle()

    def shuffle(self):
        self.game_deck[:] = self.__deck[:]
        shuffle(self.game_deck)

    # def __iter__(self):
    #     shuffle(self.__deck)
    #     return iter(self.__deck)

    # def __next__(self):
    #     return

    def get_card(self):
        if len(self.game_deck) <= 5:
            self.shuffle()
        return self.game_deck.pop()

    def __str__(self):
        return " | ".join(map(str, self.game_deck))

    def __len__(self):
        return len(self.game_deck)


if __name__ == '__main__':
    from const import CARD_VALUES, RANKS, SUITS

    deck = Deck(deck_count=3)

    print(deck)

    hand1 = Hand()
    hand1.add_card(deck.get_card())
    hand1.add_card(deck.get_card())

    print("hand 1:", hand1)

    hand2 = Hand()
    for _ in range(4):
        hand2.add_card(deck.get_card())

    print("hand 2:", hand2, " Points: ", hand2.points)
