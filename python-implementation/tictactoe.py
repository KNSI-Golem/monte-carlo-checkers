from enum import Enum
from game_simulation import GameSimulation, GameState
import numpy as np


class BoardSlot(Enum):
    CROSS = 1
    CIRCLE = -1
    EMPTY = 0


class Move(Enum):
    CROSS = 1
    CIRCLE = -1


class TicTacToe(GameSimulation):
    class GameState(GameState):
        def __init__(self, board_state: list[BoardSlot], active_player: Move, game):
            self.board_state = board_state
            self.active_player = active_player
            moves = game.get_moves(self)  # awful fr
            return super().__init__(board_state, active_player, moves)

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

    def is_terminal(self, game_state: GameState) -> int | None:
        # check rows
        for row in self._indexes['rows']:
            row_sum = sum([game_state.board_state[slot_index].value for slot_index in row])
            if (abs(row_sum) == self.board_size):
                return Move(np.sign(row_sum))

        # check columns
        for column in self._indexes['columns']:
            column_sum = sum([game_state.board_state[slot_index].value for slot_index in column])
            if (abs(column_sum) == self.board_size):
                return Move(np.sign(column_sum))

        # check diagonals
        for diagonal in self._indexes['diagonals']:
            diagonal_sum = sum([game_state.board_state[slot_index].value for slot_index in diagonal])
            if (abs(diagonal_sum) == self.board_size):
                return Move(np.sign(diagonal_sum))

        # check if there are empty slots, if so -> no winner but game still goes on
        for slot in game_state.board_state:
            if slot == BoardSlot.EMPTY:
                return None

        # draw
        return 0  # we kinda return trash, but its fine

    def get_moves(self, game_state: GameState) -> list[str]:
        successors = []
        for index in range(self.board_size**2):
            if game_state.board_state[index] == BoardSlot.EMPTY:
                successors.append(f"{index}")
        return successors

    def make_move(self, game_state: GameState, move: str) -> GameState:
        """
        Make a move without checking the move correctness.
        """
        index = int(move)
        game_state.board_state[index] = BoardSlot(game_state.active_player.value)
        game_state.active_player = Move(game_state.active_player.value*-1)
        game_state.possible_moves = self.get_moves(game_state)
        return game_state

    def make_random_move(self, game_state: GameState) -> GameState:
        move_index = np.random.randint(0, len(game_state.possible_moves))
        return self.make_move(game_state, game_state.possible_moves[move_index])

    def get_starting_state(self) -> GameState:
        return TicTacToe.GameState([BoardSlot(0) for _ in range(self.board_size**2)], Move(-1), self)


if __name__ == "__main__":
    game = TicTacToe(3)
    start = game.get_starting_state()
    # first_move = game.make_random_move(start)
    start.board_state[0] = BoardSlot(1)
    start.board_state[1] = BoardSlot(1)
    start.board_state[2] = BoardSlot(1)
    print(game.is_terminal(start))
