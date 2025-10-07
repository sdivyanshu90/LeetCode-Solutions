from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                longest = max(longest, length)
        return longest

def test_longest_consecutive():
    solution = Solution()
    
    # Test case 1
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums))  # Expected output: 4

    # Test case 2
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(solution.longestConsecutive(nums))  # Expected output: 9

    # Test case 3
    nums = []
    print(solution.longestConsecutive(nums))  # Expected output: 0

    # Test case 4
    nums = [1,2,0,1]
    print(solution.longestConsecutive(nums))  # Expected output: 3

    # Test case 5
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
    print(solution.longestConsecutive(nums))  # Expected output: 4

test_longest_consecutive()