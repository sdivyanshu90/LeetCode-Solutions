from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101
        for num in nums:
            count[num] += 1
        
        for i in range(1, 101):
            count[i] += count[i - 1]
        
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1])
        
        return result

def test_smallerNumbersThanCurrent():
    solution = Solution()

    # Test case 1
    nums1 = [8, 1, 2, 2, 3]
    print(solution.smallerNumbersThanCurrent(nums1)) # Expected output: [4, 0, 1, 1, 3]

    # Test case 2
    nums2 = [6, 5, 4, 8]
    print(solution.smallerNumbersThanCurrent(nums2)) # Expected output: [2, 1, 0, 3]

    # Test case 3
    nums3 = [7, 7, 7, 7]
    print(solution.smallerNumbersThanCurrent(nums3)) # Expected output: [0, 0, 0, 0]

    # Test case 4
    nums4 = [0]
    print(solution.smallerNumbersThanCurrent(nums4)) # Expected output: [0]

    # Test case 5
    nums5 = [10, 9, 8, 7]
    print(solution.smallerNumbersThanCurrent(nums5)) # Expected output: [3, 2, 1, 0]

test_smallerNumbersThanCurrent()