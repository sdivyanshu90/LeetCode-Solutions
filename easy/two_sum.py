from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


def test_two_sum():
    solution = Solution()

    # Test Case 1: Basic Example (Found Pair)
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # Expected output: [0, 1]

    # Test Case 2: Negative Numbers
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(solution.twoSum(nums, target))  # Expected output: [2, 4]

    # Test Case 3: No Solution
    nums = [1, 2, 3, 4, 5]
    target = 10
    print(solution.twoSum(nums, target))  # Expected output: []

    # Test Case 4: Large Numbers
    nums = [1000000, 5000000, 7000000, 2000000]
    target = 12000000
    print(solution.twoSum(nums, target))  # Expected output: [1, 2]

    # Test Case 5: Multiple Pairs
    nums = [3, 2, 4, 3]
    target = 6
    print(solution.twoSum(nums, target))  # Expected output: [0, 3] or [1, 2]

    # Test Case 6: Large List with Solution at the End
    nums = [i for i in range(1, 1000001)]
    target = 1999999
    print(solution.twoSum(nums, target))  # Expected output: [999998, 999999]

    # Test Case 7: Single Element (No Solution)
    nums = [1]
    target = 2
    print(solution.twoSum(nums, target))  # Expected output: []

    # Test Case 8: Same Value Multiple Times
    nums = [1, 1, 1, 1]
    target = 2
    print(solution.twoSum(nums, target))  # Expected output: [0, 1]

    # Test Case 9: Zero as Target
    nums = [0, 4, -4, 3, 2]
    target = 0
    print(solution.twoSum(nums, target))  # Expected output: [1, 2]

    # Test Case 10: Large Negative Target
    nums = [-7, 1, 5, -4]
    target = -3
    print(solution.twoSum(nums, target))  # Expected output: [0, 3]


test_two_sum()