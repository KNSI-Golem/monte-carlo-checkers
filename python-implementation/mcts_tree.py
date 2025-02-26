from mcts_node import MCTSNode
from game_state import GameState, Move
from game_simulation import GameSimulation
import numpy as np
from copy import deepcopy


class MCTSTree:
    """
    Monte Carlo Tree Search is a method for finding optimal decision in a given game state.
    This class provides methods for running algorithm in given game environment.
    """

    def __init__(self, game: GameSimulation, explore_rate: float, iteration_limit: int) -> None:
        self.root = None
        self.game = game
        self.explore_rate = explore_rate
        self.iteration_limit = iteration_limit

    def mcts_search(self, init_state: GameState) -> Move:
        """
        Implementation of basic algorithm that involves building a search tree
        until predefined computational budget - time.
        :param init_state: current game state
        :return: action that leads to the best child of init_state
        """
        self.root = MCTSNode(deepcopy(init_state), self.game.get_moves(init_state))
        self._run_mcts()
        for child in self.root.children_nodes:
            print(f"{child.prev_move} {child.q_value/child.visit_count:.3}")
        best_child = self._get_best_child()
        return best_child.prev_move

    def _run_mcts(self) -> None:
        for _ in range(self.iteration_limit):
            node = self._selection(self.root)
            reward = self._simulation(node)
            self._backprop(node, reward)

    def _selection(self, current_node: MCTSNode) -> MCTSNode:
        while not self.game.is_terminal(current_node.game_state):
            if len(current_node.moves_not_taken) != 0:
                return self._expansion(current_node)

            ucb_scores = [node.get_ucb_score() for node in current_node.children_nodes]
            max_score_index = np.argmax(ucb_scores)
            current_node = current_node.children_nodes[max_score_index]

        return current_node

    def _expansion(self, leaf_node: MCTSNode) -> MCTSNode:
        move_index = np.random.randint(0, len(leaf_node.moves_not_taken))
        move = leaf_node.moves_not_taken.pop(move_index)

        new_game_state = self.game.make_move(deepcopy(leaf_node.game_state), move)
        new_node = MCTSNode(new_game_state, self.game.get_moves(new_game_state), move, leaf_node)

        leaf_node.children_nodes.append(new_node)
        return new_node  # debug and see if memory layout is ok, ie. if leaf_node.children...[-1] return isn't needed

    def _simulation(self, start_node: MCTSNode) -> int:
        new_state = deepcopy(start_node.game_state)

        while not self.game.is_terminal(new_state):
            new_state = self.game.make_random_move(new_state)

        # self.game.print_board(new_state)
        simulation_result = self.game.reward(new_state, self.root.game_state.active_player)
        return simulation_result

    def _backprop(self, leaf_node: MCTSNode, reward: int = 1 | 0 | -1) -> None:
        while True:
            if (reward == 0.5):
                leaf_node.q_value += reward
            else:
                if (leaf_node.game_state.active_player != self.root.game_state.active_player):
                    leaf_node.q_value += reward

            leaf_node.visit_count += 1
            if leaf_node.parent_node is None:
                return
            leaf_node = leaf_node.parent_node

    def _get_best_child(self) -> MCTSNode:
        root_children = [child for child in self.root.children_nodes]
        return max(root_children, key=lambda x: x.q_value / x.visit_count)
