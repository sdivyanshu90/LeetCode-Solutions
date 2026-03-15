from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1
        
        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i
        
        return -1

def test_special_array():
    solution = Solution()

    # Test case 1
    nums = [3, 5]
    print(solution.specialArray(nums))  # Expected output: 2

    # Test case 2
    nums = [0, 0]
    print(solution.specialArray(nums))  # Expected output: -1

    # Test case 3
    nums = [0, 4, 3, 0, 4]
    print(solution.specialArray(nums))  # Expected output: 3

    # Test case 4
    nums = [1, 1, 3]
    print(solution.specialArray(nums))  # Expected output: -1

    # Test case 5
    nums = [1, 2, 3, 4, 5]
    print(solution.specialArray(nums))  # Expected output: 3

test_special_array()