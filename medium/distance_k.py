from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        self.buildGraph(root, None, graph)

        queue = deque([(target, 0)])
        visited = set([target])
        result = []
        
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                result.append(node.val)
            elif distance < k:
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
                        visited.add(neighbor)
        
        return result
    
    def buildGraph(self, node, parent, graph):
        if node:
            if parent:
                graph.setdefault(node, []).append(parent)
                graph.setdefault(parent, []).append(node)
            self.buildGraph(node.left, node, graph)
            self.buildGraph(node.right, node, graph)

def test_distanceK():
    solution = Solution()
    
    # Test Case 1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    target = root.left  # Node with value 5
    print(solution.distanceK(root, target, 2)) # Expected: [7,4,1]
    
    # Test Case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    target = root  # Node with value 1
    print(solution.distanceK(root, target, 1)) # Expected: [2]
    
    # Test Case 3
    root = TreeNode(0)
    target = root  # Node with value 0
    print(solution.distanceK(root, target, 0)) # Expected: [0]
    
    # Test Case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    target = root.left  # Node with value 2
    print(solution.distanceK(root, target, 1)) # Expected: [1]
    
    # Test Case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    target = root.left.left  # Node with value 3
    print(solution.distanceK(root, target, 3)) # Expected: []

test_distanceK()