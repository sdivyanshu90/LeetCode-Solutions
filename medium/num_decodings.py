class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i, c in enumerate(s, 1):
            if c != "0":
                dp[i] = dp[i - 1]
            if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

def test_num_decodings():
    solution = Solution()

    # Test Case 1
    print(solution.numDecodings("12")) # Output: 2

    # Test Case 2
    print(solution.numDecodings("226")) # Output: 3

    # Test Case 3
    print(solution.numDecodings("06")) # Output: 0

    # Test Case 4
    print(solution.numDecodings("10")) # Output: 1

    # Test Case 5
    print(solution.numDecodings("27")) # Output: 1

    # Test Case 6
    print(solution.numDecodings("11106")) # Output: 2

    # Test Case 7
    print(solution.numDecodings("0")) # Output: 0

    # Test Case 8
    print(solution.numDecodings("1")) # Output: 1

    # Test Case 9
    print(solution.numDecodings("101")) # Output: 1

    # Test Case 10
    print(solution.numDecodings("1001")) # Output: 0

test_num_decodings()    