from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        s = []

        for i in range(2 * n):
            index = i % n
            
            while s and nums[s[-1]] < nums[index]:
                result[s.pop()] = nums[index]
            
            if i < n:
                s.append(index)

        return result

def test_next_greater_elements():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 1]
    print(solution.nextGreaterElements(nums))  # Expected output: [2, -1, 2]

    # Test case 2
    nums = [5, 4, 3, 2, 1]
    print(solution.nextGreaterElements(nums))  # Expected output: [-1, 5, 5, 5, 5]

    # Test case 3
    nums = [2, 2, 2]
    print(solution.nextGreaterElements(nums))  # Expected output: [-1, -1, -1]

    # Test case 4
    nums = [1, 3, 2, 4]
    print(solution.nextGreaterElements(nums))  # Expected output: [3, 4, 4, -1]

    # Test case 5
    nums = [1]
    print(solution.nextGreaterElements(nums))  # Expected output: [-1]

test_next_greater_elements()