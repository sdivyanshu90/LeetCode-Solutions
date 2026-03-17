class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0]  = 0
        if n >= 1:
            res[1] = 1
        for i in range(1, (n // 2) + 1):
            if 2 * i <= n:
                res[2 * i] = res[i]
            if 2 * i + 1 <= n:
                res[2 * i + 1] = res[i] + res[i + 1]
        
        return max(res)

def test_get_maximum_generated():
    solution = Solution()

    # Test case 1
    n1 = 7
    print(solution.getMaximumGenerated(n1))  # Expected output: 3

    # Test case 2
    n2 = 2
    print(solution.getMaximumGenerated(n2))  # Expected output: 9

    # Test case 3
    n3 = 3
    print(solution.getMaximumGenerated(n3))  # Expected output: 2

    # Test case 4
    n4 = 0
    print(solution.getMaximumGenerated(n4))  # Expected output: 0

    # Test case 5
    n5 = 15
    print(solution.getMaximumGenerated(n5))  # Expected output: 4

test_get_maximum_generated()