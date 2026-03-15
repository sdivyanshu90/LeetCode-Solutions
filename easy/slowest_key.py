from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        alpha = [(keysPressed[0], releaseTimes[0])]

        for i in range(1, len(keysPressed)):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            alpha.append((keysPressed[i], diff))

        maxi = max(diff for _, diff in alpha)
        return max([key for key, diff in alpha if diff == maxi])

def test_slowest_key():
    solution = Solution()

    # Test case 1
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"
    print(solution.slowestKey(releaseTimes, keysPressed))  # Expected output: "c"

    # Test case 2
    releaseTimes = [12, 23, 36, 46, 62]
    keysPressed = "spuda"
    print(solution.slowestKey(releaseTimes, keysPressed))  # Expected output: "a"

    # Test case 3
    releaseTimes = [1, 2]
    keysPressed = "aa"
    print(solution.slowestKey(releaseTimes, keysPressed))  # Expected output: "a"

    # Test case 4
    releaseTimes = [1]
    keysPressed = "z"
    print(solution.slowestKey(releaseTimes, keysPressed))  # Expected output: "z"

    # Test case 5
    releaseTimes = [1, 2, 3]
    keysPressed = "abc"
    print(solution.slowestKey(releaseTimes, keysPressed))  # Expected output: "c"

test_slowest_key()