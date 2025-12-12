from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1
        queue = deque()
        visited = set()
        
        for i in range(n):
            queue.append((i, 1 << i, 0))
            visited.add((i, 1 << i))
        
        while queue:
            node, state_mask, distance = queue.popleft()
            
            if state_mask == target_mask:
                return distance
            
            for neighbor in graph[node]:
                next_state_mask = state_mask | (1 << neighbor)
                if (neighbor, next_state_mask) not in visited:
                    queue.append((neighbor, next_state_mask, distance + 1))
                    visited.add((neighbor, next_state_mask))
        
        return -1

def test_shortestPathLength():
    solution = Solution()
    
    # Test Case 1
    print(solution.shortestPathLength([[1,2,3],[0],[0],[0]])) # Expected: 4

    # Test Case 2
    print(solution.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])) # Expected: 4

    # Test Case 3
    print(solution.shortestPathLength([[1],[0]])) # Expected: 1

    # Test Case 4
    print(solution.shortestPathLength([[1,2,3,4],[0],[0],[0],[0]])) # Expected: 6

    # Test Case 5
    print(solution.shortestPathLength([[1,2],[0,3],[0,3],[1,2]])) # Expected: 3

test_shortestPathLength()