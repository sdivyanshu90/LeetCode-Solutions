from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections = [0] * n
        adj_matrix = [[0] * n for _ in range(n)]
        
        for road in roads:
            u, v = road
            connections[u] += 1
            connections[v] += 1
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
        
        maximal_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = connections[i] + connections[j]
                if adj_matrix[i][j]:
                    rank -= 1
                maximal_rank = max(maximal_rank, rank)
        
        return maximal_rank

def test_maximal_network_rank():
    solution = Solution()

    # Test case 1
    n = 4
    roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
    print(solution.maximalNetworkRank(n, roads))  # Expected output: 4

    # Test case 2
    n = 5
    roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
    print(solution.maximalNetworkRank(n, roads))  # Expected output: 5

    # Test case 3
    n = 8
    roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(solution.maximalNetworkRank(n, roads))  # Expected output: 4

    # Test case 4
    n = 2
    roads = [[0, 1]]
    print(solution.maximalNetworkRank(n, roads))  # Expected output: 1

    # Test case 5
    n = 3
    roads = [[0, 1], [0, 2], [1, 2]]
    print(solution.maximalNetworkRank(n, roads))  # Expected output: 3

test_maximal_network_rank()