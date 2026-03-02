from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.extend([nums[i], nums[i + n]])
        return res

def test_shuffle():
    solution = Solution()

    # Test case 1
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(solution.shuffle(nums, n))  # Expected output: [2, 3, 5, 4, 1, 7]

    # Test case 2
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(solution.shuffle(nums, n))  # Expected output: [1, 4, 2, 3, 3, 2, 4, 1]

    # Test case 3
    nums = [1, 1, 2, 2]
    n = 2
    print(solution.shuffle(nums, n))  # Expected output: [1, 2, 1, 2]

    # Test case 4
    nums = [1]
    n = 0
    print(solution.shuffle(nums, n))  # Expected output: []

    # Test case 5
    nums = [0]
    n = 0
    print(solution.shuffle(nums, n))  # Expected output: []

test_shuffle()