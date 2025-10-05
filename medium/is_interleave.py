class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        if m + n != len(s3):
            return False
        
        dp = [False] * (n + 1)
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[n]

def test_is_interleave():
    solution = Solution()

    # Test Case 1
    s1, s2, s3 = "aab", "axy", "aaxaby"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 2
    s1, s2, s3 = "aab", "axy", "abaaxy"
    print(solution.isInterleave(s1, s2, s3)) # Output: False

    # Test Case 3
    s1, s2, s3 = "", "", ""
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 4
    s1, s2, s3 = "abc", "def", "adbcef"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 5
    s1, s2, s3 = "abc", "def", "abdecf"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 6
    s1, s2, s3 = "a", "", "c"
    print(solution.isInterleave(s1, s2, s3)) # Output: False

    # Test Case 7
    s1, s2, s3 = "", "b", "b"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 8
    s1, s2, s3 = "a", "b", "ab"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 9
    s1, s2, s3 = "a", "b", "ba"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

    # Test Case 10
    s1, s2, s3 = "aa", "ab", "aaba"
    print(solution.isInterleave(s1, s2, s3)) # Output: True

test_is_interleave()