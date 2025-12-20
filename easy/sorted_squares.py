from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        position = len(nums) - 1
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
            position -= 1
        return result

def test_sorted_squares():
    solution = Solution()
    
    # Test case 1
    nums = [-4,-1,0,3,10]
    print(solution.sortedSquares(nums))  # Expected output: [0,1,9,16,100]

    # Test case 2
    nums = [-7,-3,2,3,11]
    print(solution.sortedSquares(nums))  # Expected output: [4,9,9,49,121]

    # Test case 3
    nums = [-5,-3,-2,-1]
    print(solution.sortedSquares(nums))  # Expected output: [1,4,9,25]

    # Test case 4
    nums = [0,1,2,3,4]
    print(solution.sortedSquares(nums))  # Expected output: [0,1,4,9,16]

    # Test case 5
    nums = [-2,0]
    print(solution.sortedSquares(nums))  # Expected output: [0,4]

test_sorted_squares()