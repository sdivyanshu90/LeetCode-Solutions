from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

def test_insert():
    s = Solution()

    # Test case 1: Regular case with overlapping intervals
    print(s.insert([[1,3],[6,9]], [2,5]))

    # Test case 2: New interval does not overlap and goes at the end
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [17,19]))

    # Test case 3: New interval does not overlap and goes at the beginning
    print(s.insert([[3,5],[6,7],[8,10],[12,16]], [1,2]))

    # Test case 4: New interval overlaps with all existing intervals
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [0,20]))

    # Test case 5: New interval is completely inside an existing interval
    print(s.insert([[1,5]], [2,3]))

    # Test case 6: New interval is the same as an existing interval
    print(s.insert([[1,3],[6,9]], [1,3]))

    # Test case 7: Empty intervals list
    print(s.insert([], [4,8]))

    # Test case 8: New interval overlaps with multiple intervals
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

    # Test case 9: New interval touches the end of an existing interval
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [5,6]))

    # Test case 10: New interval touches the start of an existing interval
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [10,12]))

test_insert()