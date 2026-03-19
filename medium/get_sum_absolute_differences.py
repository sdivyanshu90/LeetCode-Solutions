class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        first_sum = 0
        for i in range(1, len(nums)):
            first_sum += nums[i] - nums[0]
        abs_sum = [first_sum]
        for i in range(1, len(nums)):
            abs_sum.append(abs_sum[-1] + (2 * i - len(nums)) * (nums[i] - nums[i - 1]))
        return abs_sum

def test_get_sum_absolute_differences():
    solution = Solution()

    # Test case 1
    nums = [2, 3, 5]
    print(solution.getSumAbsoluteDifferences(nums))  # Expected output: [4, 3, 5]

    # Test case 2
    nums = [1, 4, 6, 8]
    print(solution.getSumAbsoluteDifferences(nums))  # Expected output: [20, 13, 13, 20]

    # Test case 3
    nums = [1]
    print(solution.getSumAbsoluteDifferences(nums))  # Expected output: [0]

    # Test case 4
    nums = [1, 2]
    print(solution.getSumAbsoluteDifferences(nums))  # Expected output: [1, 1]

    # Test case 5
    nums = [1, 3]
    print(solution.getSumAbsoluteDifferences(nums))  # Expected output: [2, 2]

test_get_sum_absolute_differences()