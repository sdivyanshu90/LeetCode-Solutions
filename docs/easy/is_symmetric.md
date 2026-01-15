# Symmetric Tree

## Problem Summary

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**LeetCode Problem**: [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

**LeetCode Problem**: [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isMirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (left.val == right.val) and
               isMirror(left.left, right.right) and
               isMirror(left.right, right.left)

    if root is None:
        return True

    return isMirror(root.left, root.right)
```

### How It Works

**Symmetric Tree**:

```
        1
       / \
      2   2
     / \ / \
    3  4 4  3

Check: isMirror(left=2, right=2)
  - Values match: 2 == 2 ✓
  - Outer: isMirror(left.left=3, right.right=3) ✓
  - Inner: isMirror(left.right=4, right.left=4) ✓
Result: True
```

**Non-Symmetric Tree**:

```
        1
       / \
      2   2
       \   \
        3   3

Check: isMirror(left=2, right=2)
  - Values match: 2 == 2 ✓
  - Outer: isMirror(left.left=None, right.right=3) ✗
  - One is None, other isn't
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
