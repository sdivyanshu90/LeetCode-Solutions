class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                c_sq = a**2 + b ** 2
                c = int(c_sq**0.5)
                if c > n:
                    continue
                if c*c == c_sq:
                    res += 2

        return res

def test_count_triples():
    solution = Solution()

    # Test case 1
    n1 = 5
    print(solution.countTriples(n1))  # Expected output: 2

    # Test case 2
    n2 = 10
    print(solution.countTriples(n2))  # Expected output: 4

    # Test case 3
    n3 = 15
    print(solution.countTriples(n3))  # Expected output: 8

    # Test case 4
    n4 = 20
    print(solution.countTriples(n4))  # Expected output: 12

    # Test case 5
    n5 = 199
    print(solution.countTriples(n5))  # Expected output: 16

test_count_triples()