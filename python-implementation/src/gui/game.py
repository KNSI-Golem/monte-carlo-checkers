import pygame

from .display import Display

from ..mcts import MCTSTree as MCTS
from src.checkers import Checkers


def start_game(display: Display):
    """Starts the checkers game."""
    game = Checkers()
    state = game.get_starting_state()
    # mcts1 = MCTS(game, 1.41, 200)
    # mcts2 = MCTS(game, 1.41, 1600)

    pygame.init()
    while game.is_terminal(state) is False:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return
                case pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    move = (x // display.square_size, y // display.square_size)
                    state = game.make_move(state, move)
                case _:
                    pass

        display.draw_board(state)
        pygame.display.update()
