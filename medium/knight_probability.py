class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1.0
        
        for step in range(k):
            new_dp = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dr, dc in directions:
                        r = i + dr
                        c = j + dc
                        
                        if 0 <= r < n and 0 <= c < n:
                            new_dp[r][c] += dp[i][j] / 8
            
            dp = new_dp
        total_probability = sum(sum(row) for row in dp)        
        return total_probability

def test_knight_probability():
    solution = Solution()

    # Test Case 1
    n1, k1, row1, column1 = 3, 2, 0, 0
    print(solution.knightProbability(n1, k1, row1, column1))  # Expected: 0.0625

    # Test Case 2
    n2, k2, row2, column2 = 1, 0, 0, 0
    print(solution.knightProbability(n2, k2, row2, column2))  # Expected: 1.0

    # Test Case 3
    n3, k3, row3, column3 = 4, 4, 0, 0
    print(solution.knightProbability(n3, k3, row3, column3))  # Expected: 0.015625

    # Test Case 4
    n4, k4, row4, column4 = 5, 3, 2, 2
    print(solution.knightProbability(n4, k4, row4, column4))  # Expected: 0.125

    # Test Case 5
    n5, k5, row5, column5 = 8, 30, 6, 4
    print(solution.knightProbability(n5, k5, row5, column5))  # Expected: A small probability value

test_knight_probability()