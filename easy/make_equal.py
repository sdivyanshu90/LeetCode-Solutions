from collections import defaultdict
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            for c in word:
                counts[c] += 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True

def test_make_equal():
    solution = Solution()

    # Test case 1
    words = ["abc", "aabc", "bc"]
    print(solution.makeEqual(words))  # Expected output: True

    # Test case 2
    words = ["ab", "a"]
    print(solution.makeEqual(words))  # Expected output: False

    # Test case 3
    words = ["aa", "bb", "cc"]
    print(solution.makeEqual(words))  # Expected output: False

    # Test case 4
    words = ["abc", "def", "ghi"]
    print(solution.makeEqual(words))  # Expected output: False

    # Test case 5
    words = ["a", "a", "a"]
    print(solution.makeEqual(words))  # Expected output: True

test_make_equal()