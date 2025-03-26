from __future__ import annotations
import math
from ..interfaces import GameState, Move


class MCTSNode:
    def __init__(self,
                 game_state: GameState,
                 possible_state_moves: list[Move],
                 prev_move: Move | None = None,
                 parent_node: MCTSNode | None = None
                 ) -> None:

        self.game_state = game_state
        self.parent_node = parent_node
        # move that was taken in order to get from parent node to this node. None when root node
        self.prev_move = prev_move
        self.moves_not_taken = possible_state_moves

        self.children_nodes: list[MCTSNode] = []
        self.visit_count: int = 0
        self.q_value: int = 0

    def get_ucb_score(self, explore_rate: float = 1 / math.sqrt(2)) -> float:
        if self.visit_count == 0:
            return math.inf
        return self.q_value / self.visit_count + explore_rate * math.sqrt(math.log(self.parent_node.visit_count) /
                                                                          self.visit_count)
