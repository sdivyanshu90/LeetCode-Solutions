# Binary Tree Inorder Traversal — Explanation, Approach, Complexity

**Problem Summary**

- Given the root of a binary tree, return the inorder traversal of its nodes' values.
- Inorder traversal order: left subtree → node → right subtree.

**Approach Used (Recursive DFS)**

- Define a helper `dfs(node)` that:
  - Returns immediately on `None`.
  - Recurses into `node.left`, appends `node.val`, then recurses into `node.right`.
- Collect values into a list and return it.
- This mirrors the inorder definition and is clear and concise.

**Why It Works**

- Inorder traversal is naturally expressed recursively: process left subtree first, then the node, then right subtree.
- The recursion visits each node exactly once and appends values in correct order by construction.

**Complexity**

- Time: O(n) — visits each of the n nodes once.
- Space:
  - O(n) worst-case recursion stack for a skewed tree; O(h) with h = tree height.
  - O(n) for the output list of values.

**Edge Cases**

- Empty tree → return []
- Single node → return [value]
- Skewed tree (all-left or all-right) → recursion depth equals number of nodes
- Duplicate values → kept as-is; traversal order still well-defined

**Alternative Approaches**

- Iterative with stack (avoids recursion):
  - Use a stack and a pointer `curr`.
  - While `curr` or stack not empty: push left spine, then pop, record value, go right.
  - Time O(n), Space O(n) in worst case for stack.
- Morris traversal (O(1) auxiliary space):
  - Create temporary threads to predecessor nodes to traverse without stack/recursion.
  - Time O(n), Space O(1) aux; more complex and modifies pointers during traversal.

**Thought Process / Design Choices**

- Recursive DFS is the simplest and most readable for inorder traversal.
- For very deep trees where recursion depth could be a concern, prefer the iterative stack-based approach.
- Morris traversal is an optimization when recursion/stack space is constrained and pointer manipulation is acceptable.
