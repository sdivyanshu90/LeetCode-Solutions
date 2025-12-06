from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends: return -1
        if '0000' in deadends: return -1
        queue = deque(['0000'])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return level
                for i in range(4):
                    pre = node[:i]
                    post = node[i + 1:]
                    for op in [-1, 1]:
                        nxt = pre + str((int(node[i]) + op) % 10) + post
                        if nxt not in deadends:
                            deadends.add(nxt)
                            queue.append(nxt)
            level += 1
        return -1

def test_open_lock():
    solution = Solution()
    
    # Test case 1
    deadends1 = ["0201","0101","0102","1212","2002"]
    target1 = "0202"
    print(solution.openLock(deadends1, target1)) # Expected: 6
    
    # Test case 2
    deadends2 = ["8888"]
    target2 = "0009"
    print(solution.openLock(deadends2, target2)) # Expected: 1
    
    # Test case 3
    deadends3 = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target3 = "8888"
    print(solution.openLock(deadends3, target3)) # Expected: -1
    
    # Test case 4
    deadends4 = ["0000"]
    target4 = "8888"
    print(solution.openLock(deadends4, target4)) # Expected: -1

    # Test case 5
    deadends5 = []
    target5 = "0001"
    print(solution.openLock(deadends5, target5)) # Expected: 1

    # Test case 6
    deadends6 = ["1234","5678"]
    target6 = "0000"
    print(solution.openLock(deadends6, target6)) # Expected: 0

    # Test case 7
    deadends7 = ["0001","0010","0100","1000"]
    target7 = "1111"
    print(solution.openLock(deadends7, target7)) # Expected: 6

    # Test case 8
    deadends8 = ["9999"]
    target8 = "0000"
    print(solution.openLock(deadends8, target8)) # Expected: 0

    # Test case 9
    deadends9 = ["0002","0020","0200","2000"]
    target9 = "0001"
    print(solution.openLock(deadends9, target9)) # Expected: 1

    # Test case 10
    deadends10 = ["1111","2222","3333","4444","5555","6666","7777","8888","9999"]
    target10 = "0000"
    print(solution.openLock(deadends10, target10)) # Expected: 0

test_open_lock()