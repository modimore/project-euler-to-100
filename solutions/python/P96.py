"""Project Euler Solutions
Problem 96: Su Doku
Solved by: Quinn Mortimer (modimore)
"""
from itertools import chain, product

class SudokuException(Exception):
    pass

class SudokuSquare:
    def __init__(self, value):
        if value not in range(1, 10):
            value = None
        if value is None:
            self.possible = set(range(1, 10))
        else:
            self.possible = {value}
        self.value = value
    
    def __str__(self):
        return "." if self.value is None else str(self.value)
    
    @property
    def solved(self):
        return self.value is not None
    
    @property
    def unsolveable(self):
        return self.value is None and len(self.possible) == 0
    
    def remove(self, values):
        if self.solved:
            return False
        removed = self.possible & values
        if len(removed) > 0:
            self.possible -= removed
        if len(self.possible) == 1:
            self.value = next(iter(self.possible))
        return len(removed) > 0
    
    def set(self, value):
        self.value = value
        self.possible = {value}

class SudokuSquareLookup:
    def __init__(self, board, i, j):
        self._board = board
        self._i = i
        self._j = j
    
    @property
    def _square(self):
        return self._board._board[self._j][self._i]
    
    @property
    def possible(self):
        return self._square.possible
    
    @property
    def solved(self):
        return self._square.solved
    
    @property
    def value(self):
        return self._square.value
    
    def set(self, value):
        return self._square.set(value)

class SudokuBoard:
    def __init__(self, data):
        self.data = data
        
        self.board = [[SudokuSquareLookup(self, i, j) for i in range(9)] for j in range(9)]
        self.groups = [[[] for i in range(9)] for j in range(9)]
        for j in range(9):
            row = [SudokuSquareLookup(self, i, j) for i in range(9)]
            for i in range(9):
                self.groups[j][i].append(row)
        for i in range(9):
            column = [SudokuSquareLookup(self, i, j) for j in range(9)]
            for j in range(9):
                self.groups[j][i].append(column)
        for ii, jj in product(range(0, 9, 3), range(0, 9, 3)):
            cell = [SudokuSquareLookup(self, ii+i, jj+j) for i, j in product(range(3), range(3))]
            for i, j in product(range(3), range(3)):
                self.groups[jj+j][ii+i].append(cell)
    
    def __str__(self):
        return "\n".join(" ".join(str(v) for v in row) for row in self._board)
    
    @property
    def data(self):
        return [[sq.value for sq in row] for row in self._board]
    
    @data.setter
    def data(self, data):
        board = [
            [SudokuSquare(v) for v in row]
            for row in data
        ]
        self._board = board
    
    @data.deleter
    def data(self):
        self._board = None
    
    @property
    def solved(self):
        return all(sq.solved for sq in chain(*self._board))
    
    def guess(self):
        data = self.data
        unsolved = iter(sorted((sq for sq in chain(*self.board) if not sq.solved),
                key=lambda sq: len(sq.possible)))
        sq = next(unsolved)
        
        for guess in sq.possible:
            sq.set(guess)
            
            solved = self.reduce()
            if solved:
                return True
            
            if any(sq.unsolveable for sq in chain(*self._board)):
                self.data = data
                self.reduce()
                continue
            
            solved = self.guess()
            if solved:
                return True
            
            self.data = data
            self.reduce()
        
        return False
    
    def reduce(self):
        while True:
            changed = False
            for i, j in product(range(9), range(9)):
                sq = self._board[j][i]
                if sq.solved:
                    continue
                
                groups = self.groups[j][i]
                values = {sq.value for sq in chain(*[
                    group for group in groups]) if sq.solved}
                changed = sq.remove(values) or changed
            if not changed:
                break
        return self.solved
    
    def solve(self):
        solved = self.reduce()
        if not solved:
            solved = self.guess()
            if not solved:
                raise SudokuException("Could not solve")

if __name__ == "__main__":
    boards = []
    with open("P96_Input.txt") as f:
        l = f.readline()
        while l != "":
            data = [map(int, f.readline().strip())
                for i in range(9)]
            boards.append(SudokuBoard(data))
            l = f.readline()
    result = 0
    for i, board in enumerate(boards):
        print("Board #", i+1)
        print(board)
        board.solve()
        print("+" * 17)
        print(board)
        vals = board.data[0][0:3]
        result += vals[0] * 100 + vals[1] * 10 + vals[2]
    print("Solution:", result)

