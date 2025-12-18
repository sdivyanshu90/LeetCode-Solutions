from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        left = 0
        right = n - 1
        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1
        
        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1
        
        if left > 0 and left == right and right < n - 1:
            return True
        else:
            return False

def test_valid_mountain_array():
    solution = Solution()

    # Test case 1
    arr1 = [2,1]
    print(solution.validMountainArray(arr1))  # Expected output: False

    # Test case 2
    arr2 = [3,5,5]
    print(solution.validMountainArray(arr2))  # Expected output: False

    # Test case 3
    arr3 = [0,3,2,1]
    print(solution.validMountainArray(arr3))  # Expected output: True

    # Test case 4
    arr4 = [0,1,2,3,4,5,6,7,8,9]
    print(solution.validMountainArray(arr4))  # Expected output: False

    # Test case 5
    arr5 = [9,8,7,6,5,4,3,2,1,0]
    print(solution.validMountainArray(arr5))  # Expected output: False

test_valid_mountain_array()