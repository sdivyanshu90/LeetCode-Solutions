class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_array = []
        result = float("inf")

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] % x != grid[0][0] % x:
                    return -1
                nums_array.append(grid[row][col])

        nums_array.sort()

        length = len(nums_array)
        prefix_sum = [0] * length
        suffix_sum = [0] * length

        for index in range(1, length):
            prefix_sum[index] = prefix_sum[index - 1] + nums_array[index - 1]

        for index in range(length - 2, -1, -1):
            suffix_sum[index] = suffix_sum[index + 1] + nums_array[index + 1]

        for index in range(length):
            left_operations = (
                nums_array[index] * index - prefix_sum[index]
            ) // x
            right_operations = (
                suffix_sum[index] - nums_array[index] * (length - index - 1)
            ) // x
            result = min(result, left_operations + right_operations)

        return result

def test_min_operations():
    solution = Solution()

    # Test case 1
    grid1 = [[2, 4], [6, 8]]
    x1 = 2
    print(solution.minOperations(grid1, x1))  # Expected output: 4

    # Test case 2
    grid2 = [[1, 2], [3, 4]]
    x2 = 2
    print(solution.minOperations(grid2, x2))  # Expected output: -1

    # Test case 3
    grid3 = [[1, 3], [5, 7]]
    x3 = 2
    print(solution.minOperations(grid3, x3))  # Expected output: 4

    # Test case 4
    grid4 = [[10, 20], [30, 40]]
    x4 = 10
    print(solution.minOperations(grid4, x4))  # Expected output: 6

    # Test case 5
    grid5 = [[1, 1], [1, 1]]
    x5 = 1
    print(solution.minOperations(grid5, x5))  # Expected output: 0

test_min_operations()