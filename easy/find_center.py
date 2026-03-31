from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edge, second_edge = edges[0], edges[1]
        return first_edge[0] if first_edge[0] in second_edge else first_edge[1]

def test_find_center():
    solution = Solution()

    # Test case 1
    edges1 = [[1,2],[2,3],[4,2]]
    print(solution.findCenter(edges1))  # Expected output: 2

    # Test case 2
    edges2 = [[1,3],[2,3],[3,4],[3,5]]
    print(solution.findCenter(edges2))  # Expected output: 3

    # Test case 3
    edges3 = [[1,100000],[100000,99999],[99999,99998]]
    print(solution.findCenter(edges3))  # Expected output: 100000

    # Test case 4
    edges4 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]]
    print(solution.findCenter(edges4))  # Expected output: 2

    # Test case 5
    edges5 = [[1,2],[1,3],[1,4],[1,5]]
    print(solution.findCenter(edges5))  # Expected output: 1

test_find_center()