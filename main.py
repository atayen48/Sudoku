from sudoku import Sudoku
puzzle = Sudoku(4).difficulty(0.5)
puzzle.show()

solution = puzzle.solve()
solution.show()
