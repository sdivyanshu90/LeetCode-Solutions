from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        score = (1 << (n - 1)) * m

        for j in range(1, n):
            count_same_bits = 0
            for i in range(m):
                if grid[i][j] == grid[i][0]:
                    count_same_bits += 1

            count_same_bits = max(count_same_bits, m - count_same_bits)
            column_score = (1 << (n - j - 1)) * count_same_bits
            score += column_score
        return score

def test_matrixScore():
    solution = Solution()
    
    # Test Case 1
    print(solution.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])) # Expected: 39

    # Test Case 2
    print(solution.matrixScore([[0]])) # Expected: 1

    # Test Case 3
    print(solution.matrixScore([[1]])) # Expected: 1

    # Test Case 4
    print(solution.matrixScore([[0,1],[1,1]])) # Expected: 5

    # Test Case 5
    print(solution.matrixScore([[0,0],[0,0]])) # Expected: 6

test_matrixScore()