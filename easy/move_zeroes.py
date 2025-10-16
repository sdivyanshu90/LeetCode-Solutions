from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        return nums

def test_move_zeroes():
    s = Solution()

    # Test Case 1: Standard mix of zeros and non-zeros (as provided)
    nums = [0, 1, 0, 3, 12]
    print(s.moveZeroes(nums)) # Expected: [1, 3, 12, 0, 0]

    # Test Case 2: A list containing only zeros
    nums = [0, 0, 0, 0]
    print(s.moveZeroes(nums)) # Expected: [0, 0, 0, 0]

    # Test Case 3: A list with no zeros to move
    nums = [1, 2, 3, 4, 5]
    print(s.moveZeroes(nums)) # Expected: [1, 2, 3, 4, 5]

    # Test Case 4: Zeros are already at the end
    nums = [1, 9, 8, 0, 0]
    print(s.moveZeroes(nums)) # Expected: [1, 9, 8, 0, 0]

    # Test Case 5: All zeros are at the beginning
    nums = [0, 0, 0, 1, 2]
    print(s.moveZeroes(nums)) # Expected: [1, 2, 0, 0, 0]

    # Test Case 6: An empty list
    nums = []
    print(s.moveZeroes(nums)) # Expected: []

    # Test Case 7: A single element list (a zero)
    nums = [0]
    print(s.moveZeroes(nums)) # Expected: [0]
    
    # Test Case 8: A single element list (non-zero)
    nums = [42]
    print(s.moveZeroes(nums)) # Expected: [42]

    # Test Case 9: List with negative numbers and zeros
    nums = [-1, 0, -3, 5, 0, 0, 8]
    print(s.moveZeroes(nums)) # Expected: [-1, -3, 5, 8, 0, 0, 0]

    # Test Case 10: Alternating zeros and non-zeros
    nums = [0, 1, 0, 2, 0, 3]
    print(s.moveZeroes(nums)) # Expected: [1, 2, 3, 0, 0, 0]

test_move_zeroes()