class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)

        operations = 0
        carry = 0
        for i in range(N - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1

        return operations + carry

def test_num_steps():
    solution = Solution()

    # Test case 1
    s1 = "1101"
    print(solution.numSteps(s1))  # Expected output: 6

    # Test case 2
    s2 = "10"
    print(solution.numSteps(s2))  # Expected output: 1

    # Test case 3
    s3 = "1"
    print(solution.numSteps(s3))  # Expected output: 0

    # Test case 4
    s4 = "111"
    print(solution.numSteps(s4))  # Expected output: 5

    # Test case 5
    s5 = "1010"
    print(solution.numSteps(s5))  # Expected output: 5

test_num_steps()