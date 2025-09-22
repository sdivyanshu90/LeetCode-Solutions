class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        freq = {}
        i = 0
        for j in range(n):
            if s[j] in freq:
                i = max(freq[s[j]], i)
            ans = max(ans, j - i + 1)
            freq[s[j]] = j + 1
        return ans


# Test Cases
def test_length_of_longest_substring():
    solution = Solution()

    # Test Case 1: Normal string with repeats
    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 3 ("abc")

    # Test Case 2: All unique characters
    s = "abcdef"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 6 ("abcdef")

    # Test Case 3: All same characters
    s = "aaaaaa"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 1 ("a")

    # Test Case 4: Empty string
    s = ""
    print(solution.lengthOfLongestSubstring(s))  # Expected: 0

    # Test Case 5: String with spaces and symbols
    s = "a b c!@#"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 8 (all characters unique)

    # Test Case 6: Numbers and letters
    s = "a1b2c3d4"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 8

    # Test Case 7: Repeats after a long unique sequence
    s = "abcddefgh"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 5 ("defgh")

    # Test Case 8: Long repeat in middle
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 3 ("wke")

    # Test Case 9: Long string with mixed characters
    s = "LeetCode"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 5 ("LeetC" or "eetCo" or "etCod" or "tCode")

    # Test Case 10: Substring at the end
    s = "abba"
    print(solution.lengthOfLongestSubstring(s))  # Expected: 2 ("ab" or "ba")


# Run all test cases
test_length_of_longest_substring()