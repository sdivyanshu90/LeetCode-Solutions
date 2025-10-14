from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses

def test_can_finish():
    s = Solution()

    # Test Case 1: Simple case, possible to finish
    numCourses = 2
    prerequisites = [[1, 0]] # To take course 1, you need to finish course 0 (0 -> 1)
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 2: Simple case, impossible to finish (direct cycle)
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]] # (0 -> 1) and (1 -> 0)
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: False

    # Test Case 3: No prerequisites
    numCourses = 5
    prerequisites = []
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 4: Complex case, possible to finish (DAG)
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]] # (0->1, 0->2, 1->3, 2->3)
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 5: Complex case, impossible to finish (long cycle)
    numCourses = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]] # (1 -> 0 -> 2 -> 1) is wrong, it is (1->0, 2->1, 0->2) which is a cycle
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: False

    # Test Case 6: Disconnected components (some courses independent)
    numCourses = 5
    prerequisites = [[1, 0], [3, 2]] # Two separate dependency chains
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 7: Single course
    numCourses = 1
    prerequisites = []
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 8: A long linear chain of dependencies
    numCourses = 4
    prerequisites = [[3, 2], [2, 1], [1, 0]] # (0 -> 1 -> 2 -> 3)
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 9: Multiple prerequisites for one course
    numCourses = 3
    prerequisites = [[0, 1], [0, 2]] # (1 -> 0) and (2 -> 0)
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: True

    # Test Case 10: Cycle not involving all nodes
    numCourses = 4
    prerequisites = [[0, 1], [1, 2], [2, 0], [3, 0]] # (1->0, 2->1, 0->2) forms a cycle, 3 is separate.
    print(f"\nInput: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {s.canFinish(numCourses, prerequisites)}") # Expected: False

test_can_finish()