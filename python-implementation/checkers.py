from game_state import GameState
from game_simulation import GameSimulation


class Checkers(GameSimulation):
    '''
    BIG QUESTION - multimoves are possible in a game of checkers, when
    leaping over multiple pieces in succession. 
    Should we store this a single move, or rather as a sequence?
    '''

    def is_terminal(self, game_state: GameState) -> str | None:
        '''
        Returns name of Player ('B' or 'W') who won the game, if one won the game.
        If game isn't over, returns None.
        '''
        pass

    def get_moves(self, game_state: GameState) -> list[GameState]:
        pass

    def make_move(self, game_state: GameState, move: str) -> GameState:
        pass

    def make_random_move(self, game_state: GameState) -> GameState:
        pass

    def get_starting_state(self) -> GameState:
        pass
