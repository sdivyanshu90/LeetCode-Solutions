from typing import List

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        current_string = ""
        happy_strings = []
        self.generate_happy_strings(n, current_string, happy_strings)

        if len(happy_strings) < k:
            return ""

        happy_strings.sort()
        return happy_strings[k - 1]

    def generate_happy_strings(
        self, n: int, current_string: str, happy_strings: list
    ):
        if len(current_string) == n:
            happy_strings.append(current_string)
            return

        for current_char in ["a", "b", "c"]:
            if len(current_string) > 0 and current_string[-1] == current_char:
                continue

            self.generate_happy_strings(
                n, current_string + current_char, happy_strings
            )

def test_get_happy_string():
    solution = Solution()

    # Test case 1
    n1 = 1
    k1 = 3
    print(solution.getHappyString(n1, k1))  # Expected output: "c"

    # Test case 2
    n2 = 1
    k2 = 4
    print(solution.getHappyString(n2, k2))  # Expected output: ""

    # Test case 3
    n3 = 3
    k3 = 9
    print(solution.getHappyString(n3, k3))  # Expected output: "cab"

    # Test case 4
    n4 = 2
    k4 = 7
    print(solution.getHappyString(n4, k4))  # Expected output: ""

    # Test case 5
    n5 = 10
    k5 = 100
    print(solution.getHappyString(n5, k5))  # Expected output: "abacbabacb"

test_get_happy_string()