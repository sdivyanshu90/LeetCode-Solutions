from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, res = 0, 0
        for num in nums:
            if num == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1

        return max(res, count)

def test_find_max_consecutive_ones():
    solution = Solution()

    # Test case 1
    nums = [1, 1, 0, 1, 1, 1]
    print(solution.findMaxConsecutiveOnes(nums))  # Expected output: 3

    # Test case 2
    nums = [1, 0, 1, 1, 0, 1]
    print(solution.findMaxConsecutiveOnes(nums))  # Expected output: 2

    # Test case 3
    nums = [0, 0, 0]
    print(solution.findMaxConsecutiveOnes(nums))  # Expected output: 0

    # Test case 4
    nums = [1, 1, 1, 1, 1]
    print(solution.findMaxConsecutiveOnes(nums))  # Expected output: 5

    # Test case 5
    nums = []
    print(solution.findMaxConsecutiveOnes(nums))  # Expected output: 0

test_find_max_consecutive_ones()