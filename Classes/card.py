


class Card:
    suit: str
    level: str
    value: int
    picture: str

    suits = ['diamonds', 'hearts', 'clubs', 'spades']
    levels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit: str, level: str):
        self.suit = suit
        self.level = level
        if level.isdigit():
            self.value = int(level)
        elif level == 'A':
            self.value = 11
        else:
            self.value = 10

    def info(self) -> str:
        return f'{self.suit}:{self.level}:{self.value}'

    def show(self) -> str:
        return f'{self.suit}:{self.level}'

    def get_value(self) -> int:
        return self.value
