# Univalued Binary Tree

## Problem Summary

- Binary tree is univalued if every node has the same value.
- Return true if tree is univalued.
- Example: tree with all nodes having value 1 -> True.

Current implementation (in repository)

- Implementation uses DFS with set to collect values:
  - Traverses entire tree using DFS.
  - Adds each node's value to a set.
  - After traversal, checks if set contains exactly one unique value.
  - Returns True if len(seen) == 1.
- Example code:
  ```python
  seen = set()
  def dfs(node):
      if node:
          seen.add(node.val)
          dfs(node.left)
          dfs(node.right)
  dfs(root)
  return len(seen) == 1
  ```

Why this works

- Set automatically deduplicates values.
- If all nodes have same value, set will contain only that one value.
- If any node differs, set will contain multiple values.
- DFS traverses all nodes ensuring complete coverage.

Time complexity

- Let n = number of nodes.
- DFS visits each node once: O(n).
- Adding to set is O(1) average.
- Overall time complexity: O(n).

Space complexity

- Set stores at most k unique values where k <= n.
- Best case (univalued): O(1).
- Worst case (all different): O(n).
- Recursion stack: O(h) where h is height, O(n) worst case.
- Overall space complexity: O(n).

Thought process and trade-offs

- Set-based approach: simple and clear.
- Alternative: compare each node with root value during traversal - saves space (no set needed), O(1) extra space.
- Alternative: compare children with parent at each node - similar to above.
- Current approach: trades space for clarity.
- Could optimize: return early when set size > 1 (tree not univalued).

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
  seen = set()
  def dfs(node):
      if node:
          seen.add(node.val)
          dfs(node.left)
          dfs(node.right)
  dfs(root)
  return len(seen) == 1
  ```

### How It Works

- Alternative: compare each node with root value during traversal - saves space (no set needed), O(1) extra space.
- Alternative: compare children with parent at each node - similar to above.
- Current approach: trades space for clarity.
- Could optimize: return early when set size > 1 (tree not univalued).

### Why DFS Works

- Set automatically deduplicates values.
- If all nodes have same value, set will contain only that one value.
- If any node differs, set will contain multiple values.
- DFS traverses all nodes ensuring complete coverage.

Time complexity

- Let n = number of nodes.
- DFS visits each node once: O(n).
- Adding to set is O(1) average.
- Overall time complexity: O(n).

Space complexity

- Set stores at most k unique values where k <= n.
- Best case (univalued): O(1).
- Worst case (all different): O(n).
- Recursion stack: O(h) where h is height, O(n) worst case.
- Overall space complexity: O(n).

Thought process and trade-offs

- Set-based approach: simple and clear.
- Alternative: compare each node with root value during traversal - saves space (no set needed), O(1) extra space.
- Alternative: compare children with parent at each node - similar to above.
- Current approach: trades space for clarity.
- Could optimize: return early when set size > 1 (tree not univalued).

### Complexity Analysis

- **Time Complexity**: - Let n = number of nodes. - DFS visits each node once: O(n). - Adding to set is O(1) average. - Overall time complexity: O(n). Space complexity - Set stores at most k unique values where k <= n. - Best case (univalued): O(1). - Worst case (all different): O(n). - Recursion stack: O(h) where h is height, O(n) worst case. - Overall space complexity: O(n). Thought process and trade-offs - Set-based approach: simple and clear. - Alternative: compare each node with root value during traversal - saves space (no set needed), O(1) extra space. - Alternative: compare children with parent at each node - similar to above. - Current approach: trades space for clarity. - Could optimize: return early when set size > 1 (tree not univalued).
- **Space Complexity**: - Set stores at most k unique values where k <= n. - Best case (univalued): O(1). - Worst case (all different): O(n). - Recursion stack: O(h) where h is height, O(n) worst case. - Overall space complexity: O(n). Thought process and trade-offs - Set-based approach: simple and clear. - Alternative: compare each node with root value during traversal - saves space (no set needed), O(1) extra space. - Alternative: compare children with parent at each node - similar to above. - Current approach: trades space for clarity. - Could optimize: return early when set size > 1 (tree not univalued).

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
