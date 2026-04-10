class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def quickmul(x: int, y: int) -> int:
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret

        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod

def test_count_good_numbers():
    solution = Solution()

    # Test case 1
    n1 = 1
    print(solution.countGoodNumbers(n1))  # Expected output: 5

    # Test case 2
    n2 = 4
    print(solution.countGoodNumbers(n2))  # Expected output: 400

    # Test case 3
    n3 = 50
    print(solution.countGoodNumbers(n3))  # Expected output: 564908303

    # Test case 4
    n4 = 100
    print(solution.countGoodNumbers(n4))  # Expected output: 564490093

    # Test case 5
    n5 = 99999999999999999
    print(solution.countGoodNumbers(n5))  # Expected output: 958203099

test_count_good_numbers()