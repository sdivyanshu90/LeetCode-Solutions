class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)

        while k > 0:
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            numeric_string = str(digit_sum)
            k -= 1

        return int(numeric_string)

def test_get_lucky():
    solution = Solution()

    # Test Case 1
    s1 = "iiii"
    k1 = 1
    print(solution.getLucky(s1, k1))  # Expected output: 36

    # Test Case 2
    s2 = "leetcode"
    k2 = 2
    print(solution.getLucky(s2, k2))  # Expected output: 6

    # Test Case 3
    s3 = "abc"
    k3 = 1
    print(solution.getLucky(s3, k3))  # Expected output: 6

    # Test Case 4
    s4 = "z"
    k4 = 1
    print(solution.getLucky(s4, k4))  # Expected output: 8

    # Test Case 5
    s5 = "hello"
    k5 = 3
    print(solution.getLucky(s5, k5))  # Expected output: 7

test_get_lucky()