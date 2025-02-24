class GameState:
    '''
    It needs to be possible to load and save a game state from some sort of string,
    so that we can save our model.
    Does it have to be a string? Prolly not, but it maybe needs to be hashable?

    GameState will also need == operator so that we can find node in tree which 
    is responsible for current GameState 
    '''

    board_state = None # how do we want to store these?
    active_player = None
    possible_moves = None # should this be stored 

    def __init__(self, state_representation: str) -> None:
        '''
        This should read above values from representation and save them in self.
        '''
        pass

    def get_representation(self):
