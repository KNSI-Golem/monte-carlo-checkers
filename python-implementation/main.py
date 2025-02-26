from mcts_tree import MCTSTree as MCTS
from tictactoe import TicTacToe as Game
from tictactoe import Player
from tqdm import tqdm

import os
ttt = Game()
mcts1 = MCTS(ttt, 1, 1000)
mcts2 = MCTS(ttt, 1, 1000)

def run_sim():
    game_state = ttt.get_starting_state()
    while (True):
        move = mcts1.mcts_search(game_state)
        game_state = ttt.make_move(game_state, move)
        ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            return ttt.reward(game_state, Player.CROSS)
        move = mcts2.mcts_search(game_state)
        game_state = ttt.make_move(game_state, move)
        ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            return ttt.reward(game_state, Player.CROSS)


def main():
    # start game
    os.system("clear")
    # game_state = ttt.get_starting_state()

    # while (True):
    #     # get mcts move

    #     move = mcts1.mcts_search(game_state)
    #     print(f"MCTS move: {move}")
    #     ttt.make_move(game_state, move)
    #     ttt.print_board(game_state)
    #     player_move = input("Your Move: ")
    #     os.system("clear")
    #     game_state = ttt.make_move(game_state, player_move)
    outcomes = []
    for _ in tqdm(range(1000)):
        outcomes.append(run_sim())
    print(outcomes)

if __name__ == "__main__":
    main()
