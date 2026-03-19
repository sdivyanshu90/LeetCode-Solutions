from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1, str2 = "", ""
        for i in word1:
            str1 += i
        for i in word2:
            str2 += i
        return str1 == str2

def test_array_strings_are_equal():
    solution = Solution()

    # Test case 1
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(solution.arrayStringsAreEqual(word1, word2))  # Expected output: True

    # Test case 2
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(solution.arrayStringsAreEqual(word1, word2))  # Expected output: False

    # Test case 3
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(solution.arrayStringsAreEqual(word1, word2))  # Expected output: True

    # Test case 4
    word1 = ["a", "b", "c"]
    word2 = ["a", "b", "c"]
    print(solution.arrayStringsAreEqual(word1, word2))  # Expected output: True

    # Test case 5
    word1 = ["abc"]
    word2 = ["a", "b", "c"]
    print(solution.arrayStringsAreEqual(word1, word2))  # Expected output: True

test_array_strings_are_equal()