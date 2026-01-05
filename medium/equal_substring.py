class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        max_len = 0
        start = 0
        curr_cost = 0
        
        for i in range(N):
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, i - start + 1)
        return max_len

def test_equal_substring():
    solution = Solution()

    # Test Case 1
    s1 = "abcd"
    t1 = "bcdf"
    maxCost1 = 3
    print(solution.equalSubstring(s1, t1, maxCost1))  # Expected Output: 3

    # Test Case 2
    s2 = "abcd"
    t2 = "cdef"
    maxCost2 = 3
    print(solution.equalSubstring(s2, t2, maxCost2))  # Expected Output: 1

    # Test Case 3
    s3 = "abcd"
    t3 = "acde"
    maxCost3 = 0
    print(solution.equalSubstring(s3, t3, maxCost3))  # Expected Output: 1

    # Test Case 4
    s4 = "krrgw"
    t4 = "zjxss"
    maxCost4 = 19
    print(solution.equalSubstring(s4, t4, maxCost4))  # Expected Output: 2

    # Test Case 5
    s5 = "anry"
    t5 = "mbeh"
    maxCost5 = 10
    print(solution.equalSubstring(s5, t5, maxCost5))  # Expected Output: 0

test_equal_substring()