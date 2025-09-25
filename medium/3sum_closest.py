from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

def test_three_sum_closest():
    solution = Solution()

    # Test case 1
    nums = [-1,2,1,-4]
    target = 1
    print(solution.threeSumClosest(nums, target))  # Expected output: 2

    # Test case 2
    nums = [0,0,0]
    target = 1
    print(solution.threeSumClosest(nums, target))  # Expected output: 0

    # Test case 3
    nums = [1,1,1,0]
    target = -100
    print(solution.threeSumClosest(nums, target))  # Expected output: 2

    # Test case 4
    nums = [1,2,5,10,11]
    target = 12
    print(solution.threeSumClosest(nums, target))  # Expected output: 13

    # Test case 5
    nums = [0,2,1,-3]
    target = 1
    print(solution.threeSumClosest(nums, target))  # Expected output: 0

    # Test case 6
    nums = [1,6,9,14,16,70]
    target = 81
    print(solution.threeSumClosest(nums, target))  # Expected output: 80

    # Test case 7
    nums = [-3,-2,-5,3,-4]
    target = -1
    print(solution.threeSumClosest(nums, target))  # Expected output: -2

    # Test case 8
    nums = [0,1,2]
    target = 3
    print(solution.threeSumClosest(nums, target))  # Expected output: 3

    # Test case 9
    nums = [1,1,-1,-1,3]
    target = -1
    print(solution.threeSumClosest(nums, target))  # Expected output: -1

    # Test case 10
    nums = [0,2,1,-3]
    target = 1
    print(solution.threeSumClosest(nums, target))  # Expected output: 0


test_three_sum_closest()