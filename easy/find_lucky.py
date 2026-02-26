from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr) 

        lucky_number = -1
        for num, count in freq.items():
            if num == count:
                lucky_number = max(lucky_number, num)

        return lucky_number

def test_find_lucky():
    solution = Solution()

    # Test case 1
    arr1 = [2, 2, 3, 4]
    print(solution.findLucky(arr1))  # Expected output: 2

    # Test case 2
    arr2 = [1, 1, 1, 3]
    print(solution.findLucky(arr2))  # Expected output: -1

    # Test case 3
    arr3 = [1, 1, 1, 3, 3, 3]
    print(solution.findLucky(arr3))  # Expected output: 3

    # Test case 4
    arr4 = [1, 1, 1, 3, 3, 3, 7]
    print(solution.findLucky(arr4))  # Expected output: 3

    # Test case 5
    arr5 = [1, 2, 2, 3]
    print(solution.findLucky(arr5))  # Expected output: 2

test_find_lucky()