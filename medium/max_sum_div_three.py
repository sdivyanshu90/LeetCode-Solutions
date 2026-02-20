from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]

def test_max_sum_div_three():
    solution = Solution()

    # Test case 1
    nums = [3, 6, 5, 1, 8]
    print(solution.maxSumDivThree(nums))  # Expected output: 18

    # Test case 2
    nums = [4]
    print(solution.maxSumDivThree(nums))  # Expected output: 0

    # Test case 3
    nums = [1, 2, 3, 4, 4]
    print(solution.maxSumDivThree(nums))  # Expected output: 12

    # Test case 4
    nums = [1, 1, 1]
    print(solution.maxSumDivThree(nums))  # Expected output: 3

    # Test case 5
    nums = [2, 2, 2]
    print(solution.maxSumDivThree(nums))  # Expected output: 6

test_max_sum_div_three()