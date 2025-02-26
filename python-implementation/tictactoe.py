from enum import Enum
from game_simulation import GameSimulation
from game_state import GameState, Move
import numpy as np


class BoardSlot(Enum):
    CROSS = 1
    CIRCLE = -1
    EMPTY = 0


class Player(Enum):
    CROSS = 1
    CIRCLE = -1


class GameState(GameState):
    def __init__(self, board: list[BoardSlot], active_player: Player):
        self.board = board
        self.active_player = active_player


class TicTacToe(GameSimulation):
    def __init__(self, board_size: int = 3) -> None:
        self.board_size = board_size
        self._indexes = dict()
        self._calucalte_checking_indexes()

    def _calucalte_checking_indexes(self):
        self._indexes['rows'] = [[x+y*self.board_size for x in range(self.board_size)] for y in range(self.board_size)]
        self._indexes['columns'] = [[x+y*self.board_size for y in range(self.board_size)] for x in range(self.board_size)]
        self._indexes['diagonals'] = [
            [[x+y*self.board_size for x in range(self.board_size) if x == y][0] for y in range(self.board_size)],
            [[x+y*self.board_size for x in range(self.board_size) if x+y == self.board_size-1][0] for y in range(self.board_size)]
        ]

    def reward(self, game_state: GameState) -> int | None:
        # check rows
        for row in self._indexes['rows']:
            row_sum = sum([game_state.board[slot_index].value for slot_index in row])
            if (abs(row_sum) == self.board_size):
                return np.sign(row_sum)

        # check columns
        for column in self._indexes['columns']:
            column_sum = sum([game_state.board[slot_index].value for slot_index in column])
            if (abs(column_sum) == self.board_size):
                return np.sign(column_sum)

        # check diagonals
        for diagonal in self._indexes['diagonals']:
            diagonal_sum = sum([game_state.board[slot_index].value for slot_index in diagonal])
            if (abs(diagonal_sum) == self.board_size):
                return np.sign(diagonal_sum)

        # check if there are empty slots, if so -> no winner but game still goes on
        for slot in game_state.board:
            if slot == BoardSlot.EMPTY:
                return None

        # draw
        return 0

    def is_terminal(self, game_state: GameState) -> bool:
        if self.reward(game_state) is None:
            return False
        return True

    def get_moves(self, game_state: GameState) -> list[Move]:
        successors = []
        for index in range(self.board_size**2):
            if game_state.board[index] == BoardSlot.EMPTY:
                successors.append(f"{index}")
        return successors

    def make_move(self, game_state: GameState, move: Move) -> GameState:
        """
        Make a move without checking the move correctness.
        """
        index = int(move)
        game_state.board[index] = BoardSlot(game_state.active_player.value)
        game_state.active_player = Player(game_state.active_player.value*-1)
        return game_state

    def make_random_move(self, game_state: GameState) -> GameState:
        possible_moves = self.get_moves(game_state)
        move_index = np.random.randint(0, len(possible_moves))
        return self.make_move(game_state, possible_moves[move_index])

    def get_starting_state(self) -> GameState:
        return GameState([BoardSlot(0) for _ in range(self.board_size**2)], Player(-1))


if __name__ == "__main__":
    game = TicTacToe(3)
    start = game.get_starting_state()
    # first_move = game.make_random_move(start)
    start.board[0] = BoardSlot(1)
    start.board[1] = BoardSlot(1)
    start.board[2] = BoardSlot(1)
    print(game.is_terminal(start))
