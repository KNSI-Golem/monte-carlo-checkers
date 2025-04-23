from src.gui import PygameCheckers, Gamemode
from src.checkers import Checkers

if __name__ == "__main__":
    WIDTH = 1920
    HEIGHT = 1080
    starting_state = Checkers().get_starting_state()  # Default position
    gamemode = Gamemode.PLAYER_VS_AI

    game = PygameCheckers(WIDTH, HEIGHT, starting_state, gamemode)
    game.play_game()
