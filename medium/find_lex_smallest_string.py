from math import gcd

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = s
        visited = set()

        for shift in range(0, n, gcd(n, b)):
            rotated = s[-shift:] + s[:-shift]
            for add_times in range(10):
                temp = list(rotated)
                for i in range(1, n, 2):
                    temp[i] = str((int(temp[i]) + add_times * a) % 10)
                t = "".join(temp)
                res = min(res, t)
        return res

def test_find_lex_smallest_string():
    solution = Solution()

    # Test case 1
    s = "5525"
    a = 9
    b = 2
    print(solution.findLexSmallestString(s, a, b))  # Expected output: "2050"

    # Test case 2
    s = "74"
    a = 5
    b = 1
    print(solution.findLexSmallestString(s, a, b))  # Expected output: "42"

    # Test case 3
    s = "0011"
    a = 4
    b = 2
    print(solution.findLexSmallestString(s, a, b))  # Expected output: "0011"

    # Test case 4
    s = "43987654"
    a = 7
    b = 3
    print(solution.findLexSmallestString(s, a, b))  # Expected output: "30886645"

    # Test case 5
    s = "123456"
    a = 1
    b = 2
    print(solution.findLexSmallestString(s, a, b))  # Expected output: "103254"

test_find_lex_smallest_string()