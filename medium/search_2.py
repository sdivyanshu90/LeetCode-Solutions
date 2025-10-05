from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

def test_search():
    solution = Solution()

    # Test case 1
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(solution.search(nums, target))  # Output: True

    # Test case 2
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    print(solution.search(nums, target))  # Output: False

    # Test case 3
    nums = [1, 0, 1, 1, 1]
    target = 0
    print(solution.search(nums, target))  # Output: True

    # Test case 4
    nums = [1, 1, 3, 1]
    target = 3
    print(solution.search(nums, target))  # Output: True

    # Test case 5
    nums = [1, 3, 1, 1, 1]
    target = 3
    print(solution.search(nums, target))  # Output: True

    # Test case 6
    nums = [1]
    target = 1
    print(solution.search(nums, target))  # Output: True

    # Test case 7
    nums = [1]
    target = 0
    print(solution.search(nums, target))  # Output: False

    # Test case 8
    nums = []
    target = 5
    print(solution.search(nums, target))  # Output: False

    # Test case 9
    nums = [1, 1, 1, 1, 1]
    target = 2
    print(solution.search(nums, target))  # Output: False

    # Test case 10
    nums = [3, 1]
    target = 1
    print(solution.search(nums, target))  # Output: True

test_search()