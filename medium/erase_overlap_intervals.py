from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        
        return count

def test_erase_overlap_intervals():
    s = Solution()

    # Test case 1
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Expected output: 1

    # Test case 2
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        # Expected output: 2

    # Test case 3
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))              # Expected output: 0

    # Test case 4
    print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])) # Expected output: 2

    # Test case 5
    print(s.eraseOverlapIntervals([]))                         # Expected output: 0

    # Test case 6
    print(s.eraseOverlapIntervals([[0,1]]))                    # Expected output: 0

    # Test case 7
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[4,5]])) # Expected output: 0

    # Test case 8
    print(s.eraseOverlapIntervals([[1,5],[2,3],[3,4]]))       # Expected output: 1

    # Test case 9
    print(s.eraseOverlapIntervals([[1,10],[2,3],[3,4],[4,5]]))# Expected output: 1

    # Test case 10
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,2]])) # Expected output: 1

test_erase_overlap_intervals()