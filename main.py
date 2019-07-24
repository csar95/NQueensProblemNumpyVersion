from exceptions import *
from board import *
from game import *
import time
import numpy as np


try:
    n = int(input("Write a number greater than 3 to be the board dimension and press (Enter)\n"))
    if n < 4:
        raise LessThanFourError(n)

except ValueError as err:
    exit("The value must be an integer.")
except LessThanFourError as err:
    exit(str(err))


strg = input("Type a solution for the {}-queens problem and press (Enter)\n".format(n))

try:
    solution = np.fromiter(map(int, strg.split(' ')), dtype=int)

    if solution.size != n:
        raise IncorrectInputLengthError(n)

    if np.min(solution) < 0 or np.max(solution) > n:
        raise IncorrectInputError(n)

except IncorrectInputLengthError as err:
    exit(str(err))
except IncorrectInputError as err:
    exit(str(err))
except ValueError as err:
    exit("The characters in the solution must be integers between 0 and {}.".format(n))

# ----------------------------------------------------------------------------------------------------- #

board = Board(solution)

game = Game(board)

if board.is_full() and game.is_solution_correct():
    print("Provided solution is correct.")
elif board.is_full() and not game.is_solution_correct():
    print("Provided solution is not correct.")
else:
    # Board is not full yet
    start = time.time()
    game.find_solutions()
    end = time.time()
    print("Total number of solutions: {}".format(game.numberOfSolutions))
    print("Execution time: {} seconds".format(end - start))


# For the case: n = 18 | 2 5 7 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# Without numpy: 253.03 seconds | Solutions: 1426
# With numpy: 185.99 seconds | Solutions: 1426
