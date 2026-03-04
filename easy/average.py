from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return round(sum(salary[1: len(salary) - 1]) / (len(salary) - 2), 5)

def test_average():
    solution = Solution()

    # Test Case 1
    salary1 = [4000, 3000, 1000, 2000]
    print(solution.average(salary1))  # Expected output: 2500.00000

    # Test Case 2
    salary2 = [1000, 2000, 3000]
    print(solution.average(salary2))  # Expected output: 2000.00000

    # Test Case 3
    salary3 = [6000, 5000, 4000, 3000, 2000, 1000]
    print(solution.average(salary3))  # Expected output: 3500.00000

    # Test Case 4
    salary4 = [8000, 9000, 10000]
    print(solution.average(salary4))  # Expected output: 9000.00000

    # Test Case 5
    salary5 = [5000, 4000, 3000, 2000, 1000]
    print(solution.average(salary5))  # Expected output: 3000.00000

test_average()