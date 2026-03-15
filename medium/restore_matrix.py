from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)

        curr_row_sum = [0] * N
        curr_col_sum = [0] * M

        orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                orig_matrix[i][j] = min(
                    rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j]
                )

                curr_row_sum[i] += orig_matrix[i][j]
                curr_col_sum[j] += orig_matrix[i][j]

        return orig_matrix

def test_restore_matrix():
    solution = Solution()

    # Test case 1
    rowSum = [3, 8]
    colSum = [4, 7]
    print(solution.restoreMatrix(rowSum, colSum))  # Expected output: [[3, 0], [1, 7]]

    # Test case 2
    rowSum = [5, 7, 10]
    colSum = [8, 6, 8]
    print(solution.restoreMatrix(rowSum, colSum))  # Expected output: [[5, 0, 0], [3, 4, 0], [0, 2, 8]]

    # Test case 3
    rowSum = [14, 9]
    colSum = [6, 9, 8]
    print(solution.restoreMatrix(rowSum, colSum))  # Expected output: [[6, 8, 0], [0, 1, 8]]

    # Test case 4
    rowSum = [1, 0]
    colSum = [1, 0]
    print(solution.restoreMatrix(rowSum, colSum))  # Expected output: [[1, 0], [0, 0]]

    # Test case 5
    rowSum = [0, 0]
    colSum = [0, 0]
    print(solution.restoreMatrix(rowSum, colSum))  # Expected output: [[0, 0], [0, 0]]

test_restore_matrix()