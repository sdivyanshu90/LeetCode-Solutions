# Minimum Distance Between BST Nodes

Problem summary

- Given root of Binary Search Tree, find minimum difference between values of any two nodes.
- BST property: left < root < right for all subtrees.
- Example: BST [4,2,6,1,3] -> minimum difference is 1 (between 2 and 3, or 3 and 4).

Current implementation (in repository)

- Implementation uses inorder traversal:
  - Performs inorder traversal of BST (gives sorted sequence).
  - Tracks previous node value during traversal.
  - Calculates difference with previous value for each node.
  - Updates minimum difference found.
  - Returns minimum difference after complete traversal.
- Example code:
  ```python
  def inorder(node):
      if not node:
          return
      inorder(node.left)
      if self.prev is not None:
          self.min_diff = min(self.min_diff, node.val - self.prev)
      self.prev = node.val
      inorder(node.right)
  ```

Why this works

- Inorder traversal of BST visits nodes in sorted (ascending) order.
- Adjacent elements in sorted sequence have minimum possible differences.
- Tracking previous value allows computing difference with current node.
- Only need to check adjacent pairs (no need to check all pairs).
- BST property guarantees no smaller difference exists elsewhere.

Time complexity

- Let n = number of nodes.
- Inorder traversal visits each node once: O(n).
- Overall time complexity: O(n).

Space complexity

- Recursion stack: O(h) where h is height.
- Worst case (skewed tree): O(n).
- Best case (balanced): O(log n).
- Overall space complexity: O(n) worst case.

Thought process and trade-offs

- Inorder traversal: leverages BST property elegantly.
- Alternative: collect all values in array, sort, find min difference - O(n log n) time (unnecessary since BST already ordered).
- Current approach: optimal O(n) time using BST property.
- Instance variables (self.prev, self.min_diff): simple state tracking across recursive calls.
