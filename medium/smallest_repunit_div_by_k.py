class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 0
        for length_N in range(1 ,K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length_N
        return -1

def test_smallest_repunit_div_by_k():
    solution = Solution()

    # Test case 1
    K1 = 1
    print(solution.smallestRepunitDivByK(K1))  # Expected output: 1

    # Test case 2
    K2 = 2
    print(solution.smallestRepunitDivByK(K2))  # Expected output: -1

    # Test case 3
    K3 = 3
    print(solution.smallestRepunitDivByK(K3))  # Expected output: 3

    # Test case 4
    K4 = 7
    print(solution.smallestRepunitDivByK(K4))  # Expected output: 6

    # Test case 5
    K5 = 23
    print(solution.smallestRepunitDivByK(K5))  # Expected output: 22

test_smallest_repunit_div_by_k()