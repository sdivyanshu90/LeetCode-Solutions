class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
            
        return ""

def test_largest_odd_number():
    solution = Solution()

    # Test case 1
    num = "52"
    print(solution.largestOddNumber(num))  # Expected output: "5"

    # Test case 2
    num = "4206"
    print(solution.largestOddNumber(num))  # Expected output: ""

    # Test case 3
    num = "35427"
    print(solution.largestOddNumber(num))  # Expected output: "35427"

    # Test case 4
    num = "1234567890"
    print(solution.largestOddNumber(num))  # Expected output: "123456789"

    # Test case 5
    num = "24680"
    print(solution.largestOddNumber(num))  # Expected output: ""

test_largest_odd_number()