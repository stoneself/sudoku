# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# general note:
# 1) remember that list, array behaviors are happening with zero indexing

import inspect
import math

class Cell:
    def print(self):
        #return list of the three parts

    def isLegal(self):
        # if there is at least 1 number in the cell list

    def set(self, value):
        # check value-1 is not x
        # set all other member to x

    def remove(self, value):
        # check that this is not the last value
        # set value-1 to x

    def remainingClues(self):
        # return set conversion of cell

    def __init__(self):
        self.cell = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

class Square:
    def print(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.square[i * 3 + j], end=" ")
            print()

    def __init__(self, grid, x, y):
        self.square = grid.XYSquare(x, y)

class Row:
    def print(self):
        for j in range(0, 9):
            print(self.row[j])

    def __init__(self, grid, N):
        self.row = grid.NthRow(N)
        return

class Col:
    def print(self):
        for j in range(0, 9):
            print(self.col[j])

    def __init__(self, grid, N):
        self.col = grid.NthCol(N)

class Grid:
    def createUnsolvedGrid(self):
        # zero INDEXing, but using 1, 9
        self.grid = [list(range(1, 10)) for i in range(0, 9) for j in range(0, 9)]

    def setCell(self, x, y, num):
        self.grid[x * 9 + y]=["x"]*9
        self.grid[x * 9 + y][num-1]=num
        return

    def NthCol(self, N):
        col = []
        for i in range(0, 9):
            col.append(self.grid[i * 9 + N])
        return col

    def NthRow(self, N):
        row = []
        for j in range(0, 9):
            row.append(self.grid[N * 9 + j])
        return row

    def NthSquare(self, N):
        return

    # zero indexing
    # TODO: should check input?
    def XYSquare(self, x, y):
        square = []
        # y is rows
        for i in range(0 + (y * 3), 3 + (y * 3)):
            # x is cols
            for j in range(0 + (x * 3), 3 + (x * 3)):
                square.append(self.grid[i * 9 + j])
        return square

    # xero indexing
    def print(self):
        for i in range(0, 9):
            row1 = ""
            row2 = ""
            row3 = ""
            for j in range(0, 9):
                # TODO: construct the strings to print for the 3x3 set of values in a cell instead of printing
                # plain list of contents
                # print(self.grid[i * 9 + j], end=" ")
                for t in range(3):
                    row1 = row1 + " " + str(self.grid[i * 9 + j][t]) + " "
                    row2 = row2 + " " + str(self.grid[i * 9 + j][t+3]) + " "
                    row3 = row3 + " " + str(self.grid[i * 9 + j][t+6]) + " "
                    if t == 2:
                        row1 = row1 + " "
                        row2 = row2 + " "
                        row3 = row3 + " "
                if (j % 3) == 2:
                    row1 = row1 + " "
                    row2 = row2 + " "
                    row3 = row3 + " "
            print(row1)
            print(row2)
            print(row3)
            # print()
            if (i % 3) == 2:
                print()

    def __init__(self):
        self.grid = []
        self.createUnsolvedGrid()
        self.dimension = math.floor(math.sqrt(len(self.grid)))


class Solver(Grid):

    def findSoloNumbers(self):
        return

    def SoloInSquare(self, x, y):
        return

    def __init__(self, grid):
        self.grid = []
        self.createUnsolvedGrid()


    # TODO: check should return error if invalid state is reached? or do separate check?
    # if number is only in one Square, remove other numbers from Square
    def OnlyOccurrenceRow(grid, x, y):
        return


    def OnlyOccurrenceColumn(grid, x, y):
        return


    def OnlyOccurrenceSquare(grid, x, y):
        return


    # if number is only in two rows or column of a Square
    # use info against other Squares
    # if number only occurs in corresponding row/column of another Square,
    # remove number from third Square
    # test blame

    def Rows2of3(grid, x, y):
        return


    def Cols2of3(grid, x, y):
        return


    # if number is only in one row or column of a Square, remove from other Squares in that row or column
    def OnlyInOneRowInSquare(grid, x, y):
        return


    def OnlyInOneColumnInSquare(grid, x, y):
        return


    # first general ntuple checks (aka n of n in set) :
    # if n numbers occur only in n Squares of a set,
    # remove other number from those Squares
    def NOfNInSquare(grid, x, y):
        return


    def NOfNInRow(grid, x, y):
        return


    def NOfNInCol(grid, x, y):
        return


    # second general ntuple check (aka bare n in n Squares):
    # if n numbers occur only in n Squares of a set by with no other numbers in those Squares,
    # remove those numbers from other Squares
    def BareNOfNinSquare(grid, x, y):
        return


    def BareNOfNInRow(grid, x, y):
        return


    def BareNOfNInCol(grid, x, y):
        return



# test cases
# need to make a test case harness module
# and separate test case file/module

# test case support functions
def getFuncName():
    return inspect.stack()[1][3]
    #i think look for this function name, then parent of


def testCase0001():
    print(getFuncName())
    obsolete = True
    if obsolete == True:
        print(getFuncName(), "is obsolete")
        return

    testGrid = Grid()
    testGrid.printGrid()

    testSquare = Square(testGrid.grid, 0, 1)
    testSquare.printSquare()

    for i in range(0, 81):
        testGrid.setSquare(i//9, i%9, [i])
    testGrid.printGrid()

    testSquare = Square(testGrid.grid, 0, 1)
    testSquare.printSquare()

def testCase0002():
    print(getFuncName())
    obsolete = True
    if obsolete == True:
        print(getFuncName(), "is obsolete")
        return

    testGrid = Grid()

    testGrid.print()

    testSquare = Square(testGrid.grid, 0, 1)
    testSquare.print()

    testRow = Row(testGrid.grid, 0)
    testRow.print()

    testCol = Col(testGrid.grid, 1)
    testCol.print()

def testCase0003():
    print(getFuncName())
    obsolete = True
    if obsolete == True:
        print(getFuncName(), "is obsolete")
        return

    testGrid = Grid()

    for x in range(9):
        for y in range(9):
            testGrid.setCell(x,y, x*y%9+1)

    testGrid.print()

def testCase0004():
    print(getFuncName())
    obsolete = False
    if obsolete == True:
        print(getFuncName(), "is obsolete")
        return

    testGrid = Grid()
    testGrid.print()

    testRow = Row(testGrid, 0)
    testRow.print()

    testCol = Col(testGrid, 1)
    testCol.print()

    testSquare = Square(testGrid, 1, 1)
    testSquare.print()

    for x in range(9):
        for y in range(9):
            testGrid.setCell(x,y, x*y%9+1)

    testGrid.print()

    testRow = Row(testGrid, 0)
    testRow.print()

    testCol = Col(testGrid, 1)
    testCol.print()

    testSquare = Square(testGrid, 1, 1)
    testSquare.print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testCase0004()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# test case
