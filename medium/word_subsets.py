from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in words1:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans

def test_word_subsets():
    solution = Solution()

    # Test Case 1
    print(solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"])) # Expected: ["facebook","google","leetcode"]

    # Test Case 2
    print(solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"])) # Expected: ["apple","google","leetcode"]

    # Test Case 3
    print(solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","oo"])) # Expected: ["facebook","google"]

    # Test Case 4
    print(solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])) # Expected: ["google","leetcode"]

    # Test Case 5
    print(solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["ec","oc","ce"])) # Expected: ["facebook","leetcode"]

test_word_subsets()