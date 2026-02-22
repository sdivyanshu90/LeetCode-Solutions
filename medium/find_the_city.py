class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        INF = int(1e9 + 7)
        distance_matrix = [[INF] * n for _ in range(n)]

        for i in range(n):
            distance_matrix[i][i] = 0
        for start, end, weight in edges:
            distance_matrix[start][end] = weight
            distance_matrix[end][start] = weight
        self.floyd(n, distance_matrix)
        return self.get_city_with_fewest_reachable(
            n, distance_matrix, distanceThreshold
        )

    def floyd(self, n: int, distance_matrix: List[List[int]]):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance_matrix[i][j] = min(
                        distance_matrix[i][j],
                        distance_matrix[i][k] + distance_matrix[k][j],
                    )

    def get_city_with_fewest_reachable(
        self, n: int, distance_matrix: List[List[int]], distance_threshold: int
    ) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n

        for i in range(n):
            reachable_count = sum(
                1
                for j in range(n)
                if i != j and distance_matrix[i][j] <= distance_threshold
            )
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
        return city_with_fewest_reachable

def test_findTheCity():
    solution = Solution()

    # Test case 1
    n = 4
    edges = [
        [0, 1, 3], 
        [1, 2, 1], 
        [1, 3, 4], 
        [2, 3, 1]
    ]
    distanceThreshold = 4
    expected = 3
    print(solution.findTheCity(n, edges, distanceThreshold))  # Expected Output: 3

    # Test case 2
    n = 5
    edges = [
        [0, 1, 2], 
        [0, 4, 8], 
        [1, 2, 3], 
        [1, 4, 2], 
        [2, 3, 1], 
        [3, 4, 1]
    ]
    distanceThreshold = 2
    expected = 0
    print(solution.findTheCity(n, edges, distanceThreshold))  # Expected Output: 0

    # Test case 3
    n = 6
    edges = [
        [0, 3, 7],
        [2, 3, 1],
        [2, 4, 3],
        [1, 2, 1],
        [1, 3, 3],
        [1, 4, 3],
        [1, 5, 3],
        [3, 4, 1],
        [3, 5, 1],
    ]
    distanceThreshold = 2
    expected = 5
    print(solution.findTheCity(n, edges, distanceThreshold))  # Expected Output: 5

    # Test case 4
    n = 4
    edges = [
        [0, 1, 3], 
        [1, 2, 1], 
        [1, 3, 4], 
        [2, 3, 1]
    ]
    distanceThreshold = 3
    expected = 0
    print(solution.findTheCity(n, edges, distanceThreshold))  # Expected Output: 0

    # Test case 5
    n = 5
    edges = [
        [0, 1, 2], 
        [0, 4, 8], 
        [1, 2, 3], 
        [1, 4, 2], 
        [2, 3, 1], 
        [3, 4, 1]
    ]
    distanceThreshold = 3
    expected = 0
    print(solution.findTheCity(n, edges, distanceThreshold))  # Expected Output: 0

test_findTheCity()