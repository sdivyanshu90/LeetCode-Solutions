class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]

        return dp[len(s)][len(p)]

def test_regex_matching():
    solution = Solution()

    # Test Case 1: Simple match without special characters
    s = "aa"
    p = "a"
    print(solution.isMatch(s, p))  # Expected output: False

    # Test Case 2: Simple match with '.'
    s = "aa"
    p = "a."
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 3: Match with '*'
    s = "ab"
    p = ".*"
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 4: Complex pattern with multiple '*' and '.'
    s = "aab"
    p = "c*a*b"
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 5: No match due to extra characters
    s = "mississippi"
    p = "mis*is*p*."
    print(solution.isMatch(s, p))  # Expected output: False

    # Test Case 6: Empty string and pattern
    s = "youarerejected"
    p = "youare.*jected"
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 7: Empty string with pattern that can match empty
    s = "thankyouforinterest"
    p = "t*.*rest"
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 8: Pattern with consecutive '*' characters
    s = "aaa"
    p = "a*a"
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 9: Pattern with '.' at the end
    s = "abc"
    p = "ab."
    print(solution.isMatch(s, p))  # Expected output: True

    # Test Case 10: Pattern that does not match due to character mismatch
    s = "abcd"
    p = "d*"
    print(solution.isMatch(s, p))  # Expected output: False

test_regex_matching()