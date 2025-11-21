from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return [actual_sum - sum(set(nums)), total_sum - actual_sum + (actual_sum - sum(set(nums)))]

def test_find_error_nums():
    s = Solution()

    # Test case 1
    nums = [1,2,2,4]
    print(s.findErrorNums(nums))  # Expected output: [2,3]

    # Test case 2
    nums = [1,1]
    print(s.findErrorNums(nums))  # Expected output: [1,2]

    # Test case 3
    nums = [2,2]
    print(s.findErrorNums(nums))  # Expected output: [2,1]

    # Test case 4
    nums = [3,2,3,4,6,5]
    print(s.findErrorNums(nums))  # Expected output: [3,1]

    # Test case 5
    nums = [1,5,3,2,2,7,6,4,8,9]
    print(s.findErrorNums(nums))  # Expected output: [2,10]

test_find_error_nums()