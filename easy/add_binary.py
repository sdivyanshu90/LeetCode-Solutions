class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (f"{int(a, 2) + int(b, 2):b}")

def test_add_binary():
    solution = Solution()
    # Test Case 1
    print(solution.addBinary("11", "1"))  # Expected output: "100"
    # Test Case 2
    print(solution.addBinary("1010", "1011"))  # Expected output: "10101"
    # Test Case 3
    print(solution.addBinary("0", "0"))  # Expected output: "0"
    # Test Case 4
    print(solution.addBinary("111", "111"))  # Expected output: "1110"
    # Test Case 5
    print(solution.addBinary("1", "111"))  # Expected output: "1000"
    # Test Case 6
    print(solution.addBinary("1101", "101"))  # Expected output: "10010"
    # Test Case 7
    print(solution.addBinary("100", "110010"))  # Expected output: "110110"
    # Test Case 8
    print(solution.addBinary("1111111", "1"))  # Expected output: "10000000"
    # Test Case 9
    print(solution.addBinary("101010", "110011"))  # Expected output: "1011101"
    # Test Case 10
    print(solution.addBinary("0", "111111"))  # Expected output: "111111"

test_add_binary()