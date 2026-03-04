class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)

        if len(factors) < k:
            return -1
        else:
            return factors[k - 1])

def test_kth_factor():
    solution = Solution()

    # Test Case 1
    n1 = 12
    k1 = 3
    print(solution.kthFactor(n1, k1))  # Expected output: 3

    # Test Case 2
    n2 = 7
    k2 = 2
    print(solution.kthFactor(n2, k2))  # Expected output: 7

    # Test Case 3
    n3 = 4
    k3 = 4
    print(solution.kthFactor(n3, k3))  # Expected output: -1

    # Test Case 4
    n4 = 1
    k4 = 1
    print(solution.kthFactor(n4, k4))  # Expected output: 1

    # Test Case 5
    n5 = 100
    k5 = 9
    print(solution.kthFactor(n5, k5))  # Expected output: 25

test_kth_factor()