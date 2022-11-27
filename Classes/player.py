from aiogram import types

from Classes.card import Card


class Player:
    player_id: int
    name: str
    dis_id: int
    money: float
    cards: list
    value: int
    current_player_id = 1

    def __init__(self, message: types.Message):
        self.player_id = Player.current_player_id
        self.name = message.from_user.first_name
        self.dis_id = message.from_user.id
        self.cards = []
        self.money = 1000.0
        self.value = 0
        Player.current_player_id += 1


    def greetings(self):
        return f'Привет, {self.name}!\nУ тебя {self.money}\nЧто будешь делать?'
    def get_id(self):
        return self.player_id

    def get_dis_id(self):
        return self.dis_id
    def get_money(self) -> float:
        return self.money

    def set_money(self, money):
        self.money = money

    def info(self):
        return f'{self.player_id} {self.name} ({self.dis_id}) : {self.money}'

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
        value = 0
        for card in self.cards:
            value += card.get_value()
        return value
