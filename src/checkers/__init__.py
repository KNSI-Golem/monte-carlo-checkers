# Packages checkers into a single module for relative imports
from .checkers import Checkers  # noqa
from .board import CheckersPiece, CheckersBoard  # noqa
from .state import CheckersPlayer, CheckersState  # noqa
