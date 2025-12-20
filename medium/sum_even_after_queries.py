from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        res = []
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            res.append(even_sum)
        return res

def test_sum_even_after_queries():
    solution = Solution()
    
    # Test case 1
    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    print(solution.sumEvenAfterQueries(nums, queries))  # Expected output: [8,6,2,4]

    # Test case 2
    nums = [0]
    queries = [[4,0],[3,0],[-2,0],[1,0]]
    print(solution.sumEvenAfterQueries(nums, queries))  # Expected output: [4,0,2,2]

    # Test case 3
    nums = [2,10,8]
    queries = [[5,1],[-5,0],[5,2],[-10,1]]
    print(solution.sumEvenAfterQueries(nums, queries))  # Expected output: [10,8,13,3]

    # Test case 4
    nums = [1,3,5]
    queries = [[2,1],[4,0],[6,2]]
    print(solution.sumEvenAfterQueries(nums, queries))  # Expected output: [0,4,10]

    # Test case 5
    nums = [-2,0,4]
    queries = [[3,0],[-1,1],[2,2],[-3,0]]
    print(solution.sumEvenAfterQueries(nums, queries))  # Expected output: [4,4,6,0]

test_sum_even_after_queries()