from mcts_tree import MCTSTree as MCTS
from tictactoe import TicTacToe as Game
from tictactoe import Player
from tqdm import tqdm
from collections import Counter

import os
ttt = Game()


def run_sim(explore: float, time_limit: float, print_board: bool = False):
    game_state = ttt.get_starting_state()
    moves = []
    move_probs = []
    mcts1 = MCTS(ttt, explore, time_limit)
    mcts2 = MCTS(ttt, explore, time_limit)
    while (True):
        move = mcts1.mcts_search(game_state)
        moves.append(move)
        move_probs.append([mcts1.get_move_probs()])
        game_state = ttt.make_move(game_state, move)
        if print_board:
            ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            return ttt.reward(game_state, Player.CROSS), moves, move_probs
        move = mcts2.mcts_search(game_state)
        move_probs.append([mcts2.get_move_probs()])
        moves.append(move)
        game_state = ttt.make_move(game_state, move)
        if print_board:
            ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            return ttt.reward(game_state, Player.CROSS), moves, move_probs


def main():

    os.system("clear")
    lost_game_moves = []
    lost_game_probs = []

    outcomes = []
    for _ in tqdm(range(5)):
        val, moves, move_probs = run_sim(explore=0.7, time_limit=1, print_board=False)
        outcomes.append(val)
        if val != 0:
            lost_game_moves.append(moves)
            lost_game_probs.append(move_probs)

    with open("test_log.txt", 'w') as f:
        for i in range(len(lost_game_moves)):
            f.write(f"#### Lost game nr {i+1}\n")
            f.write(" ".join(lost_game_moves[i]))
            f.write('\n')
            for c in range(len(lost_game_probs[i])):
                f.write("".join(lost_game_probs[i][c]))
        f.close()

    print(Counter(outcomes))


if __name__ == "__main__":
    main()
