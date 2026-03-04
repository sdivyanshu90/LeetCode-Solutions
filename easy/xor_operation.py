class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0]*n
        for i in range(n):
            nums[i] = start + 2 * i

        result = 0
        for num in nums:
            result ^= num
        return result

def test_xor_operation():
    solution = Solution()

    # Test Case 1
    n1 = 5
    start1 = 0
    print(solution.xorOperation(n1, start1))  # Expected output: 8

    # Test Case 2
    n2 = 6
    start2 = 5
    print(solution.xorOperation(n2, start2))  # Expected output: 2

    # Test Case 3
    n3 = 1
    start3 = 7
    print(solution.xorOperation(n3, start3))  # Expected output: 7

    # Test Case 4
    n4 = 10
    start4 = 3
    print(solution.xorOperation(n4, start4))  # Expected output: 8

    # Test Case 5
    n5 = 0
    start5 = 0
    print(solution.xorOperation(n5, start5))  # Expected output: 0

test_xor_operation()