from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]

def test_wordBreak():
    solution = Solution()
    # Test Case 1
    print(solution.wordBreak("leetcode", ["leet", "code"])) # Expected output: True

    # Test Case 2
    print(solution.wordBreak("applepenapple", ["apple", "pen"])) # Expected output: True

    # Test Case 3
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # Expected output: False

    # Test Case 4
    print(solution.wordBreak("aaaaaaa", ["aaaa","aa"])) # Expected output: False

    # Test Case 5
    print(solution.wordBreak("cars", ["car","ca","rs"])) # Expected output: True

test_wordBreak()