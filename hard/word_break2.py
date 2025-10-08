from collections import defaultdict
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = defaultdict(list)

        def _wordBreak_topdown(s):
            if not s:
                return [[]]
            if s in memo:
                return memo[s]

            for endIndex in range(1, len(s) + 1):
                word = s[:endIndex]
                if word in wordSet:
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        _wordBreak_topdown(s)
        return [" ".join(words) for words in memo[s]]

def test_wordBreak():
    solution = Solution()
    # Test Case 1
    print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) 
    # Expected output: ["cats and dog", "cat sand dog"]

    # Test Case 2
    print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) 
    # Expected output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

    # Test Case 3
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) 
    # Expected output: []

    # Test Case 4
    print(solution.wordBreak("aaaaaaa", ["aaaa","aa","a"])) 
    # Expected output: ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","a a a aa a a","a a a a aa a","a a a a a aa","aa aa a a a","aa a aa a a","aa a a aa a","aa a a a aa","a aa aa a a","a aa a aa a","a aa a a aa","a a aa aa a","a a aa a aa","a a a aa aa","aa aa aa"]

    # Test Case 5
    print(solution.wordBreak("leetcode", ["leet", "code"])) 
    # Expected output: ["leet code"]

test_wordBreak()