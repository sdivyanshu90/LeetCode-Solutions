# Same Tree

## Problem Summary

Given the roots of two binary trees `p` and `q`, determine if they are the same tree. Two binary trees are considered the same if they are structurally identical and the nodes have the same values.

**LeetCode Problem**: [100. Same Tree](https://leetcode.com/problems/same-tree/)

**LeetCode Problem**: [Same Tree](https://leetcode.com/problems/same-tree/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if (p is None and q) or (p and q is None):
        return False

    if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
        return True

    return False
```

### How It Works

The algorithm performs a **simultaneous traversal** of both trees:

```
Tree p:      1              Tree q:      1
           /   \                        /   \
          2     3                      2     3

Step 1: Compare roots (1 == 1) ✓
Step 2: Compare left subtrees (2 == 2) ✓
Step 3: Compare right subtrees (3 == 3) ✓
Result: True
```

For different trees:

```
Tree p:      1              Tree q:      1
           /                              \
          2                                2

Step 1: Compare roots (1 == 1) ✓
Step 2: Compare left subtrees (2 vs None) ✗
Result: False
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
