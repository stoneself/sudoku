# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# general note:
# 1) remember that list, array behaviors are happening with zero indexing

import inspect
import math


class Square:
    # zero indexing
    # TODO: should check input?
    def selectSquareInGrid(self, grid, x, y):
        # y is rows
        for i in range(0 + (y*3), 3 + (y*3)):
            # x is cols
            for j in range(0 + (x*3), 3 + (x*3)):
                self.square.append(grid[i * 9 + j])

    def print(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.square[i * 3 + j], end=" ")
            print()

    def __init__(self, grid, x, y):
        self.square = []
        self.selectSquareInGrid(grid, x, y)


class Row:
    # TODO: i feel bad about using row twice
    def selectRowInGrid(self, grid, row):
        for j in range(0, 9):
            self.row.append(grid[row * 9 + j])

    def print(self):
        for j in range(0, 9):
            print(self.row[j])

    def __init__(self, grid, row):
        self.row = []
        self.selectRowInGrid(grid, row)
        return


class Col:
    # TODO: i feel bad about using col twice
    def selectColInGrid(self, grid, col):
        for i in range(0, 9):
            self.col.append(grid[i * 9 + col])

    def print(self):
        for j in range(0, 9):
            print(self.col[j])

    def __init__(self, grid, col):
        self.col = []
        self.selectColInGrid(grid, col)
        return

class Grid:
    def createUnsolvedGrid(self):
        # zero INDEXing, but using 1, 9
        self.grid = [list(range(1, 10)) for i in range(0, 9) for j in range(0, 9)]

    def setCell(self, x, y, numList):
        self.grid[x * 9 + y] = numList
        return

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
    obsolete = False
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
    obsolete = False
    if obsolete == True:
        print(getFuncName(), "is obsolete")
        return

    testGrid = Grid()

    '''
    for i in range(0, 81):
        testGrid.setCell(i//9, i%9, [i])
    '''
    testGrid.print()

    testSquare = Square(testGrid.grid, 0, 1)
    testSquare.print()

    testRow = Row(testGrid.grid, 0)
    testRow.print()

    testCol = Col(testGrid.grid, 1)
    testCol.print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testCase0002()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# test case
