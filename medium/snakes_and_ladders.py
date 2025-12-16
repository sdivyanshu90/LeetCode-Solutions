from collections import deque
from itertools import chain
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        for i in range(1, len(board), 2):
            board[i].reverse()
        arr = [None] + list(chain(*board))
        
        n, queue, seen, ct = len(arr) - 1, deque([1]), {1}, 0

        while queue:
            lenQ = len(queue)

            for _ in range(lenQ):
                cur = queue.popleft()
                if cur == n:
                    return ct

                for i in range(cur + 1, min(cur + 7, n + 1)):
                    nxt = arr[i] if arr[i] != -1 else i
                    if nxt in seen:
                        continue
                    seen.add(nxt)
                    queue.append(nxt)
                    
            ct += 1

        return -1

def test_snakes_and_ladders():
    solution = Solution()

    # Test Case 1
    print(solution.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                                     [-1,-1,-1,-1,-1,-1],
                                     [-1,-1,-1,-1,-1,-1],
                                     [-1,35,-1,-1,13,-1],
                                     [-1,-1,-1,-1,-1,-1],
                                     [-1,15,-1,-1,-1,-1]])) # Expected: 4

    # Test Case 2
    print(solution.snakesAndLadders([[-1,-1],
                                     [-1,3]])) # Expected: 1

    # Test Case 3
    print(solution.snakesAndLadders([[-1,4,-1],
                                     [3,5,-1],
                                     [-1,2,-1]])) # Expected: 2

    # Test Case 4
    print(solution.snakesAndLadders([[-1,-1,-1],
                                     [-1,9,8],
                                     [-1,8,9]])) # Expected: 3

    # Test Case 5
    print(solution.snakesAndLadders([[-1]])) # Expected: 0
    
test_snakes_and_ladders()