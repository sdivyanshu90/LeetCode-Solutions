from collections import Counter
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        return Counter([word for word in words if word not in banned]).most_common(1)[0][0]

def test_most_common_word():
    solution = Solution()

    # Test Case 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(solution.mostCommonWord(paragraph1, banned1)) # Expected: "ball"

    # Test Case 2
    paragraph2 = "a."
    banned2 = []
    print(solution.mostCommonWord(paragraph2, banned2)) # Expected: "a"

    # Test Case 3
    paragraph3 = "Bob. hIt, baLl"
    banned3 = ["bob", "hit"]
    print(solution.mostCommonWord(paragraph3, banned3)) # Expected: "ball"

    # Test Case 4
    paragraph4 = "It was the best of times, it was the worst of times."
    banned4 = ["it", "was", "the"]
    print(solution.mostCommonWord(paragraph4, banned4)) # Expected: "of"

    # Test Case 5
    paragraph5 = "Hello hello HELLO"
    banned5 = ["allo"]
    print(solution.mostCommonWord(paragraph5, banned5)) # Expected: "hello"

test_most_common_word()