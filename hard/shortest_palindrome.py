from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_string = s[::-1]
        combined_string = s + "#" + reversed_string
        prefix_table = self._build_prefix_table(combined_string)
        palindrome_length = prefix_table[-1]
        suffix = reversed_string[: len(s) - palindrome_length]
        return suffix + s

    def _build_prefix_table(self, s: str) -> list:
        prefix_table = [0] * len(s)
        length = 0

        for i in range(1, len(s)):
            while length > 0 and s[i] != s[length]:
                length = prefix_table[length - 1]
            if s[i] == s[length]:
                length += 1
            prefix_table[i] = length
        return prefix_table
        
def test_shortest_palindrome():
    s = Solution()

    # Test Case 1: A string that is already a palindrome
    string = "racecar"
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'racecar'

    # Test Case 2: A simple non-palindrome
    string = "abcd"
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'dcbabcd'

    # Test Case 3: Empty string (edge case)
    string = ""
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: ''

    # Test Case 4: Single character string (edge case)
    string = "a"
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'a'

    # Test Case 5: A string with a non-trivial palindromic prefix
    string = "abacabad"
    # Longest palindromic prefix is "abacaba". Need to prepend reverse of "d".
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'dabacabad'

    # Test Case 6: A string that requires prepending most of its reverse
    string = "google"
    # Longest palindromic prefix is "g". Need to prepend reverse of "oogle".
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'elgoogle'
    
    # Test Case 7: String with alternating characters
    string = "abab"
    # Longest palindromic prefix is "aba". Need to prepend reverse of "b".
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'babab'

    # Test Case 8: Another standard non-palindrome example
    string = "aacecaaa"
    # Longest palindromic prefix is "aacecaa". Need to prepend reverse of "a".
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'aaacecaaa'

    # Test Case 9: All characters are the same (already a palindrome)
    string = "bbbbb"
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'bbbbb'

    # Test Case 10: A case with a palindrome in the middle
    string = "adcba"
    # Longest palindromic prefix is "a". Need to prepend reverse of "dcba".
    print(f"\nInput: '{string}'")
    print(f"Output: '{s.shortestPalindrome(string)}'") # Expected: 'abcdadcba'
    
test_shortest_palindrome()