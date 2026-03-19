class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = ""
        for i in range(1, n + 1):
            temp = bin(i)[2:]
            res += temp

        return int(res, 2) % MOD

def test_concatenated_binary():
    solution = Solution()

    # Test case 1
    n = 1
    print(solution.concatenatedBinary(n))  # Expected output: 1

    # Test case 2
    n = 3
    print(solution.concatenatedBinary(n))  # Expected output: 27

    # Test case 3
    n = 12
    print(solution.concatenatedBinary(n))  # Expected output: 505379714

    # Test case 4
    n = 1000
    print(solution.concatenatedBinary(n))  # Expected output: 499361981

    # Test case 5
    n = 100000
    print(solution.concatenatedBinary(n))  # Expected output: 757631812

test_concatenated_binary()