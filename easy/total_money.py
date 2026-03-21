class Solution:
    def totalMoney(self, n: int) -> int:
        w, r = divmod(n, 7)
        return (28 * w + 7 * (w * (w - 1)) // 2) + (r * (w + 1) + (r * (r - 1)) // 2)

def test_total_money():
    s = Solution()

    # Test Case 1
    n1 = 4
    print(s.totalMoney(n1)) # Expected Output: 10

    # Test Case 2
    n2 = 10
    print(s.totalMoney(n2)) # Expected Output: 37

    # Test Case 3
    n3 = 20
    print(s.totalMoney(n3)) # Expected Output: 96

    # Test Case 4
    n4 = 25
    print(s.totalMoney(n4)) # Expected Output: 138

    # Test Case 5
    n5 = 30
    print(s.totalMoney(n5)) # Expected Output: 210

test_total_money()