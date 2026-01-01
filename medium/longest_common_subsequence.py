class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        lcs = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = 1 + lcs[i - 1][j - 1]

                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

        return lcs[m][n]

def test_longest_common_subsequence():
    solution = Solution()

    # Test case 1
    text1 = "abcde"
    text2 = "ace"
    print(solution.longestCommonSubsequence(text1, text2))  # Expected output: 3

    # Test case 2
    text1 = "abc"
    text2 = "abc"
    print(solution.longestCommonSubsequence(text1, text2))  # Expected output: 3

    # Test case 3
    text1 = "abc"
    text2 = "def"
    print(solution.longestCommonSubsequence(text1, text2))  # Expected output: 0

    # Test case 4
    text1 = "aggtab"
    text2 = "gxtxayb"
    print(solution.longestCommonSubsequence(text1, text2))  # Expected output: 4

    # Test case 5
    text1 = "aaaa"
    text2 = "aa"
    print(solution.longestCommonSubsequence(text1, text2))  # Expected output: 2

test_longest_common_subsequence()