from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = 0
        for i in range(len(chalk)):
            sum_chalk += chalk[i]
            if sum_chalk > k:
                break

        k = k % sum_chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0

def test_chalk_replacer():
    solution = Solution()

    # Test case 1
    chalk = [5, 1, 5]
    k = 22
    print(solution.chalkReplacer(chalk, k))  # Expected output: 0

    # Test case 2
    chalk = [3, 4, 1, 2]
    k = 25
    print(solution.chalkReplacer(chalk, k))  # Expected output: 1

    # Test case 3
    chalk = [1, 2, 3]
    k = 10
    print(solution.chalkReplacer(chalk, k))  # Expected output: 2

    # Test case 4
    chalk = [10, 20, 30]
    k = 60
    print(solution.chalkReplacer(chalk, k))  # Expected output: 0

    # Test case 5
    chalk = [2, 3, 4]
    k = 15
    print(solution.chalkReplacer(chalk, k))  # Expected output: 2

test_chalk_replacer()