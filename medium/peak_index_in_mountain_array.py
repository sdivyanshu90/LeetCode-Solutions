from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) >> 1

            if arr[mid] <= arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

def test_peakIndexInMountainArray():
    solution = Solution()
    
    # Test Case 1
    print(solution.peakIndexInMountainArray([0,1,0])) # Expected: 1

    # Test Case 2
    print(solution.peakIndexInMountainArray([0,2,1,0])) # Expected: 1

    # Test Case 3
    print(solution.peakIndexInMountainArray([0,10,5,2])) # Expected: 1

    # Test Case 4
    print(solution.peakIndexInMountainArray([3,4,5,1])) # Expected: 2

    # Test Case 5
    print(solution.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])) # Expected: 2

test_peakIndexInMountainArray()