from game_state import GameState


class Checkers:
    """
    BIG QUESTION - multimoves are possible in a game of checkers, when
    leaping over multiple pieces in succession.
    Should we store this a single move, or rather as a sequence?
    """

    def is_terminal(self, state: GameState) -> str | None:
        """
        Returns name of Player ('B' or 'W') who won the game, if one won the game.
        If game isn't over, returns None.
        """
        pass

    def get_moves(self, check_state=None):
        pass

    def make_move(self, state: GameState, move: str) -> GameState:
        pass

    def make_random_move(self, state: GameState) -> GameState:
        pass
