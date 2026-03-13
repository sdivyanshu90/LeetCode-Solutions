class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, 0, seen)

    def backtrack(self, s, start, seen):
        if start == len(s):
            return 0

        max_count = 0

        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)
                max_count = max(max_count, 1 + self.backtrack(s, end, seen))
                seen.remove(sub_string)

        return max_count

def test_max_unique_split():
    solution = Solution()

    # Test case 1
    s = "ababccc"
    print(solution.maxUniqueSplit(s))  # Expected output: 5

    # Test case 2
    s = "aba"
    print(solution.maxUniqueSplit(s))  # Expected output: 2

    # Test case 3
    s = "aa"
    print(solution.maxUniqueSplit(s))  # Expected output: 1

    # Test case 4
    s = "abcdef"
    print(solution.maxUniqueSplit(s))  # Expected output: 6

    # Test case 5
    s = "abcabc"
    print(solution.maxUniqueSplit(s))  # Expected output: 3

test_max_unique_split()