from mcts_node import MCTSNode
from game_state import GameState
from game_simulation import GameSimulation
import numpy as np


class MCTSTree:
    """
    Monte Carlo Tree Search is a method for finding optimal decision in a given game state.
    This class provides methods for running algorithm in given game environment.
    """

    def __init__(self, my_game: GameSimulation, explore_rate: float, iteration_limit: int) -> None:
        self.root = None
        self.my_game = my_game
        self.explore_rate = explore_rate
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
            reward = self._simulation(node)
            self._backprop(node, reward)

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

    def _simulation(self, start_node: MCTSNode) -> int:
        new_state = start_node.game_state

        while not self.my_game.is_terminal(new_state):
            new_node = self.my_game.make_random_move(new_state)

        simulation_result = self.my_game.reward(new_node.game_state)

        return simulation_result

    def _backprop(self, leaf_node: MCTSNode, reward: int = 1 | 0 | -1) -> None:
        while leaf_node.parent_node is not None:
            leaf_node.visit_count += 1
            leaf_node.q_value += reward
            reward = -reward
            leaf_node = leaf_node.parent_node

    def _get_best_child(self) -> MCTSNode:
        root_children = [child for child in self.root.children_nodes]
        return max(root_children, key=lambda x: x.q_value / x.visit_count)
