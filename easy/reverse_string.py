from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

def test_reverse_string():
    s = Solution()

    # Test Case 1: Example with simple string
    string_list = ["h","e","l","l","o"]
    s.reverseString(string_list)
    print(string_list)  # Expected: ["o","l","l","e","h"]

    # Test Case 2: Single character string
    string_list = ["a"]
    s.reverseString(string_list)
    print(string_list)  # Expected: ["a"]

    # Test Case 3: Empty string
    string_list = []
    s.reverseString(string_list)
    print(string_list)  # Expected: []

    # Test Case 4: Palindrome string
    string_list = ["r","a","c","e","c","a","r"]
    s.reverseString(string_list)
    print(string_list)  # Expected: ["r","a","c","e","c","a","r"]

    # Test Case 5: String with spaces
    string_list = [" ","h","e","l","l","o"," "]
    s.reverseString(string_list)
    print(string_list)  # Expected: [" ","o","l","l","e","h"," "]

    # Test Case 6: Long string
    string_list = list("abcdefghijklmnopqrstuvwxyz")
    s.reverseString(string_list)
    print(string_list)  # Expected: list of characters from 'z' to 'a'

    # Test Case 7: String with special characters
    string_list = ["!","@","#","$","%"]
    s.reverseString(string_list)
    print(string_list)  # Expected: ["%","$","#","@","!"]

    # Test Case 8: String with numbers
    string_list = ["1","2","3","4","5"]
    s.reverseString(string_list)
    print(string_list)  # Expected: ["5","4","3","2","1"]

    # Test Case 9: Mixed characters
    string_list = ["a","1","!","b","2","@"]
    s.reverseString(string_list)
    print(string_list)  # Expected: ["@","2","b","!","1","a"]

    # Test Case 10: Very long string
    string_list = list("a" * 10)
    s.reverseString(string_list)
    print(string_list)  # Expected: list of 10 "a" characters

test_reverse_string()