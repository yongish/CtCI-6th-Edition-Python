class Hand:
    def __init__(self):
        self.cards = []

    def score(self):
        score = 0
        for card in self.cards:
            score += card.value()
        return score

