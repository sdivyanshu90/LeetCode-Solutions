from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        frequencies.sort()
        elements_removed = 0

        for i in range(len(frequencies)):
            elements_removed += frequencies[i]
            if elements_removed > k:
                return len(frequencies) - i

        return 0

def test_find_least_num_of_unique_ints():
    solution = Solution()

    # Test case 1
    arr = [5, 5, 4]
    k = 1
    print(solution.findLeastNumOfUniqueInts(arr, k))  # Expected output: 1

    # Test case 2
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    print(solution.findLeastNumOfUniqueInts(arr, k))  # Expected output: 2

    # Test case 3
    arr = [2, 4, 1, 8, 3, 5]
    k = 0
    print(solution.findLeastNumOfUniqueInts(arr, k))  # Expected output: 6

    # Test case 4
    arr = [1, 1, 1]
    k = 2
    print(solution.findLeastNumOfUniqueInts(arr, k))  # Expected output: 1

    # Test case 5
    arr = [1, 2, 3]
    k = 3
    print(solution.findLeastNumOfUniqueInts(arr, k))  # Expected output: 0

test_find_least_num_of_unique_ints()