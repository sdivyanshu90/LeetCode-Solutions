from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def backtrack(index):
            if index == len(nums):
                results.append(nums[:])
                return
            
            used = set()
            
            for i in range(index, len(nums)):
                if nums[i] not in used:
                    nums[i], nums[index] = nums[index], nums[i]
                    backtrack(index + 1)
                    nums[i], nums[index] = nums[index], nums[i]
                    used.add(nums[i])

        backtrack(0)
        return results

def test_permute_unique():
    solution = Solution()
    
    # Test case 1: Regular case with duplicates
    print(solution.permuteUnique([1,1,2]))  # Expected output: [[1,1,2],[1,2,1],[2,1,1]]
    
    # Test case 2: All elements the same
    print(solution.permuteUnique([2,2,2]))  # Expected output: [[2,2,2]]

    # Test case 3: No duplicates
    print(solution.permuteUnique([1,2,3]))  # Expected output: All permutations of [1,2,3]

    # Test case 4: Single element
    print(solution.permuteUnique([1]))  # Expected output: [[1]]

    # Test case 5: Empty list
    print(solution.permuteUnique([]))  # Expected output: [[]]

    # Test case 6: Larger input with some duplicates
    print(solution.permuteUnique([1,2,2,3]))  # Expected output: All unique permutations of [1,2,2,3]

    # Test case 7: Negative and positive integers with duplicates
    print(solution.permuteUnique([-1,0,-1]))  # Expected output: [[-1,-1,0],[-1,0,-1],[0,-1,-1]]

    # Test case 8: Larger input with all elements the same
    print(solution.permuteUnique([3,3,3,3]))  # Expected output: [[3,3,3,3]]

    # Test case 9: Mixed integers with multiple duplicates
    print(solution.permuteUnique([1,1,2,2]))  # Expected output: All unique permutations of [1,1,2,2]

    # Test case 10: Larger range of integers with some duplicates
    print(solution.permuteUnique([0,-1,-1,0]))  # Expected output: All unique permutations of [0,-1,-1,0]

test_permute_unique()