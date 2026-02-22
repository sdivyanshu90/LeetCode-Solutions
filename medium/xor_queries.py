class Solution:
    def xorQueries(self, arr, queries):
        result = []

        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        for left, right in queries:
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])

        return result

def test_xorQueries():
    solution = Solution()

    # Test case 1
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3]]
    expected = [2, 7, 14]
    print(solution.xorQueries(arr, queries))  # Expected Output: [2, 7, 14]

    # Test case 2
    arr = [4, 8, 2, 10]
    queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
    expected = [8, 0, 4, 4]
    print(solution.xorQueries(arr, queries))  # Expected Output: [8, 0, 4, 4]

    # Test case 3
    arr = [1, 2, 3, 4, 5]
    queries = [[0, 4], [1, 3], [2, 2]]
    expected = [1, 5, 3]
    print(solution.xorQueries(arr, queries))  # Expected Output: [1, 5, 3]

    # Test case 4
    arr = [5, 6, 7, 8, 9]
    queries = [[0, 2], [1, 4], [0, 4]]
    expected = [4, 14, 1]
    print(solution.xorQueries(arr, queries))  # Expected Output: [4, 0, 5]

    # Test case 5
    arr = [10, 11, 12, 13, 14]
    queries = [[0, 1], [2, 3], [1, 4]]
    expected = [1, 1, 3]
    print(solution.xorQueries(arr, queries))  # Expected Output: [1, 1, 4]

test_xorQueries()