from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = -1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                if last_index != -1 and i - last_index <= k:
                    return False
                last_index = i
        
        return True

def test_k_length_apart():
    solution = Solution()

    # Test case 1
    nums1 = [1,0,0,0,1,0,0,1]
    k1 = 2
    print(solution.kLengthApart(nums1, k1))  # Expected output: True

    # Test case 2
    nums2 = [1,0,0,1,0,1]
    k2 = 2
    print(solution.kLengthApart(nums2, k2))  # Expected output: False

    # Test case 3
    nums3 = [1,1,1,1]
    k3 = 0
    print(solution.kLengthApart(nums3, k3))  # Expected output: True

    # Test case 4
    nums4 = [0,0,0]
    k4 = 1
    print(solution.kLengthApart(nums4, k4))  # Expected output: True

    # Test case 5
    nums5 = [1,0,1]
    k5 = 2
    print(solution.kLengthApart(nums5, k5))  # Expected output: False

test_k_length_apart()