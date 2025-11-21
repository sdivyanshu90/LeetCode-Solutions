class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            palindrome[i][i] = True
            ans += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = True
                ans += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
                    palindrome[i][i + length - 1] = True
                    ans += 1

        return ans


def test_count_substrings():
    s = Solution()

    # Test case 1
    string = "abc"
    print(s.countSubstrings(string))  # Expected output: 3

    # Test case 2
    string = "aaa"
    print(s.countSubstrings(string))  # Expected output: 6

    # Test case 3
    string = "ababa"
    print(s.countSubstrings(string))  # Expected output: 9

    # Test case 4
    string = "a"
    print(s.countSubstrings(string))  # Expected output: 1

    # Test case 5
    string = "racecar"
    print(s.countSubstrings(string))  # Expected output: 10

test_count_substrings()