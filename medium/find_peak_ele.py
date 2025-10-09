from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
        return left

def test_find_peak_element():
    sol = Solution()
    
    # Test case 1
    print(sol.findPeakElement([1, 2, 3, 1])) # Expected output: 2 (index of peak element 3)
    
    # Test case 2
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])) # Expected output: 5 (index of peak element 6)
    
    # Test case 3
    print(sol.findPeakElement([1])) # Expected output: 0 (only one element)
    
    # Test case 4
    print(sol.findPeakElement([3, 2, 1])) # Expected output: 0 (peak is the first element)
    
    # Test case 5
    print(sol.findPeakElement([1, 2, 3])) # Expected output: 2 (peak is the last element)

    # Test case 6
    print(sol.findPeakElement([1, 3, 2, 4, 3, 5, 4])) # Expected output: 1 (indices of peak elements 3, 4, or 5)

    # Test case 7
    print(sol.findPeakElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Expected output: 9 (peak is the last element)

    # Test case 8
    print(sol.findPeakElement([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # Expected output: 0 (peak is the first element)

    # Test case 9
    print(sol.findPeakElement([1, 3, 2, 1, 4, 3, 5, 4, 6, 5])) # Expected output: 1

    # Test case 10
    print(sol.findPeakElement([1, 2, 1, 2, 1, 2, 1])) # Expected output: 1 (indices of peak elements 2)

test_find_peak_element()