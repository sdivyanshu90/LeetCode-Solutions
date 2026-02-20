from typing import List
import collections

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)
        can_open = [status[i] == 1 for i in range(n)]
        has_box, used = [False] * n, [False] * n

        q = collections.deque()
        ans = 0
        for box in initialBoxes:
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                used[box] = True
                ans += candies[box]

        while len(q) > 0:
            big_box = q.popleft()
            for key in keys[big_box]:
                can_open[key] = True
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    ans += candies[key]
            for box in containedBoxes[big_box]:
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans += candies[box]

        return ans

def test_max_candies():
    solution = Solution()

    # Test case 1
    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[1],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [0]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Expected output: 16

    # Test case 2
    status = [1,0,0,0]
    candies = [100,1,100,1]
    keys = [[1,2,3],[],[],[]]
    containedBoxes = [[],[],[],[]]
    initialBoxes = [0]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Expected output: 100

    # Test case 3
    status = [1,1,1]
    candies = [10,20,30]
    keys = [[],[],[]]
    containedBoxes = [[1],[2],[]]
    initialBoxes = [0]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Expected output: 60

    # Test case 4
    status = [0,0,0]
    candies = [10,20,30]
    keys = [[],[],[]]
    containedBoxes = [[1],[2],[]]
    initialBoxes = [0]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Expected output: 0

    # Test case 5
    status = [1,0,0,1]
    candies = [10,20,30,40]
    keys = [[],[0,2],[],[]]
    containedBoxes = [[1],[2],[],[]]
    initialBoxes = [0,3]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Expected output: 100

test_max_candies()