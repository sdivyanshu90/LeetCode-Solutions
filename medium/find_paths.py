class Solution(object):
    def findPaths(self, m, n, N, x, y):
        M = 1000000000 + 7
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(2)]
        for moves in range(N):
            for i in range(m):
                for j in range(n):
                    dp[(moves + 1) % 2][i][j] = (((1 if (i == 0) else dp[moves % 2][i - 1][j]) + \
                                                  (1 if (i == m - 1) else dp[moves % 2][i + 1][j])) % M + \
                                                 ((1 if (j == 0) else dp[moves % 2][i][j - 1]) + \
                                                  (1 if (j == n - 1) else dp[moves % 2][i][j + 1])) % M) % M
        return dp[N % 2][x][y]

def test_find_paths():
    s = Solution()

    # Test case 1
    m1, n1, N1, x1, y1 = 2, 2, 2, 0, 0
    print(s.findPaths(m1, n1, N1, x1, y1)) # Expected output: 6

    # Test case 2
    m2, n2, N2, x2, y2 = 1, 3, 3, 0, 1
    print(s.findPaths(m2, n2, N2, x2, y2)) # Expected output: 12

    # Test case 3
    m3, n3, N3, x3, y3 = 3, 3, 2, 1, 1
    print(s.findPaths(m3, n3, N3, x3, y3)) # Expected output: 4

    # Test case 4
    m4, n4, N4, x4, y4 = 8, 7, 16, 1, 5
    print(s.findPaths(m4, n4, N4, x4, y4)) # Expected output: 102984580

    # Test case 5
    m5, n5, N5, x5, y5 = 10, 10, 20, 5, 5
    print(s.findPaths(m5, n5, N5, x5, y5)) # Expected output: 277211170

test_find_paths()