from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in edges: 
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        size = [0]*n
        
        def fn(x, par): 
            """Return size and sum of distances in sub-tree."""
            c = s = 0
            for xx in graph.get(x, []): 
                if xx != par: 
                    cc, ss = fn(xx, x)
                    c, s = c + cc, s + ss + cc
            size[x] = c + 1
            return c + 1, s
        
        ans = [0]*n
        ans[0] = fn(0, -1)[1]
        
        stack = [0]
        while stack: 
            x = stack.pop()
            for xx in graph.get(x, []): 
                if not ans[xx]: 
                    ans[xx] = ans[x] + n - 2*size[xx]
                    stack.append(xx)
        return ans

def test_sum_of_distances_in_tree():
    solution = Solution()

    # Test Case 1
    n1 = 6
    edges1 = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(solution.sumOfDistancesInTree(n1, edges1)) # Expected: [8,12,6,10,10,10]

    # Test Case 2
    n2 = 1
    edges2 = []
    print(solution.sumOfDistancesInTree(n2, edges2)) # Expected: [0]

    # Test Case 3
    n3 = 2
    edges3 = [[1,0]]
    print(solution.sumOfDistancesInTree(n3, edges3)) # Expected: [1,1]

    # Test Case 4
    n4 = 3
    edges4 = [[0,1],[0,2]]
    print(solution.sumOfDistancesInTree(n4, edges4)) # Expected: [2,3,3]

    # Test Case 5
    n5 = 4
    edges5 = [[0,1],[1,2],[1,3]]
    print(solution.sumOfDistancesInTree(n5, edges5)) # Expected: [5,3,5,5]

test_sum_of_distances_in_tree()