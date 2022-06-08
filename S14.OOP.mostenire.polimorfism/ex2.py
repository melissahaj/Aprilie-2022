from pydoc import describe


class Card:
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol
    def __str__(self):
        return self.number + self.symbol
    def __repr__(self):
        return self.__str__()
class Deck:
    def __init__(self):
        self.__AVAILABLE_SYMBOLS = ("♠", "♥", "♦", "♣")
        self.__cards = []
        self.__generate_cards()
    def get_cards(self, number):
        r_cards = []
        for i in range(number):