from n_puzzle import Npuzzle
from utils.search.iterative_dfs import iterative_deepening_search
from utils.search.A_star import astar
from math import sqrt

if __name__ == '__main__':
    n = 1
    while not (sqrt(n+1).is_integer() or n > 7):
        n = int(input("Choose the size of the puzzle {8, 15, 24, ...} > 7 \n"))

    puz = Npuzzle(n)
    print(puz)
    print("Searching a solution ... \n")
    # moves = iterative_deepening_search(puz) not effective
    moves = astar(puz)
    puz.run(moves)
