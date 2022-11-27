from Classes.table import Table
from bot_create import bot


class Game:
    _players: list
    _tables: list
    _current_table_id: int
    _current_player_id: int

    def __init__(self):
        self._players = []
        self._tables = []
        self._current_table_id = 1

    def get_table_id(self):
        return self._current_table_id
    def create_table(self, player_id, bet):
        for play in self._players:
            if player_id == play.get_dis_id():
                player = play
        table = Table(self._current_table_id, bet, [player])
        self._tables.append(table)
        self._current_table_id += 1

    def add(self, player):
        self._players.append(player)

    def show_tables(self) -> str:
        tables_list = ''
        if not self._tables == []:
            for table in self._tables:
                tables_list += f'#{table.get_id()} | Ставка: {table.get_bet()}\n'
                for player in table.get_players():
                    tables_list += f'{player.info()}\n'
                tables_list += '\n'
            return tables_list
        else:
            return 'Столов нет'

    def seat(self, player_id: int, table_id: int):
        player = None
        for play in self._players:
            if play.get_dis_id() == player_id:
                player = play
        for table in self._tables:
            if table.get_id() == table_id:
                table.seat(player)



    def show_players(self) -> str:
        info = ''
        if not self._players == []:
            for player in self._players:
                info += player.info() + '\n'
            return info
        else:
            return 'Игроков в ожидании нет'

    def play_with(self, id: int):
        if not self._players == []:
            for index, player in enumerate(self._players):
                if player.get_id == id:
                    return self._players.pop(index)
        else:
            return 'Игрок с таким ID не найден'

    def play_random(self):
        if not self._players == []:
            return self._players.pop(0)
        else:
            return 'Игроков пока нет'

    def is_empty(self):
        if not self._players == []:
            return False
        else:
            return True

    def players_list(self) -> list:
        return self._players

