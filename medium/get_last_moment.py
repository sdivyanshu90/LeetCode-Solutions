from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=-1), n - min(right, default=n+1))

def test_get_last_moment():
    solution = Solution()

    # Test Case 1
    n1 = 4
    left1 = [4, 3]
    right1 = [0, 1]
    print(solution.getLastMoment(n1, left1, right1))  # Expected output: 4

    # Test Case 2
    n2 = 7
    left2 = []
    right2 = [0, 1, 2, 3, 4, 5, 6, 7]
    print(solution.getLastMoment(n2, left2, right2))  # Expected output: 7

    # Test Case 3
    n3 = 7
    left3 = [0, 1, 2, 3, 4, 5, 6, 7]
    right3 = []
    print(solution.getLastMoment(n3, left3, right3))  # Expected output: 7

    # Test Case 4
    n4 = 9
    left4 = [5]
    right4 = [4]
    print(solution.getLastMoment(n4, left4, right4))  # Expected output: 5

    # Test Case 5
    n5 = 6
    left5 = [6]
    right5 = [0]
    print(solution.getLastMoment(n5, left5, right5))  # Expected output: 6

test_get_last_moment()