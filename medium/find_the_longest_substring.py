class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        return longestSubstring

def test_findTheLongestSubstring():
    solution = Solution()

    # Test case 1
    s1 = "eleetminicoworoep"
    print(solution.findTheLongestSubstring(s1)) # Expected output: 13

    # Test case 2
    s2 = "leetcodeisgreat"
    print(solution.findTheLongestSubstring(s2)) # Expected output: 5

    # Test case 3
    s3 = "bcbcbc"
    print(solution.findTheLongestSubstring(s3)) # Expected output: 6

    # Test case 4
    s4 = "aeiou"
    print(solution.findTheLongestSubstring(s4)) # Expected output: 0

    # Test case 5
    s5 = "abcdeiouxyz"
    print(solution.findTheLongestSubstring(s5)) # Expected output: 6

test_findTheLongestSubstring()