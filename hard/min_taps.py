from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_ranges = [0] * (n+1)
        for i,r in enumerate(ranges):
            left, right = max(0,i-r), min(n,i+r)
            max_ranges[left] =  max(max_ranges[left],right - left)
        start = end = count = 0
        while end < n:
            count +=1
            start , end = end, max(max_ranges[i] + i for i in range(start,end+1))  
            if start == end:
                return -1
        return count

def test_minTaps():
    solution = Solution()

    # Test case 1
    n = 5
    ranges = [3,4,1,1,0,0]
    expected = 1
    print(solution.minTaps(n, ranges))  # Expected Output: 1

    # Test case 2
    n = 3
    ranges = [0,0,0,0]
    expected = -1
    print(solution.minTaps(n, ranges))  # Expected Output: -1

    # Test case 3
    n = 7
    ranges = [1,2,1,0,2,1,0,1]
    expected = 3
    print(solution.minTaps(n, ranges))  # Expected Output: 3

    # Test case 4
    n = 8
    ranges = [4,0,0,0,4,0,0,0,4]
    expected = 1
    print(solution.minTaps(n, ranges))  # Expected Output: 1

    # Test case 5
    n = 8
    ranges = [4,0,0,0,4,0,0,0,2]
    expected = 2
    print(solution.minTaps(n, ranges))  # Expected Output: 1

test_minTaps()