import numpy as np
from math import sqrt
from random import shuffle
import time
import copy

class Npuzzle:
    def __init__(self, n):
        self.size = n+1
        self.pos, self.state = self.generatePuzzle() # and generate self.pos also

    def __repr__(self):
        strs = ""
        for rows in self.state:
            strs += str(rows)
            strs += "\n"

        strs += "\n"
        return strs


    ''' generate_puzzle

        @bref: generate a solvable puzzle of the N-puzzle
    '''
    def generatePuzzle(self):
        solvable = False
        puzzle = []
        x = int(sqrt(self.size))

        for i in range(1, self.size):
            puzzle.append(i)
        puzzle.append('x')

        while solvable is False:
            shuffle(puzzle)
            self.state = np.reshape(puzzle, (x, x))
            solvable = self.isSolvable()

        return self.pos, self.state

    ''' isSolvable

        @bref: verify if the current puzzle is solvable (self.state)

    '''
    def isSolvable(self):
        puzzle = self.state
        x = int(sqrt(self.size))
        N = 0

        for i in range(x):
            for j in range(x):
                N += self.computeInversions(puzzle, i, j)

        return bool(N%2)

    ''' SHOULD BE STATIC computeInversions
        @bref: compute 'inversion' of puzzle[i][j]

        @param puzzle: a matrix representing the puzzle
        @param i, j: matrix[i][j]
    '''
    def computeInversions(self, puzzle, i, j):
        x = int(sqrt(self.size))
        N = 0
        number = puzzle[i][j]
        if number == 1:
            return 0

        if number == 'x':
            self.pos = (i, j)

        while i < x:

            while j < x:
                if puzzle[i][j] < number:
                    N += 1
                j += 1

            j = 0
            i += 1

        return N

    def moveUp(self):
        matrix = self.state
        i = self.pos[0]
        j = self.pos[1]

        matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j]
        i, j = i-1, j
        self.pos = (i, j)


    def moveDown(self):
        matrix = self.state
        i = self.pos[0]
        j = self.pos[1]

        matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
        i, j = i+1, j
        self.pos = (i, j)

    def moveRight(self):
        matrix = self.state
        i = self.pos[0]
        j = self.pos[1]

        matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
        i, j = i, j+1
        self.pos = (i, j)

    def moveLeft(self):
        matrix = self.state
        i = self.pos[0]
        j = self.pos[1]

        matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]
        i, j = i, j-1
        self.pos = (i, j)

    def possibleAction(self, translated=False):
        i = self.pos[0]
        j = self.pos[1]
        action = []

        if i != 0:
            if translated:
                action.append("Up")

            else:
                action.append(self.moveUp)

        if i != int(sqrt(self.size))-1:
            if translated:
                action.append("Down")

            else:
                action.append(self.moveDown)

        if j != 0:
            if translated:
                action.append("Left")

            else:
                action.append(self.moveLeft)

        if j != int(sqrt(self.size))-1:
            if translated:
                action.append("Right")

            else:
                action.append(self.moveRight)

        return action

    def move(self, move):
        if move == "Down":
            self.moveDown()

        elif move == "Up":
            self.moveUp()

        elif move == "Right":
            self.moveRight()

        elif move == "Left":
            self.moveLeft()


    def isSolve(self):
        if self.state[0][0] != 'x':
            return False

        i = 0
        j = 1
        x = int(sqrt(self.size))
        prec = 0
        while i < x:
            while j < x:
                if int(self.state[i][j]) < prec:
                    return False

                prec = int(self.state[i][j])
                j += 1
            j = 0
            i += 1

        return True

    def clone(self):
        return copy.deepcopy(self)

    def equal(self, obj):
        if not isinstance(obj, Npuzzle):
            return False

        if self.size != obj.size:
            return False

        if self.pos[0] != obj.pos[0] or self.pos[1] != obj.pos[1]:
            return False

        i = 0
        x = int(sqrt(self.size))
        while i < x:
            j = 0
            while j < x:
                if obj.state[i][j] != self.state[i][j]:
                    return False

                j += 1

            i += 1

        return True

    def run(self, actions):
        print(actions)
        for action in actions:
            self.move(action)
            print(self)
            time.sleep(1)


    def h(self):
        x = int(sqrt(self.size))
        h = 0
        i = 0
        j = 0
        if self.state[0][0] != 'x':
            h += 1
        while i < x:
            while j < x:
                if self.state[i][j] != 'x' and int(self.state[i][j]) != ((i*x)+j):
                    h += 1
                j += 1
            i+=1
            j = 0

        return h
