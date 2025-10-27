class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0

        # Loop over characters in the string
        for c in s:
            # If set contains the character, match found
            if c in character_set:
                character_set.remove(c)
                # Add the two occurrences to our palindrome
                res += 2
            else:
                # Add the character to the set
                character_set.add(c)

        # If any character remains, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if character_set:
            res += 1

        return res

def test_longest_palindrome():
    s = Solution()

    # Test case 1
    print(s.longestPalindrome("abccccdd"))  # Expected output: 7

    # Test case 2
    print(s.longestPalindrome("a"))         # Expected output: 1

    # Test case 3
    print(s.longestPalindrome("bb"))        # Expected output: 2

    # Test case 4
    print(s.longestPalindrome("Aa"))        # Expected output: 1

    # Test case 5
    print(s.longestPalindrome("abc"))       # Expected output: 1

    # Test case 6
    print(s.longestPalindrome("ababa"))     # Expected output: 5

    # Test case 7
    print(s.longestPalindrome("ababbc"))    # Expected output: 5

    # Test case 8
    print(s.longestPalindrome("ccc"))       # Expected output: 3

    # Test case 9
    print(s.longestPalindrome("aabbccdde")) # Expected output: 9

    # Test case 10
    print(s.longestPalindrome("abcdabcd"))  # Expected output: 8

test_longest_palindrome()