class Card: # object
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def data(self):
        return self._rank, self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":    
    c = Card('6', 'Clubs')
    print(f"{type(c) = }")
    print(f"{c = }")  # repr(c)
    print(c)  # print(str(c))
    # print(c.get_rank())  # c.rank
    # print(c.get_suit())  # c.suit
    print(f"{c.rank = }")
    print(f"{c.suit = }")
    print(f"{c.data = }")

    x = str(c)  #  CardDeck.__str__(c)
