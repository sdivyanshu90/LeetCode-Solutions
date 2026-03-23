class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_row = [0] * n
        ans = 0
        
        for row in range(m):
            curr_row = matrix[row][:]
            for col in range(n):
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]

            sorted_row = sorted(curr_row, reverse=True)
            for i in range(n):
                ans = max(ans, sorted_row[i] * (i + 1))

            prev_row = curr_row

        return ans

def test_largest_submatrix():
    solution = Solution()

    # Test case 1
    matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
    print(solution.largestSubmatrix(matrix))  # Expected output: 4

    # Test case 2
    matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print(solution.largestSubmatrix(matrix))  # Expected output: 6

    # Test case 3
    matrix = [[0]]
    print(solution.largestSubmatrix(matrix))  # Expected output: 0

    # Test case 4
    matrix = [[1]]
    print(solution.largestSubmatrix(matrix))  # Expected output: 1

    # Test case 5
    matrix = [[0, 0], [0, 0]]
    print(solution.largestSubmatrix(matrix))  # Expected output: 0

test_largest_submatrix()