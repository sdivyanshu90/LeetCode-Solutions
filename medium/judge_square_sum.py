class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)
        while a <= b:
            m = a * a + b * b
            if m == c:
                return True
            elif m > c:
                b -= 1
            else:
                a += 1
        return False

def test_judge_square_sum():
    s = Solution()

    # Test case 1
    c = 5
    print(s.judgeSquareSum(c))  # Expected output: True

    # Test case 2
    c = 3
    print(s.judgeSquareSum(c))  # Expected output: False

    # Test case 3
    c = 4
    print(s.judgeSquareSum(c))  # Expected output: True

    # Test case 4
    c = 2
    print(s.judgeSquareSum(c))  # Expected output: True

    # Test case 5
    c = 1
    print(s.judgeSquareSum(c))  # Expected output: True

test_judge_square_sum()