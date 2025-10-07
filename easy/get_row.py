from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res

def test_get_row():
    solution = Solution()

    # Test case 1: rowIndex = 3
    print(solution.getRow(3))  # Expected output: [1, 3, 3, 1]

    # Test case 2: rowIndex = 0
    print(solution.getRow(0))  # Expected output: [1]

    # Test case 3: rowIndex = 1
    print(solution.getRow(1))  # Expected output: [1, 1]

    # Test case 4: rowIndex = 4
    print(solution.getRow(4))  # Expected output: [1, 4, 6, 4, 1]

    # Test case 5: rowIndex = 5
    print(solution.getRow(5))  # Expected output: [1, 5, 10, 10, 5, 1]

test_get_row()