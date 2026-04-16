from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0

        for num in nums:
            if num - k in freq:
                count += freq[num - k]
            if num + k in freq:
                count += freq[num + k]

            freq[num] = freq.get(num, 0) + 1

        return count

def test_count_k_difference():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4]
    k1 = 1
    print(solution.countKDifference(nums1, k1))  # Expected output: 3

    # Test case 2
    nums2 = [1, 3]
    k2 = 3
    print(solution.countKDifference(nums2, k2))  # Expected output: 0

    # Test case 3
    nums3 = [3, 2, 1, 5, 4]
    k3 = 2
    print(solution.countKDifference(nums3, k3))  # Expected output: 3

    # Test case 4
    nums4 = [1, 1, 1, 1]
    k4 = 0
    print(solution.countKDifference(nums4, k4))  # Expected output: 12

    # Test case 5
    nums5 = [1, 2, 3, 4, 5]
    k5 = 2
    print(solution.countKDifference(nums5, k5))  # Expected output: 3

test_count_k_difference()