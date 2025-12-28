# Leaf-Similar Trees

Problem summary

- Two binary trees are leaf-similar if their leaf value sequences are the same.
- Leaf sequence: values of leaves read from left to right.
- Return true if trees are leaf-similar.
- Example: different structure but same leaf sequence [6,7,4,9,8] -> True.

Current implementation (in repository)

- Implementation uses generator for DFS traversal:
  - Defines nested generator function that yields leaf values.
  - Uses DFS to traverse tree.
  - Yields node value only if it's a leaf (no children).
  - Compares leaf sequences of both trees as lists.
- Example code:
  ```python
  def dfs(node):
      if node:
          if not node.left and not node.right:
              yield node.val
          yield from dfs(node.left)
          yield from dfs(node.right)
  return list(dfs(root1)) == list(dfs(root2))
  ```

Why this works

- Generator with yield creates iterator over leaf values.
- DFS traversal visits nodes in consistent order (left-to-right for leaves).
- Leaf detection: node exists but has no children.
- `yield from` delegates to recursive calls, maintaining traversal order.
- List comparison checks if leaf sequences match exactly.

Time complexity

- Let n = nodes in root1, m = nodes in root2.
- DFS traverses all nodes: O(n) + O(m).
- List comparison: O(min(leaves1, leaves2)).
- Overall time complexity: O(n + m).

Space complexity

- List of leaves: O(k1) + O(k2) where k1, k2 are leaf counts.
- Recursion stack: O(h1) + O(h2) where h is height.
- Overall space complexity: O(n + m) worst case.

Thought process and trade-offs

- Generator approach: Pythonic and memory-efficient for large trees (lazy evaluation).
- Alternative: collect leaves in lists during traversal, then compare - same complexity but eager evaluation.
- Alternative: interleave traversals, compare on-the-fly - early termination possible but more complex.
- Current approach: clean and leverages Python's generator features.
