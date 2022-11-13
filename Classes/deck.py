import asyncio
import random

from Classes import card



class Deck:
    card: list
    count: int

    def __init__(self, count: int):
        self.card = []
        if count == 36:
            for suit in card.Card.suits:
                for level in card.Card.levels[4:]:
                    self.card.append(card.Card(suit, level))
        elif count == 52:
            for suit in card.Card.suits:
                for level in card.Card.levels:
                    self.card.append(card.Card(suit, level))
        elif count == 54:
            for suit in card.Card.suits:
                for level in card.Card.levels:
                    self.card.append(card.Card(suit, level))
            self.card.append(card.Card('Jocker', 'Jocker'))
        else:
            print('Ошибка')

    def shuffle(self):
        random.shuffle(self.card)

    def take(self):
        return self.card.pop(0)


# deck = Deck(52)
# deck.shuffle()
#
#
#
# def player_turn():
#     player_summa = 0
#     player_cards = []
#     choice = 1
#     while choice:
#         player_card = deck.take()
#         player_cards.append(player_card)
#         print(player_card.info())
#         player_summa += player_card.get_value()
#         print(f'У тебя {player_summa} очков')
#         if player_summa > 21:
#             print('Перебор')
#             player_summa = 0
#             return player_summa
#         choice = int(input('Еще? (1/0)'))
#     else:
#         print('У игрока на руках:')
#         for card in player_cards:
#             print(card.info())
#         print(f'Общей суммой {player_summa}')
#     return player_summa
#
#
# def enemy_turn():
#     enemy_summa = 0
#     enemy_cards = []
#     choice = 1
#     while choice:
#
#         enemy_card = deck.take()
#         enemy_cards.append(enemy_card)
#         print(enemy_card.info())
#         enemy_summa += enemy_card.get_value()
#         print(f'У тебя {enemy_summa} очков')
#         if enemy_summa > 21:
#             print('Перебор')
#             enemy_summa = 0
#             return enemy_summa
#         if enemy_summa <= 10:
#             choice = True
#         elif enemy_summa <= 16:
#             choice = random.randint(0,1)
#         elif enemy_summa <= 18:
#             rand = choice = random.randint(0,10)
#             if rand <= 2:
#                 choice = 1
#             else:
#                 choice = 0
#     else:
#         print('У противника на руках:')
#         for card in enemy_cards:
#             print(card.info())
#         print(f'Общей суммой {enemy_summa}')
#     return enemy_summa
#
# result = player_turn() > enemy_turn()
#
# if result:
#     print('Победил игрок')
# elif not result:
#     print('Победил компьютер')
# else:
#     print('Попилили бабки')
#
#
#
#

