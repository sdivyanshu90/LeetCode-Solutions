from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if i in nums:
                nums.remove(i)
        return nums[0]

def test_find_duplicates():
    s = Solution()

    # Test Case 1: Standard case with duplicate in the middle
    nums = [1, 3, 4, 2, 2]
    print(s.findDuplicate(nums)) # Expected from this code: 2

    # Test Case 2: Duplicate appears at the beginning of the unsorted list
    nums = [3, 1, 3, 4, 2]
    print(s.findDuplicate(nums)) # Expected from this code: 3
    
    # Test Case 3: The smallest possible list with a duplicate
    nums = [1, 1]
    print(s.findDuplicate(nums)) # Expected from this code: 1

    # Test Case 4: Duplicate is the largest number in the range
    nums = [4, 1, 2, 3, 4]
    print(s.findDuplicate(nums)) # Expected from this code: 4

    # Test Case 5: A larger list
    nums = [4, 3, 1, 5, 2, 6, 3]
    print(s.findDuplicate(nums)) # Expected from this code: 3

    # Test Case 6: Multiple instances of the duplicate number
    nums = [2, 2, 2, 2, 2]
    print(s.findDuplicate(nums)) # Expected from this code: 2

    # Test Case 7: Another standard case
    nums = [1, 2, 4, 4, 3]
    print(s.findDuplicate(nums)) # Expected from this code: 4
    
    # Test Case 8: Duplicate is 1
    nums = [1, 1, 3, 4, 2]
    print(s.findDuplicate(nums)) # Expected from this code: 1
    
    # Test Case 9: Long list with duplicate at the end (unsorted)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
    print(s.findDuplicate(nums)) # Expected from this code: 8

    # Test Case 10: A case where the flawed logic might be more apparent
    nums = [5, 5, 5, 5, 5]
    print(s.findDuplicate(nums)) # Expected from this code: 5

test_find_duplicates()