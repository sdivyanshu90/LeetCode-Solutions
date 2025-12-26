from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_frequency = {}

        for current_row in matrix:
            row_pattern = "".join(
                "T" if num == current_row[0] else "F" for num in current_row
            )

            pattern_frequency[row_pattern] = (
                pattern_frequency.get(row_pattern, 0) + 1
            )

        return max(pattern_frequency.values(), default=0)

def test_max_equal_rows_after_flips():
    solution = Solution()

    # Test case 1
    matrix1 = [[0, 1], [1, 1]]
    print(solution.maxEqualRowsAfterFlips(matrix1))  # Expected output: 1

    # Test case 2
    matrix2 = [[0, 1], [1, 0]]
    print(solution.maxEqualRowsAfterFlips(matrix2))  # Expected output: 2

    # Test case 3
    matrix3 = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(solution.maxEqualRowsAfterFlips(matrix3))  # Expected output: 2

    # Test case 4
    matrix4 = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    print(solution.maxEqualRowsAfterFlips(matrix4))  # Expected output: 4

    # Test case 5
    matrix5 = [[1]]
    print(solution.maxEqualRowsAfterFlips(matrix5))  # Expected output: 1

test_max_equal_rows_after_flips()