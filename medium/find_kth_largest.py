import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

def test_find_kth_largest():
    s = Solution()

    # Test Case 1: Standard unsorted list
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # Sorted: [1, 2, 3, 4, 5, 6]. The 2nd largest is 5.
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 5

    # Test Case 2: List with duplicates
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    # Sorted: [1, 2, 2, 3, 3, 4, 5, 5, 6]. The 4th largest is 4.
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 4

    # Test Case 3: k is 1 (finding the largest element)
    nums = [99, 12, 34, 56, 78]
    k = 1
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 99

    # Test Case 4: k is equal to the length of the list (finding the smallest element)
    nums = [99, 12, 34, 56, 78]
    k = 5
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 12

    # Test Case 5: List with negative numbers
    nums = [-1, -5, 2, 0]
    k = 2
    # Sorted: [-5, -1, 0, 2]. The 2nd largest is 0.
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 0

    # Test Case 6: List is already sorted
    nums = [10, 20, 30, 40, 50]
    k = 3
    # The 3rd largest is 30.
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 30

    # Test Case 7: List is sorted in reverse order
    nums = [50, 40, 30, 20, 10]
    k = 3
    # The 3rd largest is 30.
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 30

    # Test Case 8: All elements are the same
    nums = [7, 7, 7, 7, 7]
    k = 4
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 7

    # Test Case 9: Single element list (edge case)
    nums = [42]
    k = 1
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 42
    
    # Test Case 10: k points to a duplicate value
    nums = [5, 8, 2, 8, 3, 8]
    k = 3
    # Sorted: [2, 3, 5, 8, 8, 8]. The three largest are [8, 8, 8]. The 3rd largest is 8.
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.findKthLargest(nums, k)}") # Expected: 8

test_find_kth_largest()