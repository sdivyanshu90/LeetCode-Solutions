# N-ary Tree Postorder Traversal

## Problem Summary

- Given root of N-ary tree, return postorder traversal of node values.
- Postorder: visit all children left to right, then visit node itself.
- Example: tree with root 1 having children [3,2,4], 3 having children [5,6] -> [5,6,3,2,4,1].

Current implementation (in repository)

- Implementation uses recursive DFS:
  - Base case: returns if node is None.
  - Recursively traverses all children first.
  - Appends current node value after all children processed.
  - Returns result list.
- Example code:
  ```python
  def _traverse_postorder(self, current_node, postorder_list):
      if not current_node:
          return
      for child_node in current_node.children:
          self._traverse_postorder(child_node, postorder_list)
      postorder_list.append(current_node.val)
  ```

Why this works

- Postorder definition: children before parent.
- Iterating through children list and recursing maintains left-to-right order.
- Appending node value after recursive calls ensures parent comes last.
- None check in children prevents errors on empty child slots.

Time complexity

- Let n = number of nodes.
- Each node visited exactly once: O(n).
- Each node's value appended once: O(1) per node.
- Overall time complexity: O(n).

Space complexity

- Result list: O(n) for storing all values.
- Recursion stack: O(h) where h is height.
- Worst case: O(n) for skewed tree.
- Overall space complexity: O(n).

Thought process and trade-offs

- Recursive approach: natural fit for tree traversal.
- Separate helper function: maintains clean interface while enabling recursion.
- Alternative: iterative with stack - more complex but no recursion overhead.
- Current approach: clear and standard postorder implementation.
- N-ary generalization: loops through children list instead of fixed left/right.

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
  def _traverse_postorder(self, current_node, postorder_list):
      if not current_node:
          return
      for child_node in current_node.children:
          self._traverse_postorder(child_node, postorder_list)
      postorder_list.append(current_node.val)
  ```

### How It Works

- Separate helper function: maintains clean interface while enabling recursion.
- Alternative: iterative with stack - more complex but no recursion overhead.
- Current approach: clear and standard postorder implementation.
- N-ary generalization: loops through children list instead of fixed left/right.

### Why DFS Works

- Postorder definition: children before parent.
- Iterating through children list and recursing maintains left-to-right order.
- Appending node value after recursive calls ensures parent comes last.
- None check in children prevents errors on empty child slots.

Time complexity

- Let n = number of nodes.
- Each node visited exactly once: O(n).
- Each node's value appended once: O(1) per node.
- Overall time complexity: O(n).

Space complexity

- Result list: O(n) for storing all values.
- Recursion stack: O(h) where h is height.
- Worst case: O(n) for skewed tree.
- Overall space complexity: O(n).

Thought process and trade-offs

- Recursive approach: natural fit for tree traversal.
- Separate helper function: maintains clean interface while enabling recursion.
- Alternative: iterative with stack - more complex but no recursion overhead.
- Current approach: clear and standard postorder implementation.
- N-ary generalization: loops through children list instead of fixed left/right.

### Complexity Analysis

- **Time Complexity**: - Let n = number of nodes. - Each node visited exactly once: O(n). - Each node's value appended once: O(1) per node. - Overall time complexity: O(n). Space complexity - Result list: O(n) for storing all values. - Recursion stack: O(h) where h is height. - Worst case: O(n) for skewed tree. - Overall space complexity: O(n). Thought process and trade-offs - Recursive approach: natural fit for tree traversal. - Separate helper function: maintains clean interface while enabling recursion. - Alternative: iterative with stack - more complex but no recursion overhead. - Current approach: clear and standard postorder implementation. - N-ary generalization: loops through children list instead of fixed left/right.
- **Space Complexity**: - Result list: O(n) for storing all values. - Recursion stack: O(h) where h is height. - Worst case: O(n) for skewed tree. - Overall space complexity: O(n). Thought process and trade-offs - Recursive approach: natural fit for tree traversal. - Separate helper function: maintains clean interface while enabling recursion. - Alternative: iterative with stack - more complex but no recursion overhead. - Current approach: clear and standard postorder implementation. - N-ary generalization: loops through children list instead of fixed left/right.

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
