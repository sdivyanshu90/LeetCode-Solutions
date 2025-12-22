from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []

        for char in words[0]:
            if all(char in word for word in words[1:]):
                result.append(char)
                words = [word.replace(char, '', 1) for word in words]
        return result

def test_common_chars():
    solution = Solution()

    # Test case 1
    words1 = ["bella", "label", "roller"]
    print(solution.commonChars(words1))  # Expected output: ["e", "l", "l"]

    # Test case 2
    words2 = ["cool", "lock", "cook"]
    print(solution.commonChars(words2))  # Expected output: ["c", "o"]

    # Test case 3
    words3 = ["a", "b", "c"]
    print(solution.commonChars(words3))  # Expected output: []

    # Test case 4
    words4 = ["abca", "bcab", "cab"]
    print(solution.commonChars(words4))  # Expected output: ["a", "b", "c"]

    # Test case 5
    words5 = ["aaa", "aa", "aaaa"]
    print(solution.commonChars(words5))  # Expected output: ["a", "a"]

test_common_chars()