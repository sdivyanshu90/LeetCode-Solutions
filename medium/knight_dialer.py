class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        MOD = 10 ** 9 + 7
        dp = [0] * 10
        prev_dp = [1] * 10
        
        for remain in range(1, n):
            dp = [0] * 10
            for square in range(10):
                ans = 0
                for next_square in jumps[square]:
                    ans = (ans + prev_dp[next_square]) % MOD
                
                dp[square] = ans
                
            prev_dp = dp

        ans = 0
        for square in range(10):
            ans = (ans + prev_dp[square]) % MOD
        
        return ans

def test_knight_dialer():
    solution = Solution()

    # Test case 1
    n1 = 1
    print(solution.knightDialer(n1))  # Expected output: 10

    # Test case 2
    n2 = 2
    print(solution.knightDialer(n2))  # Expected output: 20

    # Test case 3
    n3 = 3
    print(solution.knightDialer(n3))  # Expected output: 46

    # Test case 4
    n4 = 4
    print(solution.knightDialer(n4))  # Expected output: 104

    # Test case 5
    n5 = 5
    print(solution.knightDialer(n5))  # Expected output: 240

test_knight_dialer()