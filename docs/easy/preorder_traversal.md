# Binary Tree Preorder Traversal

## Problem Summary

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

In preorder traversal, we visit nodes in this order: **Root → Left → Right**

**LeetCode Problem**: [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

**Follow-up**: Recursive solution is trivial, could you do it iteratively?

**LeetCode Problem**: [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    res = []
    def dfs(node):
        if not node:
            return

        res.append(node.val)  # Process root
        dfs(node.left)         # Visit left
        dfs(node.right)        # Visit right

    dfs(root)
    return res
```

### How It Works

**Example 1**:

```
Tree:    1
          \
           2
          /
         3

Preorder: Root → Left → Right

Execution:
  dfs(1):
    append 1 → [1]
    dfs(left=None): return
    dfs(right=2):
      append 2 → [1, 2]
      dfs(left=3):
        append 3 → [1, 2, 3]
        dfs(left=None): return
        dfs(right=None): return
      dfs(right=None): return

Result: [1, 2, 3] ✓
```

**Example 2**:

```
Tree:      1
          / \
         2   3

Preorder: Root → Left → Right

Execution:
  dfs(1):
    append 1 → [1]
    dfs(left=2):
      append 2 → [1, 2]
      dfs(left=None): return
      dfs(right=None): return
    dfs(right=3):
      append 3 → [1, 2, 3]
      dfs(left=None): return
      dfs(right=None): return

Result: [1, 2, 3] ✓
```

### Why DFS Works

The dfs approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: as recursive - Satisfies follow-up requirement **Why preorder is useful**: - **Tree copying**: Need to create parent before children - **Tree serialization**: Store structure naturally - **DFS search**: Process node as soon as you see it - **Prefix expression**: Operator comes before operands **Comparison with other traversals**: - **Preorder**: Root first, good for copying/serialization - **Inorder**: For BST, gives sorted order - **Postorder**: Children first, good for deletion This is a fundamental tree traversal pattern with straightforward implementation!

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
