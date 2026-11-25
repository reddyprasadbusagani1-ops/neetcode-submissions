class Solution:
    def solveNQueens(self, n):
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diagonals = set()       # row - col
        anti_diagonals = set()  # row + col

        def backtrack(row):
            # All queens have been placed
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Check whether this position is safe
                if (col in cols or
                    (row - col) in diagonals or
                    (row + col) in anti_diagonals):
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack: remove queen
                board[row][col] = "."
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        backtrack(0)
        return result