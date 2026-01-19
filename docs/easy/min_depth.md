# Minimum Depth of Binary Tree

## Problem Summary

Given a binary tree, find its **minimum depth**.

The minimum depth is the number of nodes along the **shortest path from the root node down to the nearest leaf node**.

**Note**: A leaf is a node with no children.

**LeetCode Problem**: [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

**LeetCode Problem**: [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return self.minDepth(root.right) + 1
    if root.right is None:
        return self.minDepth(root.left) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

### How It Works

**Example 1** (Balanced tree):

```
Tree:        3
            / \
           9  20
             / \
            15  7

minDepth(3):
  - 3 has both children
  - Left path: minDepth(9)
    - 9 is a leaf → return 1
  - Right path: minDepth(20)
    - 20 has both children
    - Left: minDepth(15) → leaf → 1
    - Right: minDepth(7) → leaf → 1
    - return min(1, 1) + 1 = 2
  - return min(1, 2) + 1 = 2

Minimum depth: 2 (path 3→9)
```

**Example 2** (Skewed tree):

```
Tree:    1
         |
         2
         |
         3

minDepth(1):
  - 1 has only left child (no right)
  - return minDepth(left) + 1
    - minDepth(2):
      - 2 has only left child
      - return minDepth(left) + 1
        - minDepth(3):
          - 3 is a leaf
          - return 1
        - return 1 + 1 = 2
      - return 2 + 1 = 3
    - return 3

Minimum depth: 3 (must go to actual leaf)
```

### Why DFS Works

The dfs approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: Considerations**: - **Balanced tree**: Both DFS and BFS are O(n) in typical case - **Highly unbalanced tree**: BFS is O(h), DFS is O(n)   - Skewed tree with 1 million nodes:     - DFS visits all 1 million nodes     - BFS finds leaf in O(h) = 1 million steps but stops there     - Actually, for single-chain tree, both are O(n)     - BFS shines when there's a short path but deep tree **When to use which**: - **DFS Recursive**: Simple, clean code for interview - **BFS Iterative**: Production code, handles large/unbalanced trees **Space optimization**: - Both O(h) and O(w) are logarithmic for balanced trees - For unbalanced trees, BFS could use more space if tree is wide
- **Space Complexity**: O(1)

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
