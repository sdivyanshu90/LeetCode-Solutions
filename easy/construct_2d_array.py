class Solution:
    def construct2DArray(
        self, original: list[int], m: int, n: int
    ) -> list[list[int]]:
        if m * n != len(original):
            return []

        result_array = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            result_array[i // n][i % n] = original[i]

        return result_array

def test_construct_2d_array():
    solution = Solution()

    # Test case 1
    original1 = [1, 2, 3, 4]
    m1, n1 = 2, 2
    print(solution.construct2DArray(original1, m1, n1))  # Expected output: [[1, 2], [3, 4]]

    # Test case 2
    original2 = [1, 2, 3]
    m2, n2 = 1, 3
    print(solution.construct2DArray(original2, m2, n2))  # Expected output: [[1, 2, 3]]

    # Test case 3
    original3 = [1, 2]
    m3, n3 = 1, 1
    print(solution.construct2DArray(original3, m3, n3))  # Expected output: []

    # Test case 4
    original4 = [1]
    m4, n4 = 1, 1
    print(solution.construct2DArray(original4, m4, n4))  # Expected output: [[1]]

    # Test case 5
    original5 = [1, 2, 3, 4]
    m5, n5 = 4, 1
    print(solution.construct2DArray(original5, m5, n5))  # Expected output: [[1], [2], [3], [4]]

test_construct_2d_array()