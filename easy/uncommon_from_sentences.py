from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}
        for word in s1.split():
            count[word] = count.get(word, 0) + 1
        for word in s2.split():
            count[word] = count.get(word, 0) + 1

        return [word for word in count if count[word] == 1]

def test_uncommon_from_sentences():
    solution = Solution()

    # Test case 1
    s1_1 = "this apple is sweet"
    s2_1 = "this apple is sour"
    print(solution.uncommonFromSentences(s1_1, s2_1))  # Expected output: ["sweet", "sour"]

    # Test case 2
    s1_2 = "apple apple"
    s2_2 = "banana"
    print(solution.uncommonFromSentences(s1_2, s2_2))  # Expected output: ["banana"]

    # Test case 3
    s1_3 = "hello world"
    s2_3 = "hello leetcode"
    print(solution.uncommonFromSentences(s1_3, s2_3))  # Expected output: ["world", "leetcode"]

    # Test case 4
    s1_4 = "a b c d e"
    s2_4 = "e d c b a"
    print(solution.uncommonFromSentences(s1_4, s2_4))  # Expected output: []

    # Test case 5
    s1_5 = "one two three"
    s2_5 = "four five six"
    print(solution.uncommonFromSentences(s1_5, s2_5))  # Expected output: ["one", "two", "three", "four", "five", "six"]


test_uncommon_from_sentences()