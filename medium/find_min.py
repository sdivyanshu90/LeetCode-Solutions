from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(left, right):
            if left == right:
                return nums[left]
            
            if nums[left] < nums[right]:
                return nums[left]
            
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                return binarySearch(mid + 1, right)
            else:
                return binarySearch(left, mid)

        n = len(nums)
        return binarySearch(0, n - 1)

def test_find_min():
    sol = Solution()
    
    # Test case 1
    print(sol.findMin([3, 4, 5, 1, 2])) # Expected output: 1
    
    # Test case 2
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2])) # Expected output: 0
    
    # Test case 3
    print(sol.findMin([11, 13, 15, 17])) # Expected output: 11
    
    # Test case 4
    print(sol.findMin([2, 1])) # Expected output: 1

    # Test case 5
    print(sol.findMin([1])) # Expected output: 1

    # Test case 6
    print(sol.findMin([5, 1, 2, 3, 4])) # Expected output: 1

    # Test case 7
    print(sol.findMin([2, 3, 4, 5, 1])) # Expected output: 1

    # Test case 8
    print(sol.findMin([1, 2, 3, 4, 5])) # Expected output: 1

    # Test case 9
    print(sol.findMin([2, 3, 4, 5, 6, 7, 8, 9, 1])) # Expected output: 1

    # Test case 10
    print(sol.findMin([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # Expected output: 1

test_find_min()