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

    def get_best_move(self, init_state: GameState):
        self.root = MCTSNode(init_state)
        self._run_mcts()
        best_kid = self._get_best_child()
        return best_kid.prev_move

    def _run_mcts(self) -> None:
        pass

    def _selection(self, current_node: MCTSNode) -> MCTSNode:
        possible_moves = self.my_game.get_moves(current_node.game_state)
        while (len(current_node.children_nodes) == len(possible_moves)):
            ucb_scores = [node.get_ucb_score() for node in current_node.children_nodes]
            max_score_index = np.argmax(ucb_scores)[0]
            current_node = current_node.children_nodes[max_score_index]
            possible_moves = self.my_game.get_moves(current_node.game_state)
        return current_node
    
    def _expansion(self, leaf_mode: MCTSNode) -> None:
        # check 
        pass
    
    def _simulation(self) -> None:
        pass

    def _get_best_child(self) -> MCTSNode:
        root_kids = [kid for kid in self.root.children_nodes]
        return max(root_kids, key=lambda x: x.wins/x.sims)

