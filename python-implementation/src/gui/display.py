import pygame
import sys
import pkg_resources
from ..checkers import CheckersPiece, CheckersState

class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_size = width // 8 if width < height else height // 8

        self.screen = self._init_screen(width, height)

    def _load_image(self, image_name):
        image_path = pkg_resources.resource_filename(__name__, f"assets/{image_name}")
        return pygame.image.load(image_path)


    def _get_piece_image(self, piece: CheckersPiece):
        match (piece):
            case CheckersPiece.BLACK:
                return self._load_image("black_piece.png")
            case CheckersPiece.WHITE:
                return self._load_image("white_piece.png")
            case CheckersPiece.BLACK_QUEEN:
                return self._load_image("black_queen.png")
            case CheckersPiece.WHITE_QUEEN:
                return self._load_image("white_queen.png")
            case CheckersPiece.EMPTY:
                return None


    def draw_board(self, state: CheckersState):
        pieces = state.get_board().get_squares()
        for j in range(8):
            for i in range(8):
                color = (255, 255, 255) if (i + j) % 2 != 0 else (0, 0, 0)
                pygame.draw.rect(
                    self.screen,
                    color,
                    (i * self.square_size, j * self.square_size, self.square_size, self.square_size),
                )
                if i % 2 == j % 2:
                    indx = j * 4 + i // 2
                    piece = pieces[indx]
                    if piece != CheckersPiece.EMPTY:
                        img = self._get_piece_image(piece)
                        img = pygame.transform.scale(img, (0.75*self.square_size, 0.75*self.square_size))
                        x_pad, y_pad = self._calculate_padding(img, self.square_size, self.square_size)
                        self.screen.blit(img, (i * self.square_size + x_pad, j * self.square_size + y_pad))
                    

    def _init_screen(self, width, height):
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Golemowe Warcaby")
        return screen


    def _calculate_padding(self, img, new_width, new_height):
        img_width, img_height = img.get_width(), img.get_height()
        target_width = int(0.75 * self.square_size)
        target_height = int(0.75 * self.square_size)
        x_pad = (self.square_size - target_width) // 2
        y_pad = (self.square_size - target_height) // 2
        return x_pad, y_pad
