from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        return sum(piles[1:-len(piles)//3:2])

def test_max_coins():
    solution = Solution()

    # Test case 1
    piles = [2, 4, 1, 2, 7, 8]
    print(solution.maxCoins(piles))  # Expected output: 9

    # Test case 2
    piles = [2, 4, 5]
    print(solution.maxCoins(piles))  # Expected output: 4

    # Test case 3
    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    print(solution.maxCoins(piles))  # Expected output: 18

    # Test case 4
    piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(solution.maxCoins(piles))  # Expected output: 21

    # Test case 5
    piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(solution.maxCoins(piles))  # Expected output: 21

test_max_coins()