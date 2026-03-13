from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        n = len(points)
        edges = []
        
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        
        edges.sort()
        
        parent = list(range(n))
        min_cost = 0
        num_edges = 0
        
        for cost, u, v in edges:
            if find(parent, u) != find(parent, v):
                union(parent, u, v)
                min_cost += cost
                num_edges += 1
                if num_edges == n - 1:
                    break
        
        return min_cost

def test_min_cost_connect_points():
    solution = Solution()

    # Test case 1
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(solution.minCostConnectPoints(points))  # Expected output: 20

    # Test case 2
    points = [[3, 12], [-2, 5], [-4, 1]]
    print(solution.minCostConnectPoints(points))  # Expected output: 18

    # Test case 3
    points = [[0, 0]]
    print(solution.minCostConnectPoints(points))  # Expected output: 0

    # Test case 4
    points = [[1, 1], [3, 4], [6, 1]]
    print(solution.minCostConnectPoints(points))  # Expected output: 10

    # Test case 5
    points = [[-1, -1], [-2, -2], [-3, -3]]
    print(solution.minCostConnectPoints(points))  # Expected output: 4

test_min_cost_connect_points()