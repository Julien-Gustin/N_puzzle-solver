from n_puzzle import Npuzzle
from utils.search.iterative_dfs import iterative_deepening_search
from utils.search.A_star import astar
from math import sqrt
from time import time
import argparse

if __name__ == '__main__':
    n = 1
    while not (sqrt(n+1).is_integer() or n > 7):
        n = int(input("Choose the size of the puzzle {8, 15, 24, ...} > 7 \n"))

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--iterativedfs", action ="store_true", help="launch iterativedfs")
    parser.add_argument("-a", "--astar", action ="store_true", help="launch astar")
    parser.add_argument("-c", "--compare", action ="store_true", help="Compare both algorithm")

    puz = Npuzzle(n)
    print(puz)

    print("Searching for a solution ... (could take a while)\n")

    args = parser.parse_args()
    moves = []
    if args.iterativedfs or args.compare:
        start = time()
        moves = iterative_deepening_search(puz.clone()) #not effective
        end = time()
        print("Time : {}".format(end - start))
        puz.run(moves)

    if args.astar or args.compare:
        start = time()
        moves = astar(puz.clone()) #not effective
        end = time()

        print("Time : {}".format(end - start))
        puz.run(moves)


    if not (args.iterativedfs or args.compare or args.astar):
        print("Launch using python3 solver.py [-a] OR [-d] OR [-c]\n \t -a : using astar algorithm \n \t -d : using iterative dfs \n \t -c : compare both of them")
