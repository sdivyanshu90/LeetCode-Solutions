from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        result = []
        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False

            for neigh in graph[node]:
                if not dfs(neigh):
                    return safe[node]
            safe[node] = True

            return safe[node]
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return result

def test_eventual_safe_nodes():
    solution = Solution()

    # Test Case 1
    graph1 = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(solution.eventualSafeNodes(graph1)) # Expected: [2,4,5,6]

    # Test Case 2
    graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    print(solution.eventualSafeNodes(graph2)) # Expected: [4]

    # Test Case 3
    graph3 = [[],[0,2,3,4],[3],[4],[]]
    print(solution.eventualSafeNodes(graph3)) # Expected: [0,1,2,3,4]

    # Test Case 4
    graph4 = [[1],[2],[3],[4],[]]
    print(solution.eventualSafeNodes(graph4)) # Expected: [0,1,2,3,4]

    # Test Case 5
    graph5 = [[1,2],[2,3],[3,1],[]]
    print(solution.eventualSafeNodes(graph5)) # Expected: [3]

test_eventual_safe_nodes()