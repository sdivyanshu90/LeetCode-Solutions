class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = nums[0]
        res = 0

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                prev += 1
                res += prev - nums[i]
            else:
                prev = nums[i]

        return res

def test_min_operations():
    solution = Solution()

    # Test Case 1
    nums1 = [1,1,1]
    print(solution.minOperations(nums1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1,5,2,4,1]
    print(solution.minOperations(nums2))  # Expected Output: 14

    # Test Case 3
    nums3 = [8]
    print(solution.minOperations(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1,2,3]
    print(solution.minOperations(nums4))  # Expected Output: 0

    # Test Case 5
    nums5 = [3,2,1]
    print(solution.minOperations(nums5))  # Expected Output: 6

test_min_operations()