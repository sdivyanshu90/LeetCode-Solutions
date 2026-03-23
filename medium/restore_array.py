from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dict = defaultdict(list)
        for x,y in adjacentPairs:
            dict[x].append(y)
            dict[y].append(x)
        
        start = 0
        for x in dict.keys():
            if len(dict[x]) == 1:
                start = x
                break
        
        seen = set()
        ans = []
        while start != None:
            ans.append(start)
            seen.add(start)
            adj = dict[start]

            for x in adj:
                if x not in seen:
                    start = x
                    break
                start = None
        return ans

def test_restore_array():
    solution = Solution()

    # Test case 1
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    print(solution.restoreArray(adjacentPairs))  # Expected output: [1, 2, 3, 4]

    # Test case 2
    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    print(solution.restoreArray(adjacentPairs))  # Expected output: [-2, 4, 1, -3]

    # Test case 3
    adjacentPairs = [[100000, -100000]]
    print(solution.restoreArray(adjacentPairs))  # Expected output: [100000, -100000]

    # Test case 4
    adjacentPairs = [[-1, -2], [-2, -3], [-3, -4], [-4, -5]]
    print(solution.restoreArray(adjacentPairs))  # Expected output: [-1, -2, -3, -4, -5]

    # Test case 5
    adjacentPairs = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(solution.restoreArray(adjacentPairs))  # Expected output: [0, 1, 2, 3, 4]

test_restore_array()