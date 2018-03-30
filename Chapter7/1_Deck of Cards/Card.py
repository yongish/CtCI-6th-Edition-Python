from __future__ import print_function
from abc import ABCMeta, abstractmethod
import Suit


class Card:
    __metaclass__ = ABCMeta

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.available = True

    @abstractmethod
    def value(self):
        return self.value

    def print(self):
        face_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', '10']
        print(face_values[self.value - 1], end='')
        if self.suit == Suit.Club:
            print('c', end='')
        elif self.suit == Suit.Diamond:
            print('d', end='')
        elif self.suit == Suit.Heart:
            print('h', end='')
        elif self.suit == Suit.Spade:
            print('s', end='')

        print(' ')




