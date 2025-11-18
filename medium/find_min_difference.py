from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        minutes.sort()
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])

def test_find_min_difference():
    s = Solution()

    # Test case 1
    timePoints1 = ["23:59", "00:00"]
    print(s.findMinDifference(timePoints1)) # Expected output: 1

    # Test case 2
    timePoints2 = ["00:00", "23:59", "00:00"]
    print(s.findMinDifference(timePoints2)) # Expected output: 0

    # Test case 3
    timePoints3 = ["01:01", "02:01", "03:00"]
    print(s.findMinDifference(timePoints3)) # Expected output: 59

    # Test case 4
    timePoints4 = ["12:30", "12:00", "13:00"]
    print(s.findMinDifference(timePoints4)) # Expected output: 30

    # Test case 5
    timePoints5 = ["05:31", "22:08", "00:35"]
    print(s.findMinDifference(timePoints5)) # Expected output: 147

test_find_min_difference()