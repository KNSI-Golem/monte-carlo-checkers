from copy import deepcopy

from mcts_node import MCTSNode
from game_state import GameState
from checkers import Checkers
import numpy as np


class MCTSTree:
    """
    4 stages of MCTS:
    1. selection - select node
    2. expansion - add all of node's kids to tree
    3. simulation - play `sims_per` games with random moves, save nr of wins and nr of attempts
    4. backprop - backprop the nr of wins and attempts
    """

    def __init__(self, my_game: Checkers, explore_rate: float, sims_per: int, iteration_limit: int) -> None:
        self.root = None
        self.my_game = deepcopy(my_game)
        self.explore_rate = explore_rate
        self.sims_per = sims_per
        self.iteration_limit = iteration_limit

    def mcts_search(self, init_state: GameState) -> str:
        """
        Implementation of basic algorithm that involves building a search tree
        until predefined computational budget - time.
        :param init_state: current game state
        :return: action that leads to the best child of init_state
        """
        self.root = MCTSNode(init_state)
        self._run_mcts()
        best_child = self._get_best_child()
        return best_child.prev_move

    def _run_mcts(self) -> None:
        for _ in range(self.iteration_limit):
            node = self._selection(self.root)
            node = self._expansion(node)
            self._simulation(node)
            self._backprop(node)

    def _selection(self, current_node: MCTSNode) -> MCTSNode:
        while len(current_node.moves_not_taken) == 0 and not current_node.is_terminal():
            ucb_scores = [node.get_ucb_score() for node in current_node.children_nodes]
            max_score_index = np.argmax(ucb_scores)[0]
            current_node = current_node.children_nodes[max_score_index]
        return current_node

    def _expansion(self, leaf_node: MCTSNode) -> MCTSNode:
        move_index = np.random.randint(0, len(leaf_node.moves_not_taken))
        move = leaf_node.moves_not_taken.pop(move_index)
        new_node = MCTSNode(self.my_game.make_move(leaf_node.game_state, move), parent_node=leaf_node, prev_move=move)
        leaf_node.children_nodes.append(new_node)
        return new_node

    def _simulation(self, start_node: MCTSNode) -> None:
        new_state = start_node

        while not new_state.is_terminal():
            new_state = self.my_game.make_random_move(new_state)

        reward = new_state.get_reward()

        return reward

    def _backprop(self, leaf_node: MCTSNode, reward: 1 | 0 | -1) -> None:
        while leaf_node.parent_node is not None:
            leaf_node.visit_count += 1
            leaf_node.q_value += reward
            reward = -reward
            leaf_node = leaf_node.parent_node

    def _get_best_child(self) -> MCTSNode:
        root_kids = [kid for kid in self.root.children_nodes]
        return max(root_kids, key=lambda x: x.q_value / x.visit_count)
