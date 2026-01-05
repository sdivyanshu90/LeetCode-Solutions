class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * 5 for _ in range(n)]        
        for i in range(5):
            dp[0][i] = 1
        
        for i in range(1, n):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % mod
            dp[i][3] = dp[i-1][2]
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % mod
        
        return sum(dp[n-1]) % mod

def test_count_vowel_permutation():
    solution = Solution()

    # Test Case 1
    n1 = 1
    print(solution.countVowelPermutation(n1))  # Expected Output: 5

    # Test Case 2
    n2 = 2
    print(solution.countVowelPermutation(n2))  # Expected Output: 10

    # Test Case 3
    n3 = 5
    print(solution.countVowelPermutation(n3))  # Expected Output: 68

    # Test Case 4
    n4 = 144
    print(solution.countVowelPermutation(n4))  # Expected Output: 18208803

    # Test Case 5
    n5 = 50
    print(solution.countVowelPermutation(n5))  # Expected Output: 564908303

test_count_vowel_permutation()