# Cousins in Binary Tree

Problem summary

- Given binary tree root and two values x and y, return true if they are cousins.
- Cousins: nodes at same depth with different parents.
- Example: tree with nodes at same level but different parent nodes -> True.

Current implementation (in repository)

- Implementation uses level-order traversal (BFS):
  - Uses queue storing tuples of (node, parent, depth).
  - Tracks information for both x and y when found.
  - Processes level by level using queue.
  - Compares depth and parent when both nodes found.
  - Returns True only if same depth but different parents.
- Example code:
  ```python
  queue = deque([(root, None, 0)])
  while queue:
      node, parent, depth = queue.popleft()
      if node.val == x:
          x_info = (parent, depth)
      if node.val == y:
          y_info = (parent, depth)
  return x_info[1] == y_info[1] and x_info[0] != y_info[0]
  ```

Why this works

- BFS naturally processes nodes level by level (same depth).
- Tracking parent allows checking if nodes have different parents.
- Storing depth explicitly ensures accurate level comparison.
- Checking after finding both nodes determines cousin relationship.

Time complexity

- Let n = number of nodes.
- BFS visits each node once: O(n).
- Each node operation (enqueue, dequeue, check) is O(1).
- Overall time complexity: O(n).

Space complexity

- Queue can hold up to one level of nodes.
- Worst case (complete binary tree): O(n/2) = O(n) for last level.
- Overall space complexity: O(n).

Thought process and trade-offs

- BFS approach: natural fit for level-based problems.
- Alternative: DFS with depth tracking - similar complexity but less intuitive for level comparison.
- Stores parent and depth together: convenient tuple structure.
- Early return possible: could check and return immediately after finding both nodes instead of waiting for level completion.
- Current approach: clear and correct, minor optimization possible.
