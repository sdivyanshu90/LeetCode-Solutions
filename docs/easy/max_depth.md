# Maximum Depth of Binary Tree

## Problem Summary

Given the `root` of a binary tree, return its **maximum depth**. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**LeetCode Problem**: [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**LeetCode Problem**: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    else:
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
```

### How It Works

**Example Tree**:

```
        3
       / \
      9   20
         /  \
        15   7
```

**Recursive calls**:

```
maxDepth(3):
  left = maxDepth(9):
    left = maxDepth(None) = 0
    right = maxDepth(None) = 0
    return 1 + max(0, 0) = 1

  right = maxDepth(20):
    left = maxDepth(15):
      left = maxDepth(None) = 0
      right = maxDepth(None) = 0
      return 1 + max(0, 0) = 1

    right = maxDepth(7):
      left = maxDepth(None) = 0
      right = maxDepth(None) = 0
      return 1 + max(0, 0) = 1

    return 1 + max(1, 1) = 2

  return 1 + max(1, 2) = 3
```

### Why DFS Works

The dfs approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
