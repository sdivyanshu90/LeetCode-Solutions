class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        left, right = 0, 0
        current_sum = 0
        min_ops = float('inf')
        
        while right < len(nums):
            current_sum += nums[right]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                min_ops = min(min_ops, len(nums) - (right - left + 1))
            
            right += 1
        
        return min_ops if min_ops != float('inf') else -1

def test_min_operations():
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 4, 2, 3]
    x1 = 5
    print(solution.minOperations(nums1, x1))  # Expected output: 2

    # Test case 2
    nums2 = [5, 6, 7, 8, 9]
    x2 = 4
    print(solution.minOperations(nums2, x2))  # Expected output: -1

    # Test case 3
    nums3 = [3, 2, 20, 1, 1, 3]
    x3 = 10
    print(solution.minOperations(nums3, x3))  # Expected output: 5

    # Test case 4
    nums4 = [1, 1]
    x4 = 3
    print(solution.minOperations(nums4, x4))  # Expected output: -1

    # Test case 5
    nums5 = [1, 1]
    x5 = 2
    print(solution.minOperations(nums5, x5))  # Expected output: 2

test_min_operations()