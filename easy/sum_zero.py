from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
    
        if n % 2 == 0:
            half = n // 2
            for i in range(1, half + 1):
                result.append(-i)
                result.append(i)
        else:
            half = n // 2
            for i in range(half):
                result.append(-i - 1)
            result.append(0)
            for i in range(half):
                result.append(i + 1)
        return result

def test_sum_zero():
    solution = Solution()
    
    # Test case 1
    n = 5
    expected = [-2, -1, 0, 1, 2]
    print(solution.sumZero(n))  # Expected Output: [-1, -2, 0, 1, 2]

    # Test case 2
    n = 3
    expected = [-1, 0, 1]
    print(solution.sumZero(n))  # Expected Output: [-1, 0, 1]

    # Test case 3
    n = 1
    expected = [0]
    print(solution.sumZero(n))  # Expected Output: [0]

    # Test case 4
    n = 4
    expected = [-2, -1, 1, 2]
    print(solution.sumZero(n))  # Expected Output: [-1, 1, -2, 2]

    # Test case 5
    n = 6
    expected = [-3, -2, -1, 1, 2, 3]
    print(solution.sumZero(n))  # Expected Output: [-1, 1, -2, 2, -3, 3]

test_sum_zero()