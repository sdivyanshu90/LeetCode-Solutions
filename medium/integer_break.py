class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)

        for i in [1, 2, 3]:
            dp[i] = i
            
        for num in range(4, n + 1):
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp[num - i])
            
            dp[num] = ans
        
        return dp[n]

def test_integer_break():
    s = Solution()

    # Test Case 1: Example with n = 2
    n = 2
    print(s.integerBreak(n))  # Expected: 1

    # Test Case 2: Example with n = 10
    n = 10
    print(s.integerBreak(n))  # Expected: 36

    # Test Case 3: Edge case with n = 3
    n = 3
    print(s.integerBreak(n))  # Expected: 2

    # Test Case 4: Larger n
    n = 15
    print(s.integerBreak(n))  # Expected: 243

    # Test Case 5: n = 8
    n = 8
    print(s.integerBreak(n))  # Expected: 18

    # Test Case 6: n = 5
    n = 5
    print(s.integerBreak(n))  # Expected: 6

    # Test Case 7: n = 20
    n = 20
    print(s.integerBreak(n))  # Expected: 1458

    # Test Case 8: n = 4
    n = 4
    print(s.integerBreak(n))  # Expected: 4

    # Test Case 9: n = 6
    n = 6
    print(s.integerBreak(n))  # Expected: 9

    # Test Case 10: n = 7
    n = 7
    print(s.integerBreak(n))  # Expected: 12

test_integer_break()