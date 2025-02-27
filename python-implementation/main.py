from mcts_tree import MCTSTree as MCTS
from tictactoe import TicTacToe as Game
from tictactoe import Player
from tqdm import tqdm
from collections import Counter

# import os
ttt = Game()
mcts1 = MCTS(ttt, 0.7, 1600)
mcts2 = MCTS(ttt, 0.7, 1600)
moves = []
move_probs = []


def run_sim():
    game_state = ttt.get_starting_state()
    moves = []
    move_probs = []
    while (True):
        move = mcts1.mcts_search(game_state)
        moves.append(move)
        move_probs.append([mcts1.get_move_probs()])
        game_state = ttt.make_move(game_state, move)
        # ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            return ttt.reward(game_state, Player.CROSS), moves, move_probs
        move = mcts2.mcts_search(game_state)
        move_probs.append([mcts2.get_move_probs()])
        moves.append(move)
        game_state = ttt.make_move(game_state, move)
        # ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            return ttt.reward(game_state, Player.CROSS), moves, move_probs


def main():
    # start game
    os.system("clear")
    lost_game_moves = []
    lost_game_probs = []
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
    for _ in tqdm(range(50)):
        val, moves, move_probs = run_sim()
        outcomes.append(val)
        if val != 0:
            lost_game_moves.append(moves)
            lost_game_probs.append(move_probs)

    with open("log.txt", 'w') as f:
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
