from abc import ABC, abstractmethod
from game_state import GameState


class GameSimulation(ABC):
    @abstractmethod
    def is_terminal(self, game_state: GameState) -> str | None:
        pass

    @abstractmethod
    def get_moves(self, game_state: GameState) -> list[str]:
        pass

    @abstractmethod
    def make_move(self, game_state: GameState, move: str) -> GameState:
        pass

    @abstractmethod
    def make_random_move(self, game_state: GameState) -> GameState:
        pass

    @abstractmethod
    def get_starting_state(self) -> GameState:
        pass
