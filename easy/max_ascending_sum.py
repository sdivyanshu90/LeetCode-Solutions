class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        max_sum = max(max_sum, current_sum)
        
        return max_sum

def test_max_ascending_sum():
    solution = Solution()

    # Test Case 1
    nums1 = [10,20,30,5,10,50]
    print(solution.maxAscendingSum(nums1))  # Expected Output: 65

    # Test Case 2
    nums2 = [10,20,30,40,50]
    print(solution.maxAscendingSum(nums2))  # Expected Output: 150

    # Test Case 3
    nums3 = [12,17,15,13,10,11,12]
    print(solution.maxAscendingSum(nums3))  # Expected Output: 33

    # Test Case 4
    nums4 = [100,10,1]
    print(solution.maxAscendingSum(nums4))  # Expected Output: 100

    # Test Case 5
    nums5 = [1,2,3,4,5]
    print(solution.maxAscendingSum(nums5))  # Expected Output: 15

test_max_ascending_sum()