from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break

        return res

def test_string_matching():
    solution = Solution()

    # Test case 1
    words1 = ["mass", "as", "hero", "superhero"]
    print(solution.stringMatching(words1))  # Expected output: ["as", "hero"]

    # Test case 2
    words2 = ["leetcode", "et", "code"]
    print(solution.stringMatching(words2))  # Expected output: ["et", "code"]

    # Test case 3
    words3 = ["blue", "green", "bu"]
    print(solution.stringMatching(words3))  # Expected output: []

    # Test case 4
    words4 = ["a", "b", "c"]
    print(solution.stringMatching(words4))  # Expected output: []

    # Test case 5
    words5 = ["leetcoder", "leetcode", "od", "hamlet", "am"]
    print(solution.stringMatching(words5))  # Expected output: ["leetcode", "od", "am"]

test_string_matching()