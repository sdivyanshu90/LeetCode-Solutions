from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        n = len(arr)
        dp = [1] * n
        
        index = {x: i for i, x in enumerate(arr)}
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    div = arr[i] // arr[j]
                    if div in index:
                        dp[i] += dp[j] * dp[index[div]]
                        dp[i] %= mod
        
        return sum(dp) % mod

def test_num_factored_binary_trees():
    solution = Solution()

    # Test Case 1
    arr1 = [2,4]
    print(solution.numFactoredBinaryTrees(arr1)) # Expected: 3

    # Test Case 2
    arr2 = [2,4,5,10]
    print(solution.numFactoredBinaryTrees(arr2)) # Expected: 7

    # Test Case 3
    arr3 = [18,3,6,2]
    print(solution.numFactoredBinaryTrees(arr3)) # Expected: 6

    # Test Case 4
    arr4 = [15,5,3,30,6,10,2]
    print(solution.numFactoredBinaryTrees(arr4)) # Expected: 27

    # Test Case 5
    arr5 = [8,4,6,2]
    print(solution.numFactoredBinaryTrees(arr5)) # Expected: 6

test_num_factored_binary_trees()