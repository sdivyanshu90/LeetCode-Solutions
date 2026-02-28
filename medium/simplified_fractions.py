from typing import List
from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{a}/{b}" for b in range(2, n + 1) for a in range(1, b) if gcd(a, b) == 1]

def test_simplified_fractions():
    solution = Solution()

    # Test case 1
    n1 = 2
    print(solution.simplifiedFractions(n1))  # Expected output: ["1/2"]

    # Test case 2
    n2 = 3
    print(solution.simplifiedFractions(n2))  # Expected output: ["1/2", "1/3", "2/3"]

    # Test case 3
    n3 = 4
    print(solution.simplifiedFractions(n3))  # Expected output: ["1/2", "1/3", "1/4", "2/3", "3/4"]

    # Test case 4
    n4 = 5
    print(solution.simplifiedFractions(n4))  # Expected output: ["1/2", "1/3", "1/4", "1/5", "2/3", "2/5", "3/4", "3/5", "4/5"]

    # Test case 5
    n5 = 6
    print(solution.simplifiedFractions(n5))  # Expected output: ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6']

test_simplified_fractions()