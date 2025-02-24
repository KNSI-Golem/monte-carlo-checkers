from __future__ import annotations
from game_state import GameState
import math


class MCTSNode:

    children_nodes: list[MCTSNode] = []
    sims: int = 0
    wins: int = 0

    def __init__(self, game_state: GameState, parent_node: MCTSNode | None = None, prev_move = None):
        self.game_state = game_state
        self.parent_node = parent_node
        self.prev_move = prev_move
        self.moves_not_taken = game_state.possible_moves

    def get_ucb_score(self, explore_rate) -> float:
        if self.sims == 0:
            return math.inf
        return self.wins/self.sims + explore_rate*math.sqrt(math.log(self.parent_node.sims)/self.sims)


if __name__ == "__main__":
    pass
