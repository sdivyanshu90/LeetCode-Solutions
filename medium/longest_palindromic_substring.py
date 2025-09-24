class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""

def test_longest_palindrome():
    solution = Solution()

    # Test Case 1: Normal case with odd-length palindrome
    s = "babad"
    print(solution.longestPalindrome(s))  # Expected: "bab" or "aba"

    # Test Case 2: Normal case with even-length palindrome
    s = "cbbd"
    print(solution.longestPalindrome(s))  # Expected: "bb"

    # Test Case 3: Single character string
    s = "a"
    print(solution.longestPalindrome(s))  # Expected: "a"

    # Test Case 4: Empty string
    s = ""
    print(solution.longestPalindrome(s))  # Expected: ""

    # Test Case 5: All characters the same
    s = "aaaaaa"
    print(solution.longestPalindrome(s))  # Expected: "aaaaaa"

    # Test Case 6: No palindrome longer than 1
    s = "abcde"
    print(solution.longestPalindrome(s))  # Expected: "a" or "b" or "c" or "d" or "e"

    # Test Case 7: Palindrome at the start
    s = "racecarxyz"
    print(solution.longestPalindrome(s))  # Expected: "racecar" 
    # Test Case 8: Palindrome at the end
    s = "xyzracecar"
    print(solution.longestPalindrome(s))  # Expected: "racecar"
    # Test Case 9: Entire string is a palindrome
    s = "madam"
    print(solution.longestPalindrome(s))  # Expected: "madam"
    # Test Case 10: Mixed characters with special characters
    s = "Hannah"
    print(solution.longestPalindrome(s))  # Expected: "Hannah"