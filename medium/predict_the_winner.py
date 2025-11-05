from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def canWin(left: int, right: int) -> bool:
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            memo[(left, right)] = max(nums[left] - canWin(left + 1, right), nums[right] - canWin(left, right - 1))
            return memo[(left, right)]

        return canWin(0, len(nums) - 1) >= 0

def test_predict_the_winner():
    solution = Solution()

    # Test case 1
    nums = [1, 5, 2]
    print(solution.predictTheWinner(nums))  # Expected output: False

    # Test case 2
    nums = [1, 5, 233, 7]
    print(solution.predictTheWinner(nums))  # Expected output: True

    # Test case 3
    nums = [0]
    print(solution.predictTheWinner(nums))  # Expected output: True

    # Test case 4
    nums = [3, 9, 1, 2]
    print(solution.predictTheWinner(nums))  # Expected output: True

    # Test case 5
    nums = [1, 2, 3, 4, 5, 6]
    print(solution.predictTheWinner(nums))  # Expected output: False

test_predict_the_winner()