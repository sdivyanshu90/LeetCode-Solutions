from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, curr):
            if curr == target:
                res.append(path.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if curr + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, curr + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res

def test_combination_sum2():
    solution = Solution()

    # Test case 1: Regular case with duplicates
    print(solution.combinationSum2([10,1,2,7,6,1,5], 8))  # Expected output: [[1,1,6],[1,2,5],[1,7],[2,6]]

    # Test case 2: No possible combinations
    print(solution.combinationSum2([2,4,6], 5))  # Expected output: []

    # Test case 3: All elements the same
    print(solution.combinationSum2([1,1,1,1], 2))  # Expected output: [[1,1]]

    # Test case 4: Single element equal to target
    print(solution.combinationSum2([3], 3))  # Expected output: [[3]]

    # Test case 5: Single element not equal to target
    print(solution.combinationSum2([4], 3))  # Expected output: []

    # Test case 6: Empty candidates list
    print(solution.combinationSum2([], 7))  # Expected output: []

    # Test case 7: Larger input with some duplicates
    print(solution.combinationSum2([1,2,3,4,5,6,7,8,9,10]*2, 15))  # Expected output: Various combinations summing to 15

    # Test case 8: Negative and positive integers (should handle only positive as per problem constraints)
    print(solution.combinationSum2([-1,0,1,2], 1))  # Expected output: [[-1, 0, 2], [-1, 2], [0, 1], [1]]

    # Test case 9: Larger input with all elements the same
    print(solution.combinationSum2([5]*20, 10))  # Expected output: [[5,5]]

    # Test case 10: Mixed integers with multiple duplicates
    print(solution.combinationSum2([1,1,2,2,3,3], 4))  # Expected output: [[1,1,2],[1,3],[2,2]]

test_combination_sum2()