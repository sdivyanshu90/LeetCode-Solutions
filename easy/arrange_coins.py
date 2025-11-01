class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (right + left) // 2
            sums = mid * (mid + 1) // 2
            if sums == n:
                return mid
            if n < sums:
                right = mid - 1
            else:
                left = mid + 1
        return right

def test_arrange_coins():
    s = Solution()

    # Test case 1
    n = 5
    print(s.arrangeCoins(n))  # Expected output: 2

    # Test case 2
    n = 8
    print(s.arrangeCoins(n))  # Expected output: 3

    # Test case 3
    n = 0
    print(s.arrangeCoins(n))  # Expected output: 0

    # Test case 4
    n = 1
    print(s.arrangeCoins(n))  # Expected output: 1

    # Test case 5
    n = 10
    print(s.arrangeCoins(n))  # Expected output: 4

test_arrange_coins()