from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        size = len(arr)
        count = 0
        prefix = 0

        count_map = defaultdict(int)
        count_map[0] = 1
        total_map = defaultdict(int)

        for i in range(size):
            prefix ^= arr[i]
            count += count_map[prefix] * i - total_map[prefix]
            total_map[prefix] += i + 1
            count_map[prefix] += 1

        return count

def test_count_triplets():
    solution = Solution()

    # Test case 1
    arr1 = [2, 3, 1, 6, 7]
    print(solution.countTriplets(arr1))  # Expected output: 4

    # Test case 2
    arr2 = [1, 1, 1, 1, 1]
    print(solution.countTriplets(arr2))  # Expected output: 10

    # Test case 3
    arr3 = [2, 3]
    print(solution.countTriplets(arr3))  # Expected output: 0

    # Test case 4
    arr4 = [1, 3, 5, 7]
    print(solution.countTriplets(arr4))  # Expected output: 3

    # Test case 5
    arr5 = [1, 2, 3, 4]
    print(solution.countTriplets(arr5))  # Expected output: 2

test_count_triplets()