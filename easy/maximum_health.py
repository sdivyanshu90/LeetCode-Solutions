class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for i in range(len(accounts)):
            res = max(res, sum(accounts[i]))
        return res

def test_maximum_health():
    solution = Solution()

    # Test case 1
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(solution.maximumWealth(accounts))  # Expected output: 6

    # Test case 2
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(solution.maximumWealth(accounts))  # Expected output: 10

    # Test case 3
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(solution.maximumWealth(accounts))  # Expected output: 17

    # Test case 4
    accounts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.maximumWealth(accounts))  # Expected output: 24

    # Test case 5
    accounts = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(solution.maximumWealth(accounts))  # Expected output: 3

test_maximum_health()