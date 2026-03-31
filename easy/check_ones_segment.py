class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # return '01' not in s
        if "01" in s:
            return False
        else:
            return True

def test_check_ones_segment():
    solution = Solution()

    # Test case 1
    s1 = "1001"
    print(solution.checkOnesSegment(s1))  # Expected output: False

    # Test case 2
    s2 = "110"
    print(solution.checkOnesSegment(s2))  # Expected output: True

    # Test case 3
    s3 = "101"
    print(solution.checkOnesSegment(s3))  # Expected output: False

    # Test case 4
    s4 = "1111"
    print(solution.checkOnesSegment(s4))  # Expected output: True

    # Test case 5
    s5 = "10101110110101"
    print(solution.checkOnesSegment(s5))  # Expected output: False

test_check_ones_segment()