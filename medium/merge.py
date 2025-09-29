from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res

def test_merge():
    s = Solution()
    
    # Test case 1: Regular case with overlapping intervals
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

    # Test case 2: No overlapping intervals
    print(s.merge([[1,2],[3,4],[5,6]]))

    # Test case 3: All intervals overlap into one
    print(s.merge([[1,4],[2,3],[3,5]]))

    # Test case 4: Single interval
    print(s.merge([[1,5]]))

    # Test case 5: Empty list of intervals
    print(s.merge([]))

    # Test case 6: Intervals with same start time
    print(s.merge([[1,4],[1,5],[1,3]]))

    # Test case 7: Intervals with same end time
    print(s.merge([[1,4],[2,4],[3,4]]))

    # Test case 8: Intervals that touch at the edges
    print(s.merge([[1,2],[2,3],[3,4]]))

    # Test case 9: Large number of intervals
    print(s.merge([[i, i+1] for i in range(0, 100, 2)] + [[i+0.5, i+1.5] for i in range(0, 100, 2)]))

    # Test case 10: Nested intervals
    print(s.merge([[1,10],[2,5],[6,9]]))

test_merge()