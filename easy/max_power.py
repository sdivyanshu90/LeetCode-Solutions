class Solution:
    def maxPower(self, s: str) -> int:
        max_count = count = 0
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count

def test_max_power():
    solution = Solution()

    # Test case 1
    s1 = "leetcode"
    print(solution.maxPower(s1))  # Expected output: 2

    # Test case 2
    s2 = "abbcccddddeeeeedcba"
    print(solution.maxPower(s2))  # Expected output: 5

    # Test case 3
    s3 = "triplepillooooow"
    print(solution.maxPower(s3))  # Expected output: 5

    # Test case 4
    s4 = "hooraaaaaaaaaaay"
    print(solution.maxPower(s4))  # Expected output: 11

    # Test case 5
    s5 = "tourist"
    print(solution.maxPower(s5))  # Expected output: 1

test_max_power()