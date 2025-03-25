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

    square_selected = None

    pygame.init()
    while game.is_terminal(state) is False:
        moves_str = game.get_moves(state)
        moves_8x8 = convert_moves(moves_str)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return

                case pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    move_square = (x // display.square_size, y // display.square_size)

                    if square_selected is not None:
                        if (square_selected, move_square) in moves_8x8:
                            move = moves_str[
                                moves_8x8.index((square_selected, move_square))
                            ]
                            state = game.make_move(state, move)

                        display.highlight_square(None)
                        square_selected = None

                    else:
                        display.highlight_square(move_square)
                        square_selected = move_square

        display.draw_board(state)
        pygame.display.update()


def idx32_to_8x8cords(idx: int) -> str:
    y = idx // 4
    x = (idx % 4) * 2 + (y % 2 == 0)
    return (x, y)


def convert_moves(moves_str: list[str]) -> list[tuple[int, int]]:
    converted = []
    for move_str in moves_str:
        squares = move_str.split("x") if "x" in move_str else move_str.split("-")
        first_square, last_square = squares[0], squares[-1]
        move_cords = (
            idx32_to_8x8cords(int(first_square)),
            idx32_to_8x8cords(int(last_square)),
        )
        converted.append(move_cords)
    return converted
