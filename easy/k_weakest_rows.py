from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def sorting_key(row_index):
            num_soldiers = sum(mat[row_index])
            return (num_soldiers, row_index)

        rows = list(range(len(mat)))
        sorted_rows = sorted(rows, key=sorting_key)
        result = sorted_rows[:k]
        return result

def test_k_weakest_rows():
    solution = Solution()

    # Test case 1
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
    k = 3
    expected = [2, 0, 3]
    print(solution.kWeakestRows(mat, k))  # Expected Output: [2, 0, 3]

    # Test case 2
    mat = [[1, 0], [0, 0], [1, 0], [1, 1], [1, 0]]
    k = 2
    expected = [1, 2]
    print(solution.kWeakestRows(mat, k))  # Expected Output: [1, 2]

    # Test case 3
    mat = [[1, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0], [1, 0, 0]]
    k = 4
    expected = [3, 1, 4, 0]
    print(solution.kWeakestRows(mat, k))  # Expected Output: [3, 1, 4, 0]

    # Test case 4
    mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    k = 3
    expected = [0, 1, 2]
    print(solution.kWeakestRows(mat, k))  # Expected Output: [0, 1, 2]

    # Test case 5
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    k = 2
    expected = [0, 1]
    print(solution.kWeakestRows(mat, k))  # Expected Output: [0, 1]

test_k_weakest_rows()