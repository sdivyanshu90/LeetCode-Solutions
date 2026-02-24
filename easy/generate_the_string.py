class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a" * (n - 1) + "b"
        else:
            return "a" * n

def test_generateTheString():
    solution = Solution()

    # Test case 1
    n1 = 4
    print(solution.generateTheString(n1)) # Expected output: "aaab"

    # Test case 2
    n2 = 2
    print(solution.generateTheString(n2)) # Expected output: "ab"

    # Test case 3
    n3 = 7
    print(solution.generateTheString(n3)) # Expected output: "aaaaaaa"

    # Test case 4
    n4 = 1
    print(solution.generateTheString(n4)) # Expected output: "a"

    # Test case 5
    n5 = 10
    print(solution.generateTheString(n5)) # Expected output: "aaaaaaaaab"

test_generateTheString()