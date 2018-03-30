from __future__ import print_function


class Deck:
    def __init__(self):
        self.dealt_index = 0
        self.cards = None

    def remaining_cards(self):
        return len(self.cards) - self.dealt_index

    def deal_hand(self, number):
        if self.remaining_cards() < number:
            return None

        hand = []
        for i in range(number):
            card = self.deal_card()
            if card is not None:
                hand.append(card)

        return hand

    def deal_card(self):
        if self.remaining_cards() == 0:
            return None

        card = self.cards.get(self.dealt_index)
        card.available = False
        self.dealt_index += 1

        return card

    def print(self):
        for card in self.cards:
            print(card)
