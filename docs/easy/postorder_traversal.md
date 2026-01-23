# Binary Tree Postorder Traversal

## Problem Summary

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

In postorder traversal, we visit nodes in this order: **Left → Right → Root**

**LeetCode Problem**: [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

**Follow-up**: Recursive solution is trivial, could you do it iteratively?

**LeetCode Problem**: [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    def dfs(node):
        if not node:
            return

        dfs(node.left)   # Visit left
        dfs(node.right)  # Visit right
        res.append(node.val)  # Process root

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

Postorder: Left → Right → Root

Execution:
  dfs(1):
    dfs(left=None): return
    dfs(right=2):
      dfs(left=3):
        dfs(left=None): return
        dfs(right=None): return
        append 3 → [3]
      dfs(right=None): return
      append 2 → [3, 2]
    append 1 → [3, 2, 1]

Result: [3, 2, 1] ✓
```

**Example 2**:

```
Tree:      1
          / \
         2   3

Postorder: Left → Right → Root

Execution:
  dfs(1):
    dfs(left=2):
      dfs(left=None): return
      dfs(right=None): return
      append 2 → [2]
    dfs(right=3):
      dfs(left=None): return
      dfs(right=None): return
      append 3 → [2, 3]
    append 1 → [2, 3, 1]

Result: [2, 3, 1] ✓
```

### Why DFS Works

The dfs approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: ### Disadvantages - **Complex logic**: Harder to understand - **More code**: Longer implementation

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
