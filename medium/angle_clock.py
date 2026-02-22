class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        res = 0
        if hour == 12:
            res = (abs((minutes*6) - (minutes * 0.5)))
        else:
            res = (abs(((11/2)*minutes) - (30*hour)))

        return min(res, 360-res)

def test_angleClock():
    solution = Solution()

    # Test case 1
    hour = 12
    minutes = 30
    expected = 165.0
    print(solution.angleClock(hour, minutes))  # Expected Output: 165.0

    # Test case 2
    hour = 3
    minutes = 30
    expected = 75.0
    print(solution.angleClock(hour, minutes))  # Expected Output: 75.0

    # Test case 3
    hour = 3
    minutes = 15
    expected = 7.5
    print(solution.angleClock(hour, minutes))  # Expected Output: 7.5

    # Test case 4
    hour = 4
    minutes = 50
    expected = 155.0
    print(solution.angleClock(hour, minutes))  # Expected Output: 155.0

    # Test case 5
    hour = 12
    minutes = 0
    expected = 0.0
    print(solution.angleClock(hour, minutes))  # Expected Output: 0.0

test_angleClock()