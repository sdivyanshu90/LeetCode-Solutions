from typing import List
from collections import defaultdict

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        target = len(arr) / 4
        for num in arr:
            counts[num] += 1
            if counts[num] > target:
                return num

        return -1

def test_find_special_integer():
    solution = Solution()

    # Test case 1
    arr = [1,2,2,6,6,6,6,7,10]
    print(solution.findSpecialInteger(arr))  # Expected output: 6

    # Test case 2
    arr = [1,1,1,3]
    print(solution.findSpecialInteger(arr))  # Expected output: 1

    # Test case 3
    arr = [1,1,1,3]
    print(solution.findSpecialInteger(arr))  # Expected output: 1

    # Test case 4
    arr = [1,2,3,4]
    print(solution.findSpecialInteger(arr))  # Expected output: -1

    # Test case 5
    arr = [1,2,3]
    print(solution.findSpecialInteger(arr))  # Expected output: -1

test_find_special_integer()