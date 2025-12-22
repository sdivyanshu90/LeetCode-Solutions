# Balanced Binary Tree — Explanation, Approach, Complexity

**Problem Summary**

- Given the root of a binary tree, determine if it is height-balanced.
- A binary tree is height-balanced if for every node, the height difference between its left and right subtrees is at most 1.
- Example: [3,9,20,null,null,15,7] is balanced; [1,2,2,3,3,null,null,4,4] is not.

**Approach (Optimized DFS with early termination)**

- Define a helper function `check_balance_and_height(node)` that returns:
  - The height of the subtree if balanced
  - `-1` if the subtree is unbalanced (sentinel value for early exit)
- For each node:
  - Recursively check left subtree height; if `-1`, propagate up immediately.
  - Recursively check right subtree height; if `-1`, propagate up immediately.
  - If `|left_height - right_height| > 1`, return `-1` (unbalanced).
  - Otherwise, return `max(left_height, right_height) + 1` (height of current subtree).
- Root call returns `-1` if unbalanced, or a valid height ≥ 0 if balanced.

Implementation:

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def check_balance_and_height(node):
        if not node:
            return 0

        left_height = check_balance_and_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_balance_and_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_balance_and_height(root) != -1
```

**Why It Works**

- A tree is balanced if both subtrees are balanced AND the height difference at the root is ≤ 1.
- By combining height calculation with balance checking, we traverse the tree only once.
- Using `-1` as a sentinel allows early termination when imbalance is detected (no need to continue checking other branches).

**Complexity**

- Time: O(n) — visits each node exactly once in a single DFS traversal.
- Space: O(h) for recursion stack, where h = tree height.
  - Best case (balanced tree): O(log n)
  - Worst case (skewed tree): O(n)

**Edge Cases**

- Empty tree (None) → return True (considered balanced by definition)
- Single node → return True (height 0, trivially balanced)
- All nodes on left side (skewed left) → unbalanced if depth > 1
- Perfect binary tree → balanced
- Complete binary tree → balanced

**Alternative Approaches**

**Naive approach (calculate height separately):**

```python
def isBalanced(self, root):
    def height(node):
        if not node:
            return 0
        return max(height(node.left), height(node.right)) + 1

    if not root:
        return True

    left_h = height(root.left)
    right_h = height(root.right)

    if abs(left_h - right_h) > 1:
        return False

    return self.isBalanced(root.left) and self.isBalanced(root.right)
```

- Time: O(n log n) for balanced trees, O(n²) for skewed trees — recalculates heights redundantly.
- Space: O(h)
- Less efficient; not recommended.

**Iterative with explicit stack:**

- Possible but more complex; requires tracking heights and visited nodes.
- No significant advantage over the recursive approach.

**Thought Process / Design Choices**

- The optimized approach combines two concerns (height + balance check) into one traversal.
- Early termination via sentinel value `-1` improves efficiency when tree is unbalanced.
- Single-pass DFS is optimal for this problem.
- The height of an empty node is 0 (base case).

**Example Testcases (from repository)**

- [3,9,20,null,null,15,7] → True (balanced)
- [1,2,2,3,3,null,null,4,4] → False (left subtree too deep)
- [1] → True (single node)
- None → True (empty tree)
- [1,2,3,4,5,6,7] (complete tree) → True

**Common Pitfalls**

- Recalculating heights multiple times → use the optimized approach to compute heights once.
- Forgetting to check both subtrees are balanced → must verify balance at every node, not just root.
- Not handling None as base case → causes errors when accessing node attributes.
- Using positive height for unbalanced indicator → conflicts with valid heights; `-1` is a clear sentinel.

**Key Insight**

- Balance property must hold at **every** node, not just the root.
- The definition requires: for any node, `|height(left) - height(right)| ≤ 1`.
