class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        MOD = 10 ** 9 + 7
        
        for i in range(2, n + 1):
            result *= i * (2 * i - 1) % MOD
            result %= MOD
        return result

def test_countOrders():
    solution = Solution()

    # Test case 1
    n1 = 1
    print(solution.countOrders(n1)) # Expected output: 1

    # Test case 2
    n2 = 2
    print(solution.countOrders(n2)) # Expected output: 6

    # Test case 3
    n3 = 3
    print(solution.countOrders(n3)) # Expected output: 90

    # Test case 4
    n4 = 4
    print(solution.countOrders(n4)) # Expected output: 2520

    # Test case 5
    n5 = 5
    print(solution.countOrders(n5)) # Expected output: 113400

test_countOrders()