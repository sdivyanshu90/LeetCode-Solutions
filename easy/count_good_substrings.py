class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        comb = []

        comb.append(s[:3])
        for i in range(1, len(s) - 2):
            comb.append(s[i:i + 3])

        res = 0
        for substr in comb:
            if len(substr) == len(set(substr)):
                res += 1

        return res

def test_count_good_substrings():
    solution = Solution()

    # Test case 1
    s1 = "xyzzaz"
    print(solution.countGoodSubstrings(s1))  # Expected output: 1

    # Test case 2
    s2 = "aababcabc"
    print(solution.countGoodSubstrings(s2))  # Expected output: 4

    # Test case 3
    s3 = "abc"
    print(solution.countGoodSubstrings(s3))  # Expected output: 1

    # Test case 4
    s4 = "aaa"
    print(solution.countGoodSubstrings(s4))  # Expected output: 0

    # Test case 5
    s5 = "abcdefg"
    print(solution.countGoodSubstrings(s5))  # Expected output: 5

test_count_good_substrings()