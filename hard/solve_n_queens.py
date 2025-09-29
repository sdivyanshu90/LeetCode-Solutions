from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            return not (cols[col] or diag1[row + col] or diag2[row - col])

        def update_board(row, col, val):
            cols[col] = val
            diag1[row + col] = val
            diag2[row - col] = val

        def backtrack(row):
            if row == n:
                solutions.append([''.join(row) for row in board])
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    update_board(row, col, 1)

                    backtrack(row + 1)
                    board[row][col] = '.'
                    update_board(row, col, 0)

        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        cols = [0] * n
        diag1 = [0] * (2 * n - 1)
        diag2 = [0] * (2 * n - 1)

        backtrack(0)
        return solutions

def test_solve_n_queens():
    solution = Solution()
    
    # Test case 1: n = 4
    print(solution.solveNQueens(4))  # Expected output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    
    # Test case 2: n = 1
    print(solution.solveNQueens(1))  # Expected output: [["Q"]]

    # Test case 3: n = 2 (no solution)
    print(solution.solveNQueens(2))  # Expected output: []

    # Test case 4: n = 3 (no solution)
    print(solution.solveNQueens(3))  # Expected output: []

    # Test case 5: n = 5
    print(solution.solveNQueens(5))  # Expected output: Multiple valid configurations

    # Test case 6: n = 6
    print(solution.solveNQueens(6))  # Expected output: Multiple valid configurations

    # Test case 7: n = 8
    print(solution.solveNQueens(8))  # Expected output: Multiple valid configurations

    # Test case 8: n = 9
    print(solution.solveNQueens(9))  # Expected output: Multiple valid configurations

test_solve_n_queens()