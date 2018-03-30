from enum import Enum


class Suit(Enum):
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.value

    @staticmethod
    def get_suit_from_value(value):
        return {
            0: Suit.Club,
            1: Suit.Diamond,
            2: Suit.Heart,
            3: Suit.Spade
        }.get(value, None)
