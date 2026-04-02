from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = deque(range(1, n + 1))

        while len(circle) > 1:
            for _ in range(k - 1):
                circle.append(circle.popleft())
            circle.popleft()
        return circle[0]

def test_find_the_winner():
    solution = Solution()

    # Test Case 1
    n1, k1 = 5, 2
    print(solution.findTheWinner(n1, k1))  # Expected Output: 3

    # Test Case 2
    n2, k2 = 6, 5
    print(solution.findTheWinner(n2, k2))  # Expected Output: 1

    # Test Case 3
    n3, k3 = 10, 3
    print(solution.findTheWinner(n3, k3))  # Expected Output: 4

    # Test Case 4
    n4, k4 = 7, 7
    print(solution.findTheWinner(n4, k4))  # Expected Output: 5

    # Test Case 5
    n5, k5 = 8, 4
    print(solution.findTheWinner(n5, k5))  # Expected Output: 6

test_find_the_winner()