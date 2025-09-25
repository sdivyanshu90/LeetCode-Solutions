from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result

def test_three_sum():
    solution = Solution()

    # Test case 1
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))  # Expected output: [[-1,-1,2],[-1,0,1]]

    # Test case 2
    nums = []
    print(solution.threeSum(nums))  # Expected output: []

    # Test case 3
    nums = [0]
    print(solution.threeSum(nums))  # Expected output: []

    # Test case 4
    nums = [0,0,0]
    print(solution.threeSum(nums))  # Expected output: [[0,0,0]]

    # Test case 5
    nums = [1,2,-2,-1]
    print(solution.threeSum(nums))  # Expected output: []

    # Test case 6
    nums = [-2,0,1,1,2]
    print(solution.threeSum(nums))  # Expected output: [[-2,0,2],[-2,1,1]]

    # Test case 7
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(solution.threeSum(nums))  # Expected output: [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]

    # Test case 8
    nums = [-1,0,1]
    print(solution.threeSum(nums))  # Expected output: [[-1,0,1]]

    # Test case 9
    nums = [-1,-1,-1,-1,-1,-1]
    print(solution.threeSum(nums))  # Expected output: []

    # Test case 10
    nums = [3,0,-4,-3,-5,-3,-5]
    print(solution.threeSum(nums))  # Expected output: [[-3,0,3]]

test_three_sum()