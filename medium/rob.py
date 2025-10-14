from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        prevprev = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            prev, prevprev = max(prevprev + nums[i], prev), prev
        
        return prev

def test_rob():
    s = Solution()

    # Test Case 1: Provided example from many platforms
    nums = [1, 2, 3, 1]
    print(f"\nInput: {nums}, Output: {s.rob(nums)}") # Expected: 4 (1 + 3)

    # Test Case 2: Another common example
    nums = [2, 7, 9, 3, 1]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 12 (2 + 9 + 1)

    # Test Case 3: Empty list (edge case)
    nums = []
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 0

    # Test Case 4: Single house (edge case)
    nums = [100]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 100

    # Test Case 5: Two houses, rob the second one
    nums = [2, 100]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 100

    # Test Case 6: A longer list
    nums = [6, 7, 1, 30, 8, 2, 4]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 41 (7 + 30 + 4)

    # Test Case 7: All houses have zero money
    nums = [0, 0, 0, 0, 0]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 0

    # Test Case 8: Only one optimal choice is non-adjacent
    nums = [100, 1, 1, 100]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 200 (100 + 100)

    # Test Case 9: Decreasing values
    nums = [10, 8, 5, 2, 1]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 16 (10 + 5 + 1)

    # Test Case 10: Best to skip two houses in a row
    nums = [4, 1, 1, 9, 1]
    print(f"Input: {nums}, Output: {s.rob(nums)}") # Expected: 13 (4 + 9)

test_rob()