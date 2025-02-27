from game_state import GameState, Move
from game_simulation import GameSimulation


class Checkers(GameSimulation):
    """
    BIG QUESTION - multimoves are possible in a game of checkers, when
    leaping over multiple pieces in succession.
    Should we store this a single move, or rather as a sequence?
    """

    def is_terminal(self, game_state: GameState) -> bool:
        pass

    def get_moves(self, game_state: GameState) -> list[Move]:
        pass

    def make_move(self, game_state: GameState, move: Move) -> GameState:
        pass

    def make_random_move(self, game_state: GameState) -> GameState:
        pass

    def get_starting_state(self) -> GameState:
        pass

    def reward(self) -> int:
        pass
