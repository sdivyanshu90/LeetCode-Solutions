from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")

        res = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i-1], arr[i]]]
            elif diff == min_diff:
                res.append([arr[i- 1], arr[i]])
        return res

def test_minimum_abs_difference():
    solution = Solution()

    # Test Case 1
    arr1 = [4, 2, 1, 3]
    print(solution.minimumAbsDifference(arr1))  # Expected Output: [[1, 2], [2, 3], [3, 4]]

    # Test Case 2
    arr2 = [1, 3, 6, 10, 15]
    print(solution.minimumAbsDifference(arr2))  # Expected Output: [[1, 3]]

    # Test Case 3
    arr3 = [3, 8, -10, 23, 19, 17, 15, 11, -4, 27]
    print(solution.minimumAbsDifference(arr3))  # Expected Output: [[15, 17], [17, 19]]

    # Test Case 4
    arr4 = [40, 11, 26, 27, -20]
    print(solution.minimumAbsDifference(arr4))  # Expected Output: [[26, 27]]

    # Test Case 5
    arr5 = [1, 1000000]
    print(solution.minimumAbsDifference(arr5))  # Expected Output: [[1, 1000000]]

test_minimum_abs_difference()