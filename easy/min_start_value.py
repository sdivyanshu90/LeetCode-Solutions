class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        val = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            val = min(val, sums)

        res = 1 - val
        return res

def test_min_start_value():
    solution = Solution()

    # Test case 1
    nums1 = [-3, 2, -3, 4, 2]
    print(solution.minStartValue(nums1))  # Expected output: 5

    # Test case 2
    nums2 = [1, 2]
    print(solution.minStartValue(nums2))  # Expected output: 1

    # Test case 3
    nums3 = [1, -2, -3]
    print(solution.minStartValue(nums3))  # Expected output: 5

    # Test case 4
    nums4 = [-1, -2, -3]
    print(solution.minStartValue(nums4))  # Expected output: 7

    # Test case 5
    nums5 = [0, 0, 0]
    print(solution.minStartValue(nums5))  # Expected output: 1

test_min_start_value()