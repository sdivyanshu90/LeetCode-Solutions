from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
                return
            
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0, len(nums))
        return result

def test_permute():
    solution = Solution()
    
    # Test case 1: Regular case with distinct integers
    print(solution.permute([1,2,3]))  # Expected output: All permutations of [1,2,3]
    
    # Test case 2: Single element
    print(solution.permute([1]))  # Expected output: [[1]]

    # Test case 3: Two elements
    print(solution.permute([1,2]))  # Expected output: [[1,2],[2,1]]

    # Test case 4: Four elements
    print(solution.permute([1,2,3,4]))  # Expected output: All permutations of [1,2,3,4]

    # Test case 5: Empty list
    print(solution.permute([]))  # Expected output: [[]]

    # Test case 6: Negative and positive integers
    print(solution.permute([-1,0,1]))  # Expected output: All permutations of [-1,0,1]

    # Test case 7: Larger input
    print(solution.permute([1,2,3,4,5]))  # Expected output: All permutations of [1,2,3,4,5]

    # Test case 8: Repeated elements (should handle distinct permutations)
    print(solution.permute([1,1,2]))  # Expected output: [[1,1,2],[1,2,1],[2,1,1]]

    # Test case 9: All elements the same
    print(solution.permute([2,2,2]))  # Expected output: [[2,2,2]]

    # Test case 10: Larger range of integers
    print(solution.permute([0,-1,-2]))  # Expected output: All permutations of [0,-1,-2]

test_permute()