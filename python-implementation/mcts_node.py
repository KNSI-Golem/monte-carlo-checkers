from __future__ import annotations
from game_state import GameState
import math


class MCTSNode:
    children_nodes: list[MCTSNode] = []
    visit_count: int = 0
    q_value: int = 0

    def __init__(self, game_state: GameState, parent_node: MCTSNode | None = None, prev_move=None):
        self.game_state = game_state
        self.parent_node = parent_node
        self.prev_move = prev_move
        self.moves_not_taken = game_state.possible_moves

    def get_ucb_score(self, explore_rate: float = 1 / math.sqrt(2)) -> float:
        if self.visit_count == 0:
            return math.inf
        return self.q_value / self.visit_count + explore_rate * math.sqrt(math.log(self.parent_node.visit_count) /
                                                                          self.visit_count)

    def is_terminal(self):
        return self.game_state.is_terminal()


if __name__ == "__main__":
    pass
