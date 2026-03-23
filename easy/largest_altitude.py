from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0, gain[0]]
        for i in range(1, len(gain)):
            res.append(gain[i - 1] + gain[i] + res[i - 1])
        return max(res)

def test_largest_altitude():
    solution = Solution()

    # Test case 1
    gain = [-5, 1, 5, 0, -7]
    print(solution.largestAltitude(gain))  # Expected output: 1

    # Test case 2
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(solution.largestAltitude(gain))  # Expected output: 0

    # Test case 3
    gain = [0, -1, -2, -3]
    print(solution.largestAltitude(gain))  # Expected output: 0

    # Test case 4
    gain = [1, 2, 3, 4]
    print(solution.largestAltitude(gain))  # Expected output: 10

    # Test case 5
    gain = [-1, -2, -3, -4]
    print(solution.largestAltitude(gain))  # Expected output: 0

test_largest_altitude()