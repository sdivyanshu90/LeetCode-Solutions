from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        split_text = text.split(" ")

        for i in range(len(split_text) - 2):
            if split_text[i] == first and split_text[i + 1] == second:
                res.append(split_text[i + 2])
        return res

def test_find_occurences():
    solution = Solution()

    # Test case 1
    text1 = "alice is a good girl she is a good student"
    first1 = "a"
    second1 = "good"
    print(solution.findOcurrences(text1, first1, second1))  # Expected output: ["girl", "student"]

    # Test case 2
    text2 = "we will we will rock you"
    first2 = "we"
    second2 = "will"
    print(solution.findOcurrences(text2, first2, second2))  # Expected output: ["we", "rock"]

    # Test case 3
    text3 = "the quick brown fox jumps over the lazy dog"
    first3 = "the"
    second3 = "quick"
    print(solution.findOcurrences(text3, first3, second3))  # Expected output: ["brown"]

    # Test case 4
    text4 = "a b a b a b a b"
    first4 = "a"
    second4 = "b"
    print(solution.findOcurrences(text4, first4, second4))  # Expected output: ["a", "a", "a"]

    # Test case 5
    text5 = "hello world"
    first5 = "world"
    second5 = "hello"
    print(solution.findOcurrences(text5, first5, second5))  # Expected output: []

test_find_occurences()