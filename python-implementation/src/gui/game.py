import pygame
from enum import Enum
from .display import Display
from ..mcts import MCTSTree as MCTS
from ..checkers import Checkers, CheckersState


class Gamemode(Enum):
    PLAYER_VS_PLAYER = 1
    PLAYER_VS_AI = 2
    AI_VS_AI = 3


class PygameCheckers:
    def __init__(
        self, width: int, height: int, starting_state: CheckersState, gamemode: Gamemode
    ):
        self.game = Checkers()
        self.display = Display(width, height)
        self.state = starting_state
        self.gamemode = gamemode
        self.ai = MCTS(self.game, 1.41, 1)
        self.xy_selected = None

    def play_game(self):
        """Starts the checkers game."""
        pygame.init()

        player_turn = True
        while self.game.is_terminal(self.state) is False:

            self.display.draw_board(self.state)
            pygame.display.update()

            if self.gamemode == Gamemode.PLAYER_VS_PLAYER:
                self.handle_player_turn()
            if self.gamemode == Gamemode.AI_VS_AI:
                self.handle_ai_turn()

            elif self.gamemode == Gamemode.PLAYER_VS_AI:
                if player_turn:
                    result = self.handle_player_turn()
                elif not player_turn:
                    self.handle_ai_turn()
                    result = True
                player_turn = not player_turn if result else player_turn

        pygame.quit()

    def handle_player_turn(self) -> None:
        """Handles the player's turn, allowing them to make a move."""
        moves_str = self.game.get_moves(self.state)
        moves_8x8 = self._convert_moves(moves_str)

        move_success = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x, y = x // self.display.square_size, y // self.display.square_size
                xy_current = (x, y)

                if self.xy_selected is not None:
                    move = (self.xy_selected, xy_current)
                    if move in moves_8x8:
                        move = moves_str[moves_8x8.index(move)]
                        self.state = self.game.make_move(self.state, move)
                        move_success = True
                    self.display.highlight_square(None)
                    self.xy_selected = None
                else:
                    self.display.highlight_square(xy_current)
                    self.xy_selected = xy_current

        return move_success

    def handle_ai_turn(self):
        """Handles the AI's turn, using MCTS to pick the best move."""
        move = self.ai.mcts_search(self.state)
        self.state = self.game.make_move(self.state, move)

    @staticmethod
    def _idx32_to_8x8cords(idx: int) -> str:
        y = idx // 4
        x = (idx % 4) * 2 + (y % 2 == 0)
        return (x, y)

    def _convert_moves(self, moves_str: list[str]) -> list[tuple[int, int]]:
        converted = []
        for move_str in moves_str:
            squares = move_str.split(
                "x") if "x" in move_str else move_str.split("-")
            first_square, last_square = squares[0], squares[-1]
            move_cords = (
                self._idx32_to_8x8cords(int(first_square)),
                self._idx32_to_8x8cords(int(last_square)),
            )
            converted.append(move_cords)
        return converted
