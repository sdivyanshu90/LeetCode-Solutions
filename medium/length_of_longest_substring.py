class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        freq = {}
        i = 0
        for j in range(n):
            if s[j] in freq:
                i = max(freq[s[j]], i)
            
            ans = max(ans, j - i + 1)
            freq[s[j]] = j + 1

        return ans