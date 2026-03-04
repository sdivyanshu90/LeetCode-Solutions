class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0

        # Find the four smallest elements
        smallest_four = sorted(heapq.nsmallest(4, nums))

        # Find the four largest elements
        largest_four = sorted(heapq.nlargest(4, nums))

        min_diff = float("inf")
        # Four scenarios to compute the minimum difference
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])

        return min_diff

def test_min_difference():
    solution = Solution()

    # Test Case 1
    nums1 = [5, 3, 2, 4]
    print(solution.minDifference(nums1))  # Expected output: 0

    # Test Case 2
    nums2 = [1, 5, 0, 10, 14]
    print(solution.minDifference(nums2))  # Expected output: 1

    # Test Case 3
    nums3 = [6, 6, 0, 1, 1, 4, 6]
    print(solution.minDifference(nums3))  # Expected output: 2

    # Test Case 4
    nums4 = [1, 5, 6, 14, 15]
    print(solution.minDifference(nums4))  # Expected output: 1

    # Test Case 5
    nums5 = [1] * (10 ** 5)
    print(solution.minDifference(nums5))  # Expected output: 0

test_min_difference()