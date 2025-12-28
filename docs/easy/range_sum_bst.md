# Range Sum of BST

## Problem Summary

Given the root of a Binary Search Tree (BST) and two integers `low` and `high`, return the sum of all node values that fall within the range `[low, high]` inclusive.

## Current Implementation

The solution uses a recursive DFS approach that exploits BST properties to prune unnecessary branches:

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

## How It Works

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

## Why This Works

BST property ensures:

- All nodes in left subtree are smaller than current node
- All nodes in right subtree are larger than current node
- This allows pruning entire subtrees based on current node value

## Time Complexity

O(n) in worst case where all nodes are in range. However, with pruning, average case is O(h + k) where h is tree height and k is number of nodes in range.

## Space Complexity

O(h) for recursion stack where h is tree height. In worst case (skewed tree), h = n.

## Trade-offs

- **Smart pruning**: Uses BST property to avoid visiting nodes outside range
- **Instance variable**: Uses `self.ans` to accumulate sum (could alternatively pass sum through recursion)
- **Optimal for BST**: The pruning makes this more efficient than simply visiting all nodes
- **Alternative approach**: Could use iterative DFS with stack if recursion depth is a concern
