from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

def test_contains_duplicates():
    s = Solution()

    # Test Case 1: Basic case with a duplicate
    nums = [1, 2, 3, 1]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: True

    # Test Case 2: No duplicates
    nums = [1, 2, 3, 4]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: False

    # Test Case 3: Empty list (edge case)
    nums = []
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: False

    # Test Case 4: Single element list (edge case)
    nums = [1]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: False

    # Test Case 5: All elements are the same
    nums = [7, 7, 7, 7]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: True

    # Test Case 6: Multiple different duplicates
    nums = [1, 1, 2, 2, 3, 3]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: True

    # Test Case 7: List with negative numbers and duplicates
    nums = [-1, -2, -3, -1]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: True

    # Test Case 8: List with negative numbers and no duplicates
    nums = [-1, -2, -3, -4]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: False

    # Test Case 9: List containing zero as a duplicate
    nums = [0, 1, 2, 3, 0]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: True

    # Test Case 10: A longer list with no duplicates
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"\nInput: {nums}")
    print(f"Output: {s.containsDuplicate(nums)}") # Expected: False

test_contains_duplicates()