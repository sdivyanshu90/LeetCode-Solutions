# Diameter of Binary Tree

Problem summary

- Given the root of a binary tree, return the length of the diameter.
- Diameter: longest path between any two nodes in the tree.
- Path may or may not pass through the root.
- Example: Tree [1,2,3,4,5] -> diameter is 3 (path 4->2->1->3 or 5->2->1->3).

Current implementation (in repository)

- Implementation uses recursive height calculation with diameter tracking:
  - Maintains instance variable `self.diameter` to track maximum diameter found.
  - Recursively calculates height of left and right subtrees.
  - For each node, calculates chord (path through that node) = 1 + left_height + 1 + right_height.
  - Updates global maximum diameter if current chord is larger.
  - Returns height of subtree (1 + max of left and right heights).
- Example code:
  ```python
  def height(node=root):
      chord = le = ri = 0
      if node.left:
          le = height(node.left)
          chord += 1 + le
      if node.right:
          ri = height(node.right)
          chord += 1 + ri
      self.diameter = max(chord, self.diameter)
      return 1 + max(le, ri)
  ```

Why this works

- Diameter through any node = edges in left subtree + edges in right subtree + 2 (edges to children).
- Height function returns edges from node to deepest leaf in its subtree.
- By checking every node as potential "center" of diameter path, finds global maximum.
- DFS traversal ensures all nodes are considered.

Time complexity

- Let n = number of nodes in the tree.
- Each node is visited once: O(n).
- At each node, constant work is done.
- Overall time complexity: O(n).

Space complexity

- Recursion stack depth = height of tree.
- Worst case (skewed tree): O(n).
- Average case (balanced tree): O(log n).
- Overall space complexity: O(n) worst case.

Thought process and trade-offs

- Combining height calculation with diameter tracking: efficient single-pass solution.
- Alternative: calculate height for every node as root, then find max - O(n²) time.
- Current approach leverages fact that height calculation naturally visits all nodes.
- Instance variable for diameter: simple but couples state to object; could use return tuple instead.
- Trade-off: clarity of separate concerns vs. single return value.
