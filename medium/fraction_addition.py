import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1

        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))

        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])

            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        num //= gcd
        denom //= gcd

        return str(num) + "/" + str(denom)

    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)

def test_fraction_addition():
    s = Solution()

    # Test case 1
    expression1 = "-1/2+1/2"
    print(s.fractionAddition(expression1)) # Expected output: "0/1"

    # Test case 2
    expression2 = "-1/2+1/2+1/3"
    print(s.fractionAddition(expression2)) # Expected output: "1/3"

    # Test case 3
    expression3 = "1/3-1/2"
    print(s.fractionAddition(expression3)) # Expected output: "-1/6"

    # Test case 4
    expression4 = "5/3+1/3"
    print(s.fractionAddition(expression4)) # Expected output: "2/1"

    # Test case 5
    expression5 = "-2/3-1/6+1/2"
    print(s.fractionAddition(expression5)) # Expected output: "-1/3"

test_fraction_addition()