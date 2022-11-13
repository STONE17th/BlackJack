class Game:
    _players: list

    def __init__(self):
        self._players = []

    def add(self, player):
        self._players.append(player)

    def show(self) -> str:
        info = ''
        if not self._players == []:
            for player in self._players:
                info += player.info() + '\n'
        return info

    def get_players(self):
        if not self._players == []:
            return self._players.pop(0)
        else:
            return 'Игроков пока нет'

    def is_empty(self):
        if not self._players == []:
            return False
        else:
            return True

