from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

def test_combination_sum_4():
    solution = Solution()
    
    # Test case 1
    print(solution.combinationSum4([1,2,3], 4)) # Expected output: 7
    
    # Test case 2
    print(solution.combinationSum4([9], 3)) # Expected output: 0

    # Test case 3: Edge case - single element equal to target
    print(solution.combinationSum4([4], 4)) # Expected output: 1

    # Test case 4: Multiple combinations
    print(solution.combinationSum4([2,3,5], 8)) # Expected output: 6
    
    # Test case 5: No combinations possible
    print(solution.combinationSum4([5,6], 3)) # Expected output: 0

    # Test case 6: Large target with small numbers
    print(solution.combinationSum4([1,2], 10)) # Expected output: 89

    # Test case 7: Large numbers in nums
    print(solution.combinationSum4([10,20,30], 60)) # Expected output: 24

    # Test case 8: Empty nums array
    print(solution.combinationSum4([], 5)) # Expected output: 0

    # Test case 9: Target is zero
    print(solution.combinationSum4([1,2,3], 0)) # Expected output: 1

    # Test case 10: Large nums array
    print(solution.combinationSum4(list(range(1, 21)), 25)) # Expected output: 16777168


test_combination_sum_4()