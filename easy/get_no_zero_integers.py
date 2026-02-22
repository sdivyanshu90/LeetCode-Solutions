from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]

def test_get_no_zero_integers():
    solution = Solution()

    # Test case 1
    n = 2
    expected = [1, 1]
    print(solution.getNoZeroIntegers(n))  # Expected Output: [1, 1]

    # Test case 2
    n = 11
    expected = [2, 9]
    print(solution.getNoZeroIntegers(n))  # Expected Output: [2, 9]

    # Test case 3
    n = 10000
    expected = [1, 9999]
    print(solution.getNoZeroIntegers(n))  # Expected Output: [1, 9999]

    # Test case 4
    n = 69
    expected = [1, 68]
    print(solution.getNoZeroIntegers(n))  # Expected Output: [1, 68]

    # Test case 5
    n = 1010
    expected = [11, 999]
    print(solution.getNoZeroIntegers(n))  # Expected Output: [11, 999]

test_get_no_zero_integers()