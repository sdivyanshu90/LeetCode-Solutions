class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0

        for i in range(n):
            count_b[i] = b_count
            if s[i] == "b":
                b_count += 1
        a_count = 0
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1
        min_deletions = n
        for i in range(n):
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions

def test_minimum_deletions():
    solution = Solution()

    # Test case 1
    s1 = "aababbab"
    print(solution.minimumDeletions(s1))  # Expected output: 2

    # Test case 2
    s2 = "bbaaaaabb"
    print(solution.minimumDeletions(s2))  # Expected output: 2

    # Test case 3
    s3 = "ababab"
    print(solution.minimumDeletions(s3))  # Expected output: 2

    # Test case 4
    s4 = "aaaaa"
    print(solution.minimumDeletions(s4))  # Expected output: 0

    # Test case 5
    s5 = "bbbbb"
    print(solution.minimumDeletions(s5))  # Expected output: 0

test_minimum_deletions()