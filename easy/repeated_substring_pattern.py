class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_string = s + s
        return s in new_string[1:-1]

def test_repeated_substring_pattern():
    s = Solution()

    # Test case 1
    string = "abab"
    print(s.repeatedSubstringPattern(string))  # Expected output: True

    # Test case 2
    string = "aba"
    print(s.repeatedSubstringPattern(string))  # Expected output: False

    # Test case 3
    string = "abcabcabcabc"
    print(s.repeatedSubstringPattern(string))  # Expected output: True

    # Test case 4
    string = "a"
    print(s.repeatedSubstringPattern(string))  # Expected output: False

    # Test case 5
    string = "zzzzzz"
    print(s.repeatedSubstringPattern(string))  # Expected output: True

test_repeated_substring_pattern()