from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0

        for current_operation in logs:
            if current_operation == "../":
                folder_depth = max(0, folder_depth - 1)
            elif current_operation != "./":
                folder_depth += 1

        return folder_depth

def test_min_operations():
    solution = Solution()

    # Test case 1
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    print(solution.minOperations(logs))  # Expected output: 2

    # Test case 2
    logs = ["d1/", "d2/", "d3/", "../", "d31/", "./"]
    print(solution.minOperations(logs))  # Expected output: 3

    # Test case 3
    logs = ["d1/", "../", "../", "../"]
    print(solution.minOperations(logs))  # Expected output: 0

    # Test case 4
    logs = ["./", "./", "./"]
    print(solution.minOperations(logs))  # Expected output: 0

    # Test case 5
    logs = ["d1/", "d2/", "d3/"]
    print(solution.minOperations(logs))  # Expected output: 3

test_min_operations()