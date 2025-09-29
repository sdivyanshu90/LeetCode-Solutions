class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()
        return len(ans[len(ans)-1])

def test_length_of_last_word():
    solution = Solution()
    
    # Test case 1: Regular case with multiple words
    print(solution.lengthOfLastWord("Hello World"))
    
    # Test case 2: Single word
    print(solution.lengthOfLastWord("Python"))

    # Test case 3: Trailing spaces
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    
    # Test case 4: Only spaces
    print(solution.lengthOfLastWord("     "))

    # Test case 5: Empty string
    print(solution.lengthOfLastWord(""))

    # Test case 6: Single character word
    print(solution.lengthOfLastWord("a"))
    
    # Test case 7: Multiple spaces between words
    print(solution.lengthOfLastWord("a b c d e f g"))
    
    # Test case 8: Long string with punctuation
    print(solution.lengthOfLastWord("Hello, how are you doing today?"))

    # Test case 9: String with newline characters
    print(solution.lengthOfLastWord("Hello\nWorld"))

    # Test case 10: String with tabs
    print(solution.lengthOfLastWord("Hello\tWorld"))

test_length_of_last_word()