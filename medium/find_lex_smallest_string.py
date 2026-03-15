from math import gcd
from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        res = s
        n = len(s)

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            res = min(res, cur)

            lst = list(cur)
            for i in range(1, n, 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            added = "".join(lst)

            rotated = cur[-b:] + cur[:-b]

            if added not in seen:
                q.append(added)
            if rotated not in seen:
                q.append(rotated)
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