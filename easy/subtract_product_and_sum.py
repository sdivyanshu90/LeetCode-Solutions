class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sums = 0
        for i in str(n):
            mul *= int(i)
            sums += int(i)
        return (mul - sums)

def test_subtract_product_and_sum():
    solution = Solution()

    # Test case 1
    n = 234
    print(solution.subtractProductAndSum(n))  # Expected output: 15

    # Test case 2
    n = 4421
    print(solution.subtractProductAndSum(n))  # Expected output: 21

    # Test case 3
    n = 0
    print(solution.subtractProductAndSum(n))  # Expected output: 0

    # Test case 4
    n = 999
    print(solution.subtractProductAndSum(n))  # Expected output: 720

    # Test case 5
    n = 12345
    print(solution.subtractProductAndSum(n))  # Expected output: 101

test_subtract_product_and_sum()