class Solution:
    def balancedStringSplit(self, s: str) -> int:
        temp = 0
        res = 0

        for i in range(len(s)):
            if s[i] == 'L':
                temp += 1
            else:
                temp -= 1
            if temp == 0:
                res += 1
        return res

def test_balanced_string_split():
    solution = Solution()

    # Test Case 1
    s1 = "RLRRLLRLRL"
    print(solution.balancedStringSplit(s1))  # Expected Output: 4

    # Test Case 2
    s2 = "RLLLLRRRLR"
    print(solution.balancedStringSplit(s2))  # Expected Output: 3

    # Test Case 3
    s3 = "LLLLRRRR"
    print(solution.balancedStringSplit(s3))  # Expected Output: 1

    # Test Case 4
    s4 = "RLRRRLLRLL"
    print(solution.balancedStringSplit(s4))  # Expected Output: 2

    # Test Case 5
    s5 = "LRLRLRLR"
    print(solution.balancedStringSplit(s5))  # Expected Output: 4

test_balanced_string_split()