from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        max_prob = [0] * n
        max_prob[start] = 1
        
        for i in range(n - 1):
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1 
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1
            if not has_update:
                break
        
        return max_prob[end]

def test_max_probability():
    solution = Solution()

    # Test case 1
    n1 = 3
    edges1 = [[0, 1], [1, 2], [0, 2]]
    succProb1 = [0.5, 0.5, 0.2]
    start1 = 0
    end1 = 2
    print(solution.maxProbability(n1, edges1, succProb1, start1, end1))  # Expected output: 0.25

    # Test case 2
    n2 = 3
    edges2 = [[0, 1], [1, 2], [0, 2]]
    succProb2 = [0.5, 0.5, 0.3]
    start2 = 0
    end2 = 2
    print(solution.maxProbability(n2, edges2, succProb2, start2, end2))  # Expected output: 0.3

    # Test case 3
    n3 = 3
    edges3 = [[0, 1]]
    succProb3 = [0.5]
    start3 = 0
    end3 = 2
    print(solution.maxProbability(n3, edges3, succProb3, start3, end3))  # Expected output: 0.0

    # Test case 4
    n4 = 5
    edges4 = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4]]
    succProb4 = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    start4 = 0
    end4 = 4
    print(solution.maxProbability(n4, edges4, succProb4, start4, end4))  # Expected output: 0.126

    # Test case 5
    n5 = 4
    edges5 = [[0, 1], [1, 2], [2, 3]]
    succProb5 = [0.9, 0.8, 0.7]
    start5 = 0
    end5 = 3
    print(solution.maxProbability(n5, edges5, succProb5, start5, end5))  # Expected output: 0.504

test_max_probability()