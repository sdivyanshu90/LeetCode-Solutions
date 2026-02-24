from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda num: (num.bit_count(), num))
        return arr

def test_sortByBits():
    solution = Solution()

    # Test case 1
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(solution.sortByBits(arr1)) # Expected output: [0, 1, 2, 4, 8, 3, 5, 6, 7]

    # Test case 2
    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    print(solution.sortByBits(arr2)) # Expected output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    # Test case 3
    arr3 = [10000]
    print(solution.sortByBits(arr3)) # Expected output: [10000]

    # Test case 4
    arr4 = [10000, -10000]
    print(solution.sortByBits(arr4)) # Expected output: [-10000, 10000]

    # Test case 5
    arr5 = [0, 0, 0, 0]
    print(solution.sortByBits(arr5)) # Expected output: [0, 0, 0, 0]

test_sortByBits()