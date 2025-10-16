from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Method 1
        nums.insert(0, 1)
        nums.append(1)
        def recursive(i, j, memo):
            if i == j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_cost = float("-inf")
            for k in range(i, j):
                curr_cost = nums[i - 1] * nums[k] * nums[j]
                left_cost = recursive(i, k, memo)
                right_cost = recursive(k + 1, j, memo)
                max_cost = max(max_cost, curr_cost + left_cost + right_cost)
            memo[(i, j)] = max_cost
            return max_cost
        return recursive(1, len(nums) - 1, {})


        # Method 2
        # nums.insert(0, 1)
        # nums.append(1)
        # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        # for i in range(len(nums)):
        #     for j in range(len(nums) - i):
        #         k = i + j
        #         res = 0
        #         for a in range(j + 1, k):
        #             coins = nums[j] * nums[k] * nums[a]
        #             res = max(res, coins + dp[j][a] + dp[a][k])
        #         dp[j][k] = res
        # return dp[0][len(nums) - 1]

def test_max_coins():
    s = Solution()

    # Test Case 1: Example with simple array of balloon values
    nums = [3, 1, 5, 8]
    print(s.maxCoins(nums))  # Expected: 167

    # Test Case 2: Array with a single balloon
    nums = [1]
    print(s.maxCoins(nums))  # Expected: 1

    # Test Case 3: Array with two balloons
    nums = [1, 2]
    print(s.maxCoins(nums))  # Expected: 4 (since we have only two balloons, the answer is nums[0] * nums[1])

    # Test Case 4: Array with identical values
    nums = [3, 3, 3, 3]
    print(s.maxCoins(nums))  # Expected: 66 

    # Test Case 5: Array with descending values
    nums = [5, 4, 3, 2, 1]
    print(s.maxCoins(nums))  # Expected: 110 

    # Test Case 6: Array with a mix of large and small numbers
    nums = [1, 10, 1, 5, 4]
    print(s.maxCoins(nums))  # Expected: 310

    # Test Case 7: Empty array (edge case)
    nums = []
    print(s.maxCoins(nums))  # Expected: 0 (if no balloons, no coins)

    # Test Case 8: Large array with random numbers to test performance
    nums = [2, 4, 3, 5, 6, 2, 1]
    print(s.maxCoins(nums))  # Expected: 264

    # Test Case 9: Array with a balloon value of 1 (testing edge cases where 1 might be optimal to use)
    nums = [1, 1, 1, 1, 1]
    print(s.maxCoins(nums))  # Expected: 5 

    # Test Case 10:
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(s.maxCoins(nums)) # Expected: 2420

test_max_coins()