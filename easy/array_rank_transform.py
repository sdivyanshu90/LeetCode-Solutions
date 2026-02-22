from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for i in range(len(sorted_arr)):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr

def test_arrayRankTransform():
    solution = Solution()

    # Test case 1
    arr = [40, 10, 20, 30]
    expected = [4, 1, 2, 3]
    print(solution.arrayRankTransform(arr))  # Expected Output: [4, 1, 2, 3]

    # Test case 2
    arr = [100, 100, 100]
    expected = [1, 1, 1]
    print(solution.arrayRankTransform(arr))  # Expected Output: [1, 1, 1]

    # Test case 3
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    expected = [5, 3, 4, 2, 8, 6, 7, 1, 3]
    print(solution.arrayRankTransform(arr))  # Expected Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]

    # Test case 4
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    print(solution.arrayRankTransform(arr))  # Expected Output: [1, 2, 3, 4, 5]

    # Test case 5
    arr = [5, 4, 3, 2, 1]
    expected = [5, 4, 3, 2, 1]
    print(solution.arrayRankTransform(arr))  # Expected Output: [5, 4, 3, 2, 1]

test_arrayRankTransform()