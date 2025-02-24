from mcts_node import MCTSNode
from game_state import GameState
import multiprocessing as mp
from checkers import Checkers
import time

class MCTSTree:
    '''
    4 stages of MCTS:
    1. selection - select node
    2. expansion - add all of node's kids to tree
    3. simulation - play `sims_per` games with random moves, save nr of wins and nr of attempts
    4. backprop - backprop the nr of wins and attempts
    '''
        
    def __init__(self, my_game: Checkers, C: float, sims_per: int, iteration_limit: int) -> None:
        self.my_game = my_game
        self.C = C
        self.sims_per = sims_per

    def get_best_move(self, init_state: GameState):
        self.root = MCTSNode(init_state)
        self._run_mcts()
        best_kid = self._get_best_child()
        return best_kid.prev_move

    def _run_mcts(self) -> None:
        pass

    def _selection(self) -> None:
        # calc UCB for all kids 
        pass
    
    def _expansion(self) -> None:
        pass
    
    def _simulation(self) -> None:
        pass

    def _get_best_child(self) -> MCTSNode:
        root_kids = [kid for kid in self.root.children_nodes]
        return max(root_kids, key=lambda x: x.wins/x.sims)

