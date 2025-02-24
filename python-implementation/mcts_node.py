from __future__ import annotations
from game_state import GameState

class MCTSNode:

    children_nodes: tuple[MCTSNode] = []
    sims: int = 0
    wins: int = 0

    def __init__(self, game_state: GameState, parent_node: MCTSNode | None = None, prev_move = None):
        self.game_state = game_state
        self.parent_node = parent_node
        self.prev_move = prev_move


if __name__ == "__main__":
    pass