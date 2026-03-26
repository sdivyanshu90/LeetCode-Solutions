class Solution:
    def countHomogenous(self, s: str) -> int:
        blocks = []
        prev = s[0]
        cnt = 0
        result = 0
        for c in s:
            if c == prev:
                cnt += 1
            else:
                result += comb(cnt + 1, 2)
                cnt = 1
            prev = c
        result += comb(cnt + 1, 2)
        return result % (10 ** 9 + 7)

def test_count_homogenous():
    solution = Solution()

    # Test Case 1
    s1 = "abbcccaa"
    print(solution.countHomogenous(s1)) # Expected Output: 13

    # Test Case 2
    s2 = "xy"
    print(solution.countHomogenous(s2)) # Expected Output: 2

    # Test Case 3
    s3 = "zzzzz"
    print(solution.countHomogenous(s3)) # Expected Output: 15

    # Test Case 4
    s4 = "abcde"
    print(solution.countHomogenous(s4)) # Expected Output: 5

    # Test Case 5
    s5 = "aabbccdd"
    print(solution.countHomogenous(s5)) # Expected Output: 12

test_count_homogenous()