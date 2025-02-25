from dataclasses import dataclass


@dataclass
class GameState:
    """
    It needs to be possible to load and save a game state from some sort of string,
    so that we can save our model.
    Does it have to be a string? Prolly not, but it maybe needs to be hashable?

    GameState will also need == operator so that we can find node in tree which
    is responsible for current GameState
    """
    board_state: str = None  # how do we want to store these?
    active_player: str = None  # B or W
    possible_moves: list[str] = None
    terminated: bool = False

    # def __init__(self, board_state: str, possible_moves: tuple[str], active_player: str) -> None:
    #     '''
    #     This should read above values from representation and save them in self.
    #     '''
    #     self.board_state = board_state
    #     self.possible_moves = possible_moves
    #     self.active_player = active_player
    #     pass
    def is_terminal(self):
        return self.terminated

    def get_reward(self):
        pass
