from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        even_idx = 0
        odd_idx = 1
        
        for num in nums:
            if num % 2 == 0:
                res[even_idx] = num
                even_idx += 2
            else:
                res[odd_idx] = num
                odd_idx += 2
                
        return res

def test_sort_array_by_parity_ii():
    solution = Solution()

    # Test Case 1
    print(solution.sortArrayByParityII([4,2,5,7])) # Expected: [4,5,2,7]

    # Test Case 2
    print(solution.sortArrayByParityII([2,3])) # Expected: [2,3]

    # Test Case 3
    print(solution.sortArrayByParityII([1,0,1,0])) # Expected: [0,1,0,1]

    # Test Case 4
    print(solution.sortArrayByParityII([3,1,4,2])) # Expected: [4,3,2,1]

    # Test Case 5
    print(solution.sortArrayByParityII([0,1,2,3,4,5])) # Expected: [0,1,2,3,4,5]

test_sort_array_by_parity_ii()