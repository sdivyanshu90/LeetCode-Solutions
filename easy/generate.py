from math import factorial
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                res[i].append(factorial(i) // (factorial(j) * factorial(i-j)))
        return res

def test_generate():
    solution = Solution()

    # Test case 1: numRows = 5
    print(solution.generate(5))  # Expected output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    # Test case 2: numRows = 1
    print(solution.generate(1))  # Expected output: [[1]]

    # Test case 3: numRows = 0
    print(solution.generate(0))  # Expected output: []

    # Test case 4: numRows = 3
    print(solution.generate(3))  # Expected output: [[1], [1, 1], [1, 2, 1]]

    # Test case 5: numRows = 6
    print(solution.generate(6))  # Expected output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]]

test_generate()