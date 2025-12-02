class Solution:
    def _is_connected(self, src, target, visited, adj_list):
        visited[src] = True

        if src == target:
            return True

        is_found = False
        for adj in adj_list[src]:
            if not visited[adj]:
                is_found = is_found or self._is_connected(
                    adj, target, visited, adj_list
                )

        return is_found

    def findRedundantConnection(self, edges):
        N = len(edges)

        adj_list = [[] for _ in range(N)]

        for edge in edges:
            visited = [False] * N

            if self._is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge

            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        return []

def test_find_redundant_connection():
    solution = Solution()

    # Test Case 1
    edges1 = [[1,2],[1,3],[2,3]]
    print(solution.findRedundantConnection(edges1))  # Expected: [2,3]

    # Test Case 2
    edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(solution.findRedundantConnection(edges2))  # Expected: [1,4]

    # Test Case 3
    edges3 = [[1,2],[2,3],[3,1]]
    print(solution.findRedundantConnection(edges3))  # Expected: [3,1]

    # Test Case 4
    edges4 = [[1,4],[2,3],[3,4],[1,2]]
    print(solution.findRedundantConnection(edges4))  # Expected: [1,2]

    # Test Case 5
    edges5 = [[1,5],[2,5],[3,5],[4,5],[5,6],[6,7],[7,5]]
    print(solution.findRedundantConnection(edges5))  # Expected: [7,5]

test_find_redundant_connection()