class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))

def test_maximum69Number():
    solution = Solution()

    # Test case 1
    num = 9669
    expected = 9969
    print(solution.maximum69Number(num))  # Expected Output: 9969

    # Test case 2
    num = 9996
    expected = 9999
    print(solution.maximum69Number(num))  # Expected Output: 9999

    # Test case 3
    num = 9999
    expected = 9999
    print(solution.maximum69Number(num))  # Expected Output: 9999

    # Test case 4
    num = 6969
    expected = 9969
    print(solution.maximum69Number(num))  # Expected Output: 9969

    # Test case 5
    num = 6666
    expected = 9666
    print(solution.maximum69Number(num))  # Expected Output: 9666

test_maximum69Number()