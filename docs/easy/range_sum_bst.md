# Range Sum of BST

## Problem Summary

Given the root of a Binary Search Tree (BST) and two integers `low` and `high`, return the sum of all node values that fall within the range `[low, high]` inclusive.

## Approach: Binary Search (Implemented)

### Strategy

The solution uses binary search to solve the problem efficiently.

```python
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def search(node):
        if not node:
            return
        if low <= node.val <= high:
            self.ans += node.val
            search(node.left)
            search(node.right)
        elif node.val < low:
            search(node.right)
        elif node.val > high:
            search(node.left)
    self.ans = 0
    search(root)
    return self.ans
```

### How It Works

The algorithm leverages BST properties (left subtree < node < right subtree) to optimize the search:

1. **Node in range** (`low <= node.val <= high`): Add value to sum, explore both subtrees
2. **Node too small** (`node.val < low`): Only explore right subtree (left will be even smaller)
3. **Node too large** (`node.val > high`): Only explore left subtree (right will be even larger)

**Example**: BST `[10,5,15,3,7,null,18]`, low=7, high=15

- Start at 10: in range, add 10, explore both sides
- Left child 5: too small, only explore right
  - Right child 7: in range, add 7
- Right child 15: in range, add 15, explore both sides
- Sum: 10 + 7 + 15 = 32

### Why Binary Search Works

BST property ensures:

- All nodes in left subtree are smaller than current node
- All nodes in right subtree are larger than current node
- This allows pruning entire subtrees based on current node value

### Complexity Analysis

- **Time Complexity**: O(n) in worst case where all nodes are in range. However, with pruning, average case is O(h + k) where h is tree height and k is number of nodes in range.
- **Space Complexity**: O(h) for recursion stack where h is tree height. In worst case (skewed tree), h = n.

### Advantages

- Efficient binary search solution
- Clear and maintainable code

### Disadvantages

- May require additional space
