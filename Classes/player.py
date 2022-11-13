from aiogram import types

from Classes.card import Card


class Player:
    name: str
    id: int
    money: int
    cards: list
    value: int

    def __init__(self, message: types.Message):
        self.name = message.from_user.first_name
        self.id = message.from_user.id
        self.cards = []
        self.money = 1000
        self.value = 0

    def want_to_play(self):
        pass

    def info(self):
        return f'{self.name}({self.id}) : {self.money}'

    def take_card(self, card: Card):
        self.cards.append(card)

    def show(self):
        return self.cards

    def show_cards(self) -> str:
        cards = ''
        for card in self.cards:
            cards += card.show() + '\n'
        return cards

    def get_value(self) -> int:
        return self.value

    def set_value(self, value):
        self.value += value