from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i + 1] * arr[i + 2]
            if product % 2 != 0:
                return True
        return False

def test_three_consecutive_odds():
    solution = Solution()

    # Test case 1
    arr1 = [2, 6, 4, 1]
    print(solution.threeConsecutiveOdds(arr1))  # Expected output: False

    # Test case 2
    arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(solution.threeConsecutiveOdds(arr2))  # Expected output: True

    # Test case 3
    arr3 = [1, 1, 1]
    print(solution.threeConsecutiveOdds(arr3))  # Expected output: True

    # Test case 4
    arr4 = [2, 4, 6]
    print(solution.threeConsecutiveOdds(arr4))  # Expected output: False

    # Test case 5
    arr5 = [1, 3, 5]
    print(solution.threeConsecutiveOdds(arr5))  # Expected output: True

test_three_consecutive_odds()