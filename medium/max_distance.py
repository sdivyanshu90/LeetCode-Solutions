from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return max_distance

def test_max_distance():
    s = Solution()

    # Test case 1
    arrays = [[1,2,3],[4,5],[1,2,3]]
    print(s.maxDistance(arrays))  # Expected output: 4

    # Test case 2
    arrays = [[1],[1]]
    print(s.maxDistance(arrays))  # Expected output: 0

    # Test case 3
    arrays = [[-10,-5,0],[5,10],[15,20]]
    print(s.maxDistance(arrays))  # Expected output: 30

    # Test case 4
    arrays = [[0,1],[2,3],[4,5],[6,7]]
    print(s.maxDistance(arrays))  # Expected output: 7

    # Test case 5
    arrays = [[-1,0,1],[2,3,4],[5,6,7]]
    print(s.maxDistance(arrays))  # Expected output: 8

test_max_distance()