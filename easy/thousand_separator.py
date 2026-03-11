class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        str_n = str(n)
        while len(str_n) > 0:
            res.append(str_n[-3:])
            str_n = str_n[:-3]

        return ".".join(res[::-1])

def test_thousand_separator():
    solution = Solution()

    # Test case 1
    n1 = 987
    print(solution.thousandSeparator(n1))  # Expected output: "987"

    # Test case 2
    n2 = 1234
    print(solution.thousandSeparator(n2))  # Expected output: "1.234"

    # Test case 3
    n3 = 123456789
    print(solution.thousandSeparator(n3))  # Expected output: "123.456.789"

    # Test case 4
    n4 = 0
    print(solution.thousandSeparator(n4))  # Expected output: "0"

    # Test case 5
    n5 = 1000000
    print(solution.thousandSeparator(n5))  # Expected output: "1.000.000"

test_thousand_separator()