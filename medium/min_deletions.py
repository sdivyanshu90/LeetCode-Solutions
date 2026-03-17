from typing import List
import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = collections.Counter(s)
        used_freq = set()
        deletions = 0
        for char, count in char_count.items():
            while count in used_freq and count > 0:
                deletions += 1
                count -= 1
            used_freq.add(count)
        return deletions

def test_min_deletions():
    solution = Solution()

    # Test case 1
    s1 = "aab"
    print(solution.minDeletions(s1))  # Expected output: 0

    # Test case 2
    s2 = "aaabbbcc"
    print(solution.minDeletions(s2))  # Expected output: 2

    # Test case 3
    s3 = "ceabaacb"
    print(solution.minDeletions(s3))  # Expected output: 2

    # Test case 4
    s4 = "abcde"
    print(solution.minDeletions(s4))  # Expected output: 4

    # Test case 5
    s5 = "aaabbbcccddd"
    print(solution.minDeletions(s5))  # Expected output: 6

test_min_deletions()