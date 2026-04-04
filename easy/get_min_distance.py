from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(abs(i - start))
            
        return min(res)

def test_get_min_distance():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4, 5]
    target1 = 5
    start1 = 3
    print(solution.getMinDistance(nums1, target1, start1))  # Expected output: 1

    # Test case 2
    nums2 = [1]
    target2 = 1
    start2 = 0
    print(solution.getMinDistance(nums2, target2, start2))  # Expected output: 0

    # Test case 3
    nums3 = [1, 1, 1, 1, 1]
    target3 = 1
    start3 = 0
    print(solution.getMinDistance(nums3, target3, start3))  # Expected output: 0

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    target4 = 1
    start4 = 4
    print(solution.getMinDistance(nums4, target4, start4))  # Expected output: 4

    # Test case 5
    nums5 = [1, 2, 3, 4, 5]
    target5 = 3
    start5 = 2
    print(solution.getMinDistance(nums5, target5, start5))  # Expected output: 0

test_get_min_distance()