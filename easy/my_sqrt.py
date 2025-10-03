class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid <= x // mid:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

def test_my_sqrt():
    solution = Solution()
    # Test Case 1
    print(solution.mySqrt(4))  # Expected output: 2
    # Test Case 2
    print(solution.mySqrt(8))  # Expected output: 2
    # Test Case 3
    print(solution.mySqrt(0))  # Expected output: 0
    # Test Case 4
    print(solution.mySqrt(1))  # Expected output: 1
    # Test Case 5
    print(solution.mySqrt(16))  # Expected output: 4
    # Test Case 6
    print(solution.mySqrt(25))  # Expected output: 5
    # Test Case 7
    print(solution.mySqrt(26))  # Expected output: 5
    # Test Case 8
    print(solution.mySqrt(100))  # Expected output: 10
    # Test Case 9
    print(solution.mySqrt(2147395599))  # Expected output: 46339
    # Test Case 10
    print(solution.mySqrt(2147483647))  # Expected output: 46340

test_my_sqrt()