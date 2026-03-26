class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            char = s[l]
            l += 1
            r -= 1
            while l <= r and s[l] == char:
                l += 1
            while l <= r and s[r] == char:
                r -= 1
        
        return r - l + 1

def test_minimum_length():
    solution = Solution()

    # Test Case 1
    s1 = "ca"
    print(solution.minimumLength(s1)) # Expected Output: 2

    # Test Case 2
    s2 = "cabaabac"
    print(solution.minimumLength(s2)) # Expected Output: 0

    # Test Case 3
    s3 = "aabccabba"
    print(solution.minimumLength(s3)) # Expected Output: 3

    # Test Case 4
    s4 = "abcde"
    print(solution.minimumLength(s4)) # Expected Output: 5

    # Test Case 5
    s5 = "aaaaaa"
    print(solution.minimumLength(s5)) # Expected Output: 0

test_minimum_length()