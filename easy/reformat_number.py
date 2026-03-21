class Solution:
    def reformatNumber(self, number: str) -> str:
        new_num = "".join(number.replace("-", "").split())

        res = ""
        while len(new_num) > 0:
            if len(new_num) > 4:
                res += new_num[:3] + "-"
                new_num = new_num[3:]
            elif len(new_num) == 4:
                res += new_num[:2] + "-" + new_num[2:]
                new_num = ""
            else:
                res += new_num
                new_num = ""
        return res

def test_reformat_number():
    s = Solution()

    # Test Case 1
    number1 = "1-23-45 6"
    print(s.reformatNumber(number1)) # Expected Output: "123-456"

    # Test Case 2
    number2 = "123 4-567"
    print(s.reformatNumber(number2)) # Expected Output: "123-45-67"

    # Test Case 3
    number3 = "123 4-5678"
    print(s.reformatNumber(number3)) # Expected Output: "123-456-78"

    # Test Case 4
    number4 = "12"
    print(s.reformatNumber(number4)) # Expected Output: "12"

    # Test Case 5
    number5 = "--17-5 229 35-39475 "
    print(s.reformatNumber(number5)) # Expected Output: "175-229-353-94-75"

test_reformat_number()