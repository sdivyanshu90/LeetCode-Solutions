class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        curra, currb, currc = 0, 0, 0

        total_iterations = a + b + c
        result = []

        for i in range(total_iterations):
            if (a >= b and a >= c and curra != 2) or (
                a > 0 and (currb == 2 or currc == 2)
            ):

                result.append("a")
                a -= 1
                curra += 1
                currb = 0
                currc = 0
            elif (b >= a and b >= c and currb != 2) or (
                b > 0 and (currc == 2 or curra == 2)
            ):

                result.append("b")
                b -= 1
                currb += 1
                curra = 0
                currc = 0
            elif (c >= a and c >= b and currc != 2) or (
                c > 0 and (curra == 2 or currb == 2)
            ):

                result.append("c")
                c -= 1
                currc += 1
                curra = 0
                currb = 0

        return "".join(result)

def test_longest_diverse_string():
    solution = Solution()

    # Test case 1
    a1, b1, c1 = 1, 1, 7
    print(solution.longestDiverseString(a1, b1, c1))  # Expected output: "ccaccbcc"

    # Test case 2
    a2, b2, c2 = 2, 2, 1
    print(solution.longestDiverseString(a2, b2, c2))  # Expected output: "aabbc"

    # Test case 3
    a3, b3, c3 = 7, 1, 0
    print(solution.longestDiverseString(a3, b3, c3))  # Expected output: "aabaa"

    # Test case 4
    a4, b4, c4 = 0, 0, 0
    print(solution.longestDiverseString(a4, b4, c4))  # Expected output: ""

    # Test case 5
    a5, b5, c5 = 3, 3, 3
    print(solution.longestDiverseString(a5, b5, c5))  # Expected output: "abcabcabc"

test_longest_diverse_string()