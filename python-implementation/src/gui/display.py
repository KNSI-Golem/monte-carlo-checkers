import pygame
import sys
import pkg_resources
from ..checkers import CheckersPiece, CheckersBoard

SQUARE_SIZE = 64
WIDTH = HEIGHT = 8 * SQUARE_SIZE


def load_image(image_name):
    image_path = pkg_resources.resource_filename(__name__, f"assets/{image_name}")
    return pygame.image.load(image_path)


def get_piece_image(piece):
    match (piece):
        case CheckersPiece.BLACK:
            return load_image("black_piece.png")
        case CheckersPiece.WHITE:
            return load_image("white_piece.png")
        case CheckersPiece.BLACK_QUEEN:
            return load_image("black_queen.png")
        case CheckersPiece.WHITE_QUEEN:
            return load_image("white_queen.png")
        case CheckersPiece.EMPTY:
            return None


def draw_board(screen, board):
    pieces = board.get_squares()
    for i in range(8):
        for j in range(8):
            color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(
                screen,
                color,
                (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )
            piece = pieces[i * 8 + j]
            if piece:
                piece_image = get_piece_image(piece.color)
                screen.blit(piece_image, (i * SQUARE_SIZE, j * SQUARE_SIZE))


def create_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Golemowe Warcaby")
    return screen


def start_game():
    """Starts the checkers game."""
    pygame.init()
    screen = create_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_board(screen)  # Draw the checkers board

        pygame.display.update()  # Update the display
