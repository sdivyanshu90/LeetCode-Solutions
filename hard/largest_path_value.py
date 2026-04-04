from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        color_count = [[0] * 26 for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque(i for i in range(n) if indegree[i] == 0)
        processed = 0
        max_value = 0

        while queue:
            node = queue.popleft()
            processed += 1

            color_index = ord(colors[node]) - ord('a')
            color_count[node][color_index] += 1
            max_value = max(max_value, color_count[node][color_index])

            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(color_count[neighbor][c], color_count[node][c])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max_value if processed == n else -1

def test_largest_path_value():
    solution = Solution()

    # Test case 1
    colors1 = "abaca"
    edges1 = [[0,1],[0,2],[2,3],[3,4]]
    print(solution.largestPathValue(colors1, edges1))  # Expected output: 3

    # Test case 2
    colors2 = "a"
    edges2 = [[0,0]]
    print(solution.largestPathValue(colors2, edges2))  # Expected output: -1

    # Test case 3
    colors3 = "abc"
    edges3 = [[0,1],[1,2],[2,0]]
    print(solution.largestPathValue(colors3, edges3))  # Expected output: -1

    # Test case 4
    colors4 = "aaab"
    edges4 = [[0,1],[0,2],[1,3]]
    print(solution.largestPathValue(colors4, edges4))  # Expected output: 2

    # Test case 5
    colors5 = "abcde"
    edges5 = [[0,1],[0,2],[1,3],[2,4]]
    print(solution.largestPathValue(colors5, edges5))  # Expected output: 1

test_largest_path_value()