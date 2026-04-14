class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(val))

        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val

        return total_sum

def test_max_matrix_sum():
    solution = Solution()

    # Test case 1
    matrix1 = [[1, -1], [-1, 1]]
    print(solution.maxMatrixSum(matrix1))  # Expected output: 4

    # Test case 2
    matrix2 = [[1, 2, 3], [-1, -2, -3], [4, 5, 6]]
    print(solution.maxMatrixSum(matrix2))  # Expected output: 36

    # Test case 3
    matrix3 = [[-1]]
    print(solution.maxMatrixSum(matrix3))  # Expected output: 1

    # Test case 4
    matrix4 = [[-1, -2], [-3, -4]]
    print(solution.maxMatrixSum(matrix4))  # Expected output: 10

    # Test case 5
    matrix5 = [[0, -1], [1, -2]]
    print(solution.maxMatrixSum(matrix5))  # Expected output: 6

test_max_matrix_sum()