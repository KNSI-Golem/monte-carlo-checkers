class Checkers:
    '''
    BIG QUESTION - multimoves are possible in a game of checkers, when
    leaping over multiple pieces in succession. 
    Should we store this a single move, or rather as a sequence?
    '''

    def get_moves(self):
        pass

    def make_move(self, move):
        '''
        
        '''
        pass

    def get_state(self):
        pass

    def load_state(self, new_state):
        '''
        This will be used during training to make random moves from MCTSNodes state.
        '''
        pass