from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        nei_map = {}
        leaves = deque()

        layer_map = defaultdict(set)
        max_layer = 0
        for node in graph:
            num_neighbors = len(graph[node])
            if num_neighbors == 1:
                leaves.append((0, node))
                layer_map[0].add(node)
            nei_map[node] = num_neighbors

        while leaves:
            layer, node = leaves.popleft()
            max_layer = max(layer, max_layer)
            layer_map[layer].add(node)

            for nei in graph[node]:
                nei_map[nei] -= 1

                if nei_map[nei] == 1:
                    leaves.append((layer + 1, nei))

        return list(layer_map[max_layer])

def test_find_min_height_trees():
    s = Solution()

    # Test Case 1: Typical case with a balanced tree
    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [0]

    # Test Case 2: Only one node, no edges
    n = 1
    edges = []
    print(s.findMinHeightTrees(n, edges))  # Expected: [0]

    # Test Case 3: A tree where the center is the root of the tree
    n = 7
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [0]

    # Test Case 4: A star-shaped graph
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [0]

    # Test Case 5: A line graph
    n = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [1, 2]

    # Test Case 6: A disconnected graph (not connected)
    n = 4
    edges = [[0, 1], [1, 2]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [1] (Disconnected components don't form a tree)

    # Test Case 7: Tree with only two nodes
    n = 2
    edges = [[0, 1]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [0, 1]

    # Test Case 8: Larger tree with more layers
    n = 10
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [4, 5]

    # Test Case 9: A single node connected to multiple other nodes
    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    print(s.findMinHeightTrees(n, edges))  # Expected: [0]

test_find_min_height_trees()