from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        size = 0
        x1 = -1
        x2 = -2
        for start, end in intervals:
            if x1 >= start:
                continue
            elif x2 >= start:
                x1 = x2
                x2 = end
                size += 1
            else:                
                x1 = end - 1
                x2 = end
                size += 2
                
        return size

def test_intersection_size_two():
    solution = Solution()
    
    # Test case 1
    intervals1 = [[1,3],[1,4],[2,5],[3,5]]
    print(solution.intersectionSizeTwo(intervals1)) # Expected: 3
    
    # Test case 2
    intervals2 = [[1,2],[2,3],[2,4],[4,5]]
    print(solution.intersectionSizeTwo(intervals2)) # Expected: 5
    
    # Test case 3
    intervals3 = [[0,1],[1,2],[2,3],[3,4],[4,5]]
    print(solution.intersectionSizeTwo(intervals3)) # Expected: 10
    
    # Test case 4
    intervals4 = [[1,10],[2,9],[3,8],[4,7]]
    print(solution.intersectionSizeTwo(intervals4)) # Expected: 2

    # Test case 5
    intervals5 = [[5,7],[1,3],[2,4],[6,8]]
    print(solution.intersectionSizeTwo(intervals5)) # Expected: 4

    # Test case 6
    intervals6 = [[1,5],[2,6],[3,7],[4,8]]
    print(solution.intersectionSizeTwo(intervals6)) # Expected: 4

    # Test case 7
    intervals7 = [[1,2],[2,3],[3,4],[4,5],[5,6]]
    print(solution.intersectionSizeTwo(intervals7)) # Expected: 10

    # Test case 8
    intervals8 = [[0,2],[2,4],[4,6],[6,8]]
    print(solution.intersectionSizeTwo(intervals8)) # Expected: 8

    # Test case 9
    intervals9 = [[1,1000]]
    print(solution.intersectionSizeTwo(intervals9)) # Expected: 2

    # Test case 10
    intervals10 = [[1,3],[4,6],[7,9]]
    print(solution.intersectionSizeTwo(intervals10)) # Expected: 6

test_intersection_size_two()