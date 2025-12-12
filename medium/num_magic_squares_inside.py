from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        seen = [False] * 10
        for i in range(3):
            for j in range(3):
                num = grid[row + i][col + j]
                if num < 1 or num > 9:
                    return False
                if seen[num]:
                    return False
                seen[num] = True

        # Check if diagonal sums are the same
        diagonal1 = (
            grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
        )
        diagonal2 = (
            grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]
        )

        if diagonal1 != diagonal2:
            return False

        # Check if all row sums are the same as the diagonal sums
        row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
        row2 = (
            grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
        )
        row3 = (
            grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
        )

        if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
            return False

        # Check if all column sums are the same as the diagonal sums
        col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
        col2 = (
            grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
        )
        col3 = (
            grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
        )

        if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
            return False

        return True

def test_numMagicSquaresInside():
    solution = Solution()
    
    # Test Case 1
    print(solution.numMagicSquaresInside([[4,3,8,4],
                                          [9,5,1,9],
                                          [2,7,6,2]])) # Expected: 1

    # Test Case 2
    print(solution.numMagicSquaresInside([[8]])) # Expected: 0

    # Test Case 3
    print(solution.numMagicSquaresInside([[4,9,2,3,5],
                                          [3,5,7,8,1],
                                          [8,1,6,4,2],
                                          [1,7,4,9,6],
                                          [6,2,8,1,7]])) # Expected: 1

    # Test Case 4
    print(solution.numMagicSquaresInside([[10,3,5],
                                          [1,6,11],
                                          [7,9,2]])) # Expected: 0

    # Test Case 5
    print(solution.numMagicSquaresInside([[5,5,5],
                                          [5,5,5],
                                          [5,5,5]])) # Expected: 0

test_numMagicSquaresInside()