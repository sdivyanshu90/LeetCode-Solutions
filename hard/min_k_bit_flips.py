from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        current_flips = 0
        total_flips = 0

        for i in range(len(nums)):
            if i >= k and nums[i - k] == 2:
                current_flips -= 1

            if (current_flips % 2) == nums[i]:
                if i + k > len(nums):
                    return -1
                nums[i] = 2
                current_flips += 1
                total_flips += 1

        return total_flips

def test_min_k_bit_flips():
    solution = Solution()
    
    # Test case 1
    nums = [0,1,0]
    k = 1
    print(solution.minKBitFlips(nums, k))  # Expected output: 2

    # Test case 2
    nums = [1,1,0]
    k = 2
    print(solution.minKBitFlips(nums, k))  # Expected output: -1

    # Test case 3
    nums = [0,0,0,1,0,1,1,0]
    k = 3
    print(solution.minKBitFlips(nums, k))  # Expected output: 3

    # Test case 4
    nums = [1,0,0,0,1]
    k = 4
    print(solution.minKBitFlips(nums, k))  # Expected output: 2

    # Test case 5
    nums = [0,0,0,0,0]
    k = 2
    print(solution.minKBitFlips(nums, k))  # Expected output: 3

test_min_k_bit_flips()