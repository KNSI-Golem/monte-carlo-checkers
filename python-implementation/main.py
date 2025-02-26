from mcts_tree import MCTSTree as MCTS
from tictactoe import TicTacToe as Game


def main():
    ttt = Game()
    mcts = MCTS(ttt, 0.3, 1200)

    # start game
    start = ttt.get_starting_state()

    # get mcts move
    move = mcts.mcts_search(start)

    print(move)


if __name__ == "__main__":
    main()
