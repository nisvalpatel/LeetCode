# Last updated: 7/10/2025, 11:58:22 AM
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 1) Make solutions an instance variable and clear it each call
        self.solutions = []

        # initialize empty board
        board = [['.' for _ in range(n)] for _ in range(n)]

        def is_valid(board, row, col):
            # 2) Only check *to the left* of (row, col)

            # -- check same row to the left
            for c in range(col):
                if board[row][c] == 'Q':
                    return False

            # -- check up-left diagonal
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            # -- check down-left diagonal
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1

            return True

        def backtrack(col):
            # base case: placed in all columns
            if col == n:
                # record a deep copy of the board
                self.solutions.append([''.join(r) for r in board])
                return

            for row in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(col + 1)
                    board[row][col] = '.'  # undo

        # kick off recursion in column zero
        backtrack(0)
        return self.solutions
