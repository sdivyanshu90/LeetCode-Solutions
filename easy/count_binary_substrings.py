class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        res = 0
        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])

        return res

def test_count_binary_substrings():
    solution = Solution()

    # Test Case 1
    s1 = "00110011"
    print(solution.countBinarySubstrings(s1))  # Expected: 6

    # Test Case 2
    s2 = "10101"
    print(solution.countBinarySubstrings(s2))  # Expected: 4

    # Test Case 3
    s3 = "000111000"
    print(solution.countBinarySubstrings(s3))  # Expected: 6

    # Test Case 4
    s4 = "01"
    print(solution.countBinarySubstrings(s4))  # Expected: 1

    # Test Case 5
    s5 = "0000"
    print(solution.countBinarySubstrings(s5))  # Expected: 0

test_count_binary_substrings()