class Solution:
    def removeStones(self, stones):
        uf = self.UnionFind(
            20002
        )
        
        for x, y in stones:
            uf._union_nodes(
                x, y + 10001
            )
            
        return len(stones) - uf.component_count

    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n
            self.component_count = (
                0
            )
            self.unique_nodes = (
                set()
            )

        def _find(self, node):
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)

            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        def _union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)

            if root1 == root2:
                return
            self.parent[root1] = root2
            self.component_count -= 1

def test_remove_stones():
    solution = Solution()

    # Test case 1
    stones1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(solution.removeStones(stones1))  # Expected output: 5

    # Test case 2
    stones2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    print(solution.removeStones(stones2))  # Expected output: 3

    # Test case 3
    stones3 = [[0,0]]
    print(solution.removeStones(stones3))  # Expected output: 0

    # Test case 4
    stones4 = [[0,1],[1,0],[1,1]]
    print(solution.removeStones(stones4))  # Expected output: 2

    # Test case 5
    stones5 = [[0,0],[0,1],[1,1],[1,2],[2,2],[2,3]]
    print(solution.removeStones(stones5))  # Expected output: 5

test_remove_stones()