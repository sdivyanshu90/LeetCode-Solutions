import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]

def test_num_squares():
    s = Solution()

    # Test Case 1: A number that is a perfect square itself.
    n = 16
    print(s.numSquares(n)) # Expected: 1

    # Test Case 2: A number that is a sum of two squares (e.g., 9 + 4).
    n = 13
    print(s.numSquares(n)) # Expected: 2

    # Test Case 3: A standard case requiring three squares (e.g., 4 + 4 + 4).
    n = 12
    print(s.numSquares(n)) # Expected: 3

    # Test Case 4: A number requiring four squares (Lagrange's four-square theorem).
    n = 7
    print(s.numSquares(n)) # Expected: 4

    # Test Case 5: The smallest possible input.
    n = 1
    print(s.numSquares(n)) # Expected: 1

    # Test Case 6: A sum of two squares (e.g., 25 + 1).
    n = 26
    print(s.numSquares(n)) # Expected: 2

    # Test Case 7: A larger number that is a sum of three squares (e.g., 9 + 9 + 9).
    n = 27
    print(s.numSquares(n)) # Expected: 3

    # Test Case 8: Another perfect square.
    n = 100
    print(s.numSquares(n)) # Expected: 1
    
    # Test Case 9: A number one less than a perfect square.
    n = 15
    print(s.numSquares(n)) # Expected: 4

    # Test Case 10: A number that can be formed by two equal squares (e.g., 25 + 25).
    n = 50
    print(s.numSquares(n)) # Expected: 2

test_num_squares()