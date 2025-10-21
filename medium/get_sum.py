class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])

def test_get_sum():
    solution = Solution()
    
    # Test case 1
    print(solution.getSum(1, 2)) # Expected output: 3
    
    # Test case 2
    print(solution.getSum(-1, 1)) # Expected output: 0

    # Test case 3: Edge case - both zeros
    print(solution.getSum(0, 0)) # Expected output: 0

    # Test case 4: Large positive numbers
    print(solution.getSum(1000000, 2000000)) # Expected output: 3000000
    
    # Test case 5: Large negative numbers
    print(solution.getSum(-1000000, -2000000)) # Expected output: -3000000

    # Test case 6: Mixed large numbers
    print(solution.getSum(123456789, -987654321)) # Expected output: -864197532

    # Test case 7: One zero
    print(solution.getSum(0, 5)) # Expected output: 5

    # Test case 8: Both negative and positive
    print(solution.getSum(-5, 10)) # Expected output: 5

    # Test case 9: Same negative numbers
    print(solution.getSum(-3, -3)) # Expected output: -6

    # Test case 10: Same positive numbers
    print(solution.getSum(7, 7)) # Expected output: 14

test_get_sum()