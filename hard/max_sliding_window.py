from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        dq = deque()

        def clean_deque(i):
            if dq and dq[0] == i - k:
                dq.popleft()
            
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

        res = []
        
        for i in range(k):
            clean_deque(i)
            dq.append(i)
        res.append(nums[dq[0]])

        for i in range(k, n):
            clean_deque(i)
            dq.append(i)
            res.append(nums[dq[0]])

        return res

def test_max_sliding_window():
    s = Solution()

    # Test Case 1: Standard example
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [3, 3, 5, 5, 6, 7]

    # Test Case 2: k = 1 (edge case)
    nums, k = [1, 2, 3, 4, 5], 1
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [1, 2, 3, 4, 5]

    # Test Case 3: k = length of the array (edge case)
    nums, k = [9, 10, 9, -7, -4, -8, 2, -6], 8
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [10]

    # Test Case 4: Strictly decreasing list
    nums, k = [10, 9, 8, 7, 6, 5], 3
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [10, 9, 8, 7]

    # Test Case 5: Strictly increasing list
    nums, k = [1, 2, 3, 4, 5, 6], 3
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [3, 4, 5, 6]

    # Test Case 6: List with all same elements
    nums, k = [5, 5, 5, 5, 5, 5], 4
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [5, 5, 5]

    # Test Case 7: Empty list (edge case)
    nums, k = [], 5
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: []

    # Test Case 8: k = 0 (edge case, though k >= 1 is usually a constraint)
    nums, k = [1, 2, 3], 0
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: []

    # Test Case 9: List with negative numbers
    nums, k = [-7, -8, -9, -1, -2, -3], 2
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [-7, -8, -1, -1, -2]

    # Test Case 10: A zig-zag pattern
    nums, k = [9, 5, 8, 2, 7, 3, 6, 4], 3
    print(f"\nInput: nums = {nums}, k = {k}")
    print(f"Output: {s.maxSlidingWindow(nums, k)}") # Expected: [9, 8, 8, 7, 7, 6]

test_max_sliding_window()