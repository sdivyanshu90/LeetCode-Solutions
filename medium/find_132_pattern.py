from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third = float('-inf')
        stack = [] 
        for n in reversed(nums):
            if n < third:
                return True
            while stack and n > stack[-1]:
                third = stack.pop()
            stack.append(n) 
        return False

def test_find_132_pattern():
    s = Solution()

    # Test case 1
    nums = [1,2,3,4]
    print(s.find132pattern(nums))  # Expected output: False

    # Test case 2
    nums = [3,1,4,2]
    print(s.find132pattern(nums))  # Expected output: True

    # Test case 3
    nums = [-1,3,2,0]
    print(s.find132pattern(nums))  # Expected output: True

    # Test case 4
    nums = [1,0,1,-4,-3]
    print(s.find132pattern(nums))  # Expected output: False

    # Test case 5
    nums = [3,5,0,3,4]
    print(s.find132pattern(nums))  # Expected output: True

test_find_132_pattern()