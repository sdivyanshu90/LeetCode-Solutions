class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i, j = 0, 0
        while i < n and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

def test_is_subsequence():
    solution = Solution()
    
    # Test case 1: s is a subsequence of t
    print(solution.isSubsequence("abc", "ahbgdc")) # Expected output: True
    
    # Test case 2: s is not a subsequence of t
    print(solution.isSubsequence("axc", "ahbgdc")) # Expected output: False

    # Test case 3: Edge case - empty s
    print(solution.isSubsequence("", "ahbgdc")) # Expected output: True

    # Test case 4: Edge case - empty t
    print(solution.isSubsequence("a", "")) # Expected output: False
    
    # Test case 5: s and t are the same
    print(solution.isSubsequence("leetcode", "leetcode")) # Expected output: True

    # Test case 6: s longer than t
    print(solution.isSubsequence("longstring", "short")) # Expected output: False

    # Test case 7: s is at the end of t
    print(solution.isSubsequence("def", "abcdef")) # Expected output: True

    # Test case 8: s is at the beginning of t
    print(solution.isSubsequence("abc", "abcdef")) # Expected output: True

    # Test case 9: s with repeated characters
    print(solution.isSubsequence("aa", "abacadae")) # Expected output: True

    # Test case 10: Large input where s is a subsequence of t
    large_s = "a" * 1000
    large_t = "a" * 10000
    print(solution.isSubsequence(large_s, large_t)) # Expected output: True

test_is_subsequence()