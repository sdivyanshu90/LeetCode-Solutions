class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = int(num ** 0.5)
        return ans * ans == num

def test_is_perfect_square():
    solution = Solution()
    
    # Test case 1: Perfect square
    print(solution.isPerfectSquare(16)) # Expected output: True
    
    # Test case 2: Not a perfect square
    print(solution.isPerfectSquare(14)) # Expected output: False

    # Test case 3: Edge case - smallest perfect square
    print(solution.isPerfectSquare(1)) # Expected output: True

    # Test case 4: Large perfect square
    print(solution.isPerfectSquare(1000000)) # Expected output: True
    
    # Test case 5: Large non-perfect square
    print(solution.isPerfectSquare(999999)) # Expected output: False

    # Test case 6: Zero case
    print(solution.isPerfectSquare(0)) # Expected output: True

    # Test case 7: Large number that is not a perfect square
    print(solution.isPerfectSquare(123456789)) # Expected output: False

    # Test case 8: Large perfect square
    print(solution.isPerfectSquare(12345678987654321)) # Expected output: True

    # Test case 9: Small non-perfect square
    print(solution.isPerfectSquare(4)) # Expected output: True

    # Test case 10: Another perfect square
    print(solution.isPerfectSquare(16)) # Expected output: True

test_is_perfect_square()