class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]

        for i in range(1, m):
            for j in range(n):
                for k in range(j+1, n):
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if 0 <= j+x < n and 0 <= k+y < n:
                                prev = dp[i-1][j+x][k+y]
                                if prev != -1:
                                    dp[i][j][k] = max(dp[i][j][k], prev + grid[i][j] + (grid[i][k] if j != k else 0))

        ans = max(max(row) for row in dp[m-1])
        return ans if ans != -1 else 0

def test_cherry_pickup():
    solution = Solution()

    # Test case 1
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(solution.cherryPickup(grid))  # Expected output: 24

    # Test case 2
    grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
    print(solution.cherryPickup(grid)) # Expected output: 10

    # Test case 3
    grid = [[1, 0, 0, 3], [1, 0, 0, 0], [1, 9, 0, 0], [0, 0, 0, 0]]
    print(solution.cherryPickup(grid))  # Expected output: 13

    # Test case 4
    grid = [[1, 1], [1, 1]]
    print(solution.cherryPickup(grid))  # Expected output: 4

    # Test case 5
    grid = [[0]]
    print(solution.cherryPickup(grid))  # Expected output: 0

test_cherry_pickup()