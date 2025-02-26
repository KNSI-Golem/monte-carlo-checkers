from mcts_tree import MCTSTree as MCTS
from tictactoe import TicTacToe as Game
import os


def main():
    ttt = Game()
    mcts = MCTS(ttt, 0.7, 800)

    # start game
    next_state = ttt.get_starting_state()
    os.system("clear")

    while (True):
        # get mcts move
        move = mcts.mcts_search(next_state)

        print(f"MCTS move: {move}")
        next_state = ttt.make_move(next_state, move)
        ttt.print_board(next_state)
        player_move = input("Your Move: ")
        os.system("clear")
        next_state = ttt.make_move(next_state, player_move)


if __name__ == "__main__":
    main()
