from bot_create import bot

class Table():
    id: int
    player: list
    current_player: int
    bet: int
    bank: int

    def __init__(self, id, bet: int, players: list):
        self.id = id
        self.bet = bet
        self.player = players
        # for player in args:
        #     if player.get_money() > self.bet:
        #         player.set_money(player.get_money() - self.bet)
        #         self.bank += self.bet
        #         self.player.append(player)
            # else:
            #     return f'За этим столом ставка - {self.bet}, а у тебя всего {player.get_money()}'
        self.current_player = 0

    def get_id(self) -> int:
        return self.id

    def get_bet(self) -> int:
        return self.bet

    def get_players(self) -> list:
        return self.player

    def seat(self, player):
        self.player.append(player)

    def next(self) -> bool:
        if self.current_player < len(self.player):
            self.current_player += 1
            return True
        else:
            self.current_player = 0
            return False

    def turn(self):
        return self.player[self.current_player]

    def is_empty(self):
        if self.player == []:
            return True
        else:
            return False
