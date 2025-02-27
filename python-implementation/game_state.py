from typing import TypeAlias

Move: TypeAlias = str


class Player:
    pass


class GameState:
    def __init__(self):
        self.active_player = None
