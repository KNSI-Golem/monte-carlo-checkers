from mcts_node import MCTSNode
from game_state import GameState
from checkers import Checkers
import numpy as np

class MCTSTree:
    '''
    4 stages of MCTS:
    1. selection - select node
    2. expansion - add all of node's kids to tree
    3. simulation - play `sims_per` games with random moves, save nr of wins and nr of attempts
    4. backprop - backprop the nr of wins and attempts
    '''
        
    def __init__(self, my_game: Checkers, explore_rate: float, sims_per: int, iteration_limit: int) -> None:
        self.my_game = my_game
        self.explore_rate = explore_rate
        self.sims_per = sims_per
        self.iteration_limit = iteration_limit

    def get_best_move(self, init_state: GameState) -> str:
        self.root = MCTSNode(init_state)
        self._run_mcts()
        best_kid = self._get_best_child()
        return best_kid.prev_move

    def _run_mcts(self) -> None:

        for _ in range(self.iteration_limit):
            node = self._selection(self.root)
            node = self._expansion(node)
            self._simulation(node)
            self._backprop(node)

    def _selection(self, current_node: MCTSNode) -> MCTSNode:
        while len(current_node.moves_not_taken) == 0:
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
        for _ in range(self.sims_per):

            winner = self.my_game.is_terminal(start_node)
            new_state = start_node

            while winner is not None:
                new_state = self.my_game.make_random_move(new_state)
                winner = self.my_game.is_terminal(new_state)

            start_node.sims += 1
            start_node.wins += (winner == self.root.game_state.active_player)

    def _backprop(self, leaf_node: MCTSNode) -> None:
        '''
        This method, explicitly named _backprop, should propagate the results
        of the latest simulation backwards.
        '''
        pass

    def _get_best_child(self) -> MCTSNode:
        root_kids = [kid for kid in self.root.children_nodes]
        return max(root_kids, key=lambda x: x.wins/x.sims)

