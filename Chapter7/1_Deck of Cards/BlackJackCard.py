import Card


class BlackJackCard(Card):
    def __init__(self, value, suit):
        super(BlackJackCard, self).__init__(value, suit)

    def value(self):
        if self.is_ace():
            return 1
        elif 11 <= self.value <= 13:
            return 10
        else:
            return self.value

    def min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.value

    def max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.value

    def is_ace(self):
        return self.value == 1

    def is_face_card(self):
        return 11 <= self.value <= 13
