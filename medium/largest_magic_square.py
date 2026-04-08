from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_pref = [[0] * (cols + 1) for _ in range(rows)]
        col_pref = [[0] * (cols) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                row_pref[r][c+1] = row_pref[r][c] + grid[r][c]
                col_pref[r+1][c] = col_pref[r][c] + grid[r][c]

        for k in range(min(rows, cols), 1, -1):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    target = row_pref[r][c+k] - row_pref[r][c]
                    match = True
                    for i in range(k):
                        if (row_pref[r+i][c+k] - row_pref[r+i][c]) != target:
                            match = False; break
                    if not match: continue

                    for j in range(k):
                        if (col_pref[r+k][c+j] - col_pref[r][c+j]) != target:
                            match = False; break
                    if not match: continue
                    d1 = 0
                    d2 = 0
                    for i in range(k):
                        d1 += grid[r+i][c+i]
                        d2 += grid[r+i][c+k-1-i]
                    if d1 == target and d2 == target:
                        return k

        return 1

def test_largest_magic_square():
    solution = Solution()

    # Test case 1
    grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
    print(solution.largestMagicSquare(grid))  # Expected output: 3

    # Test case 2
    grid = [[5,1,3],[9,3,1],[1,3,9]]
    print(solution.largestMagicSquare(grid))  # Expected output: 1

    # Test case 3
    grid = [[1]]
    print(solution.largestMagicSquare(grid))  # Expected output: 1

    # Test case 4
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.largestMagicSquare(grid))  # Expected output: 1

    # Test case 5
    grid = [[3,10,5,1],[3,2,4,5],[3,15,6,7],[3,2,4,5]]
    print(solution.largestMagicSquare(grid))  # Expected output: 1

test_largest_magic_square()