class Checkers:
    '''
    BIG QUESTION - multimoves are possible in a game of checkers, when
    leaping over multiple pieces in succession. 
    Should we store this a single move, or rather as a sequence?
    '''
    def get_moves(self, check_state = None):
        pass

    def make_move(self, move):
        '''
        
        '''
        pass

    def make_random_move(self):
        pass

    def get_state(self):
        pass

    def set_state(self, new_state):
        '''
        This will be used during training to make random moves from MCTSNodes state.
        '''
        self.state = new_state