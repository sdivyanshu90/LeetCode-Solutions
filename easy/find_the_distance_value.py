from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for a1 in arr1:
            low = bisect_left(arr2, a1 - d)
            high = bisect_right(arr2, a1 + d)
            
            if low == high:
                count += 1
                
        return count

def test_find_the_distance_value():
    solution = Solution()

    # Test case 1
    arr1_1 = [4, 5, 8]
    arr2_1 = [10, 9, 1, 8]
    d1 = 2
    print(solution.findTheDistanceValue(arr1_1, arr2_1, d1))  # Expected output: 2

    # Test case 2
    arr1_2 = [1, 4, 2, 3]
    arr2_2 = [-4, -3, 6, 10, 20, 30]
    d2 = 3
    print(solution.findTheDistanceValue(arr1_2, arr2_2, d2))  # Expected output: 2

    # Test case 3
    arr1_3 = [2, 1, 100, 3]
    arr2_3 = [-5, -2, -3]
    d3 = 10
    print(solution.findTheDistanceValue(arr1_3, arr2_3, d3))  # Expected output: 1

    # Test case 4
    arr1_4 = [1, 2, 3]
    arr2_4 = [4, 5, 6]
    d4 = 1
    print(solution.findTheDistanceValue(arr1_4, arr2_4, d4))  # Expected output: 2

    # Test case 5
    arr1_5 = [1, 2, 3]
    arr2_5 = [10, 11, 12]
    d5 = 5
    print(solution.findTheDistanceValue(arr1_5, arr2_5, d5))  # Expected output: 3

test_find_the_distance_value()