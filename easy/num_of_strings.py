from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                count += 1
        return count

def test_num_of_strings():
    solution = Solution()

    # Test Case 1
    patterns1 = ["a", "abc", "bc", "d"]
    word1 = "abc"
    print(solution.numOfStrings(patterns1, word1))  # Expected output: 3

    # Test Case 2
    patterns2 = ["a", "b", "c"]
    word2 = "aaaaabbbbb"
    print(solution.numOfStrings(patterns2, word2))  # Expected output: 2

    # Test Case 3
    patterns3 = ["a", "a", "a"]
    word3 = "ab"
    print(solution.numOfStrings(patterns3, word3))  # Expected output: 3

    # Test Case 4
    patterns4 = ["a", "b", "c"]
    word4 = "def"
    print(solution.numOfStrings(patterns4, word4))  # Expected output: 0

    # Test Case 5
    patterns5 = ["abc", "def", "ghi"]
    word5 = "abcdefghi"
    print(solution.numOfStrings(patterns5, word5))  # Expected output: 3

test_num_of_strings()