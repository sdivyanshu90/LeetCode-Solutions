class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])

def test_count_palindromic_subsequence():
    solution = Solution()

    # Test case 1
    s1 = "aabca"
    print(solution.countPalindromicSubsequence(s1))  # Expected output: 3

    # Test case 2
    s2 = "adc"
    print(solution.countPalindromicSubsequence(s2))  # Expected output: 0

    # Test case 3
    s3 = "bbcbaba"
    print(solution.countPalindromicSubsequence(s3))  # Expected output: 4

    # Test case 4
    s4 = "aaaaa"
    print(solution.countPalindromicSubsequence(s4))  # Expected output: 0

    # Test case 5
    s5 = "abcba"
    print(solution.countPalindromicSubsequence(s5))  # Expected output: 2

test_count_palindromic_subsequence()