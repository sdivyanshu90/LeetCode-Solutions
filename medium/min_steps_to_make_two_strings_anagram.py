class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0

        for char in set(t):
            diff = t.count(char) - s.count(char)
            res += diff if diff > 0 else 0
        
        return res

def test_minSteps():
    solution = Solution()

    # Test case 1
    s = "bab"
    t = "aba"
    expected = 1
    print(solution.minSteps(s, t))  # Expected Output: 1

    # Test case 2
    s = "leetcode"
    t = "practice"
    expected = 5
    print(solution.minSteps(s, t))  # Expected Output: 5

    # Test case 3
    s = "anagram"
    t = "mangaar"
    expected = 0
    print(solution.minSteps(s, t))  # Expected Output: 0

    # Test case 4
    s = "xxyyzz"
    t = "xxyyzz"
    expected = 0
    print(solution.minSteps(s, t))  # Expected Output: 0

    # Test case 5
    s = "friend"
    t = "family"
    expected = 4
    print(solution.minSteps(s, t))  # Expected Output: 4

test_minSteps()