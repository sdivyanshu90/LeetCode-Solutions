# Path Sum

## Problem Summary

- Given the root of a binary tree and an integer `targetSum`, determine if there exists a root-to-leaf path such that the sum of node values along the path equals `targetSum`.
- A leaf is a node with no children.
- Return `True` if such a path exists, otherwise `False`.

Approach (recursive DFS)

- Base case 1: If the tree is empty (`root is None`), return `False` (no path exists).
- Base case 2: If the current node is a leaf (no left and right children):
  - Check if `targetSum == root.val` (the remaining sum equals the leaf value).
  - Return `True` if they match, `False` otherwise.
- Recursive case: For internal nodes, recursively check both left and right subtrees:
  - Subtract the current node's value from `targetSum`.
  - Return `True` if either the left subtree OR the right subtree has a valid path with the remaining sum.

Why this works (thought process)

- A root-to-leaf path is a sequence from the root to any leaf node.
- By subtracting the current node's value from the target sum and passing the remainder to child nodes, we track the "remaining sum needed" at each level.
- When we reach a leaf, the remaining sum should equal the leaf's value for a valid path.
- Using OR (`or`) ensures we return `True` if any path (left or right) satisfies the condition.

Time and space complexity

- Time: O(n) where n = number of nodes. In the worst case, we visit every node once (e.g., when no valid path exists and we must explore the entire tree).
- Space: O(h) where h = height of the tree, due to recursion stack.
  - Best case (balanced tree): O(log n).
  - Worst case (skewed tree): O(n).

Edge cases and robustness

- Empty tree (`root is None`) → return `False`.
- Single node tree → check if node value equals `targetSum`.
- Tree with only left or right subtrees (skewed) → works correctly with recursive calls.
- Negative node values → handled correctly (sum can increase or decrease).
- Target sum of 0 → handled if path sums to 0.
- Multiple valid paths → returns `True` if at least one valid path exists (doesn't enumerate all paths).

Example testcases (from repository)

- Tree [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 → `True` (path: 5→4→11→2)
- Tree [1,2], targetSum = 1 → `False` (no leaf with remaining sum 1; leaf at 2 has sum 1+2=3)
- Empty tree, targetSum = 0 → `False`
- Single node [7], targetSum = 7 → `True`
- Single node [7], targetSum = 10 → `False`

Step-by-step example

- Tree: 5 → (4, 8), 4 → (11, null), 11 → (7, 2). targetSum = 22.
- hasPathSum(5, 22):
  - Not a leaf, recurse:
  - hasPathSum(4, 17): // 22 - 5 = 17
    - Not a leaf, recurse:
    - hasPathSum(11, 13): // 17 - 4 = 13
      - Not a leaf, recurse:
      - hasPathSum(7, 2): // 13 - 11 = 2
        - Leaf node, 2 != 7 → False
      - hasPathSum(2, 2): // 13 - 11 = 2
        - Leaf node, 2 == 2 → **True**
      - Return True (left is False OR right is True)
    - Return True
  - Return True (left subtree found a valid path)
- Return True

Key insights

- The problem is a classic DFS tree traversal with path tracking.
- Subtracting the current value and passing the remainder is more elegant than maintaining a running sum.
- The base case for leaves is critical: only check the sum condition at leaf nodes, not internal nodes.
- Short-circuit evaluation with `or` ensures we stop searching once a valid path is found (though Python doesn't optimize recursion to stop early).

Alternative approaches

**Approach 1: Iterative DFS with stack**

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    stack = [(root, targetSum - root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
    return False
```

- Time: O(n), Space: O(h) for the stack.
- Avoids recursion; useful for very deep trees where stack overflow is a concern.

**Approach 2: BFS with queue**

```python
from collections import deque
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    queue = deque([(root, targetSum - root.val)])
    while queue:
        node, curr_sum = queue.popleft()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.left:
            queue.append((node.left, curr_sum - node.left.val))
        if node.right:
            queue.append((node.right, curr_sum - node.right.val))
    return False
```

- Time: O(n), Space: O(w) where w = maximum width of the tree.

Thought process / design choices

- Recursive DFS is the most natural and concise solution for tree path problems.
- The base case check `if not root.left and not root.right` identifies leaf nodes.
- Returning the OR of left and right subtree results elegantly expresses "exists a valid path in either subtree."
- The current implementation is clean and idiomatic for this problem.

Common pitfalls

- Checking `targetSum == root.val` for all nodes, not just leaves → incorrect for internal nodes.
- Forgetting the empty tree base case → causes AttributeError when accessing `root.val` on None.
- Using AND instead of OR → would require both subtrees to have valid paths (incorrect logic).
- Not subtracting the current node's value before recursing → incorrect sum tracking.
- Checking only `if not root.left` or `if not root.right` separately → misses single-child nodes.

Follow-up problems

- Path Sum II: Return all root-to-leaf paths that sum to targetSum.
- Path Sum III: Count paths (not necessarily root-to-leaf) that sum to targetSum.
- Binary Tree Maximum Path Sum: Find the maximum sum of any path in the tree.

Notes

- This is a fundamental tree traversal problem testing recursion and DFS.
- The solution is optimal in both time (O(n)) and space (O(h) for recursion).
- Understanding this problem is essential for more complex tree path problems.

## Approach: DFS (Implemented)

### Strategy

The solution uses dfs to solve the problem efficiently.

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    stack = [(root, targetSum - root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
    return False
```

### How It Works

Problem summary

- Given the root of a binary tree and an integer `targetSum`, determine if there exists a root-to-leaf path such that the sum of node values along the path equals `targetSum`.
- A leaf is a node with no children.
- Return `True` if such a path exists, otherwise `False`.

Approach (recursive DFS)

- Base case 1: If the tree is empty (`root is None`), return `False` (no path exists).
- Base case 2: If the current node is a leaf (no left and right children):
  - Check if `targetSum == root.val` (the remaining sum equals the leaf value).
  - Return `True` if they match, `False` otherwise.
- Recursive case: For internal nodes, recursively check both left and right subtrees:
  - Subtract the current node's value from `targetSum`.
  - Return `True` if either the left subtree OR the right subtree has a valid path with the remaining sum.

Why this works (thought process)

- A root-to-leaf path is a sequence from the root to any leaf node.
- By subtracting the current node's value from the target sum and passing the remainder to child nodes, we track the "remaining sum needed" at each level.
- When we reach a leaf, the remaining sum should equal the leaf's value for a valid path.
- Using OR (`or`) ensures we return `True` if any path (left or right) satisfies the condition.

Time and space complexity

- Time: O(n) where n = number of nodes. In the worst case, we visit every node once (e.g., when no valid path exists and we must explore the entire tree).
- Space: O(h) where h = height of the tree, due to recursion stack.
  - Best case (balanced tree): O(log n).
  - Worst case (skewed tree): O(n).

Edge cases and robustness

- Empty tree (`root is None`) → return `False`.
- Single node tree → check if node value equals `targetSum`.
- Tree with only left or right subtrees (skewed) → works correctly with recursive calls.
- Negative node values → handled correctly (sum can increase or decrease).
- Target sum of 0 → handled if path sums to 0.
- Multiple valid paths → returns `True` if at least one valid path exists (doesn't enumerate all paths).

Example testcases (from repository)

- Tree [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 → `True` (path: 5→4→11→2)
- Tree [1,2], targetSum = 1 → `False` (no leaf with remaining sum 1; leaf at 2 has sum 1+2=3)
- Empty tree, targetSum = 0 → `False`
- Single node [7], targetSum = 7 → `True`
- Single node [7], targetSum = 10 → `False`

Step-by-step example

- Tree: 5 → (4, 8), 4 → (11, null), 11 → (7, 2). targetSum = 22.
- hasPathSum(5, 22):
  - Not a leaf, recurse:
  - hasPathSum(4, 17): // 22 - 5 = 17
    - Not a leaf, recurse:
    - hasPathSum(11, 13): // 17 - 4 = 13
      - Not a leaf, recurse:
      - hasPathSum(7, 2): // 13 - 11 = 2
        - Leaf node, 2 != 7 → False
      - hasPathSum(2, 2): // 13 - 11 = 2
        - Leaf node, 2 == 2 → **True**
      - Return True (left is False OR right is True)
    - Return True
  - Return True (left subtree found a valid path)
- Return True

Key insights

- The problem is a classic DFS tree traversal with path tracking.
- Subtracting the current value and passing the remainder is more elegant than maintaining a running sum.
- The base case for leaves is critical: only check the sum condition at leaf nodes, not internal nodes.
- Short-circuit evaluation with `or` ensures we stop searching once a valid path is found (though Python doesn't optimize recursion to stop early).

Alternative approaches

**Approach 1: Iterative DFS with stack**

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    stack = [(root, targetSum - root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
    return False
```

- Time: O(n), Space: O(h) for the stack.
- Avoids recursion; useful for very deep trees where stack overflow is a concern.

**Approach 2: BFS with queue**

```python
from collections import deque
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    queue = deque([(root, targetSum - root.val)])
    while queue:
        node, curr_sum = queue.popleft()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.left:
            queue.append((node.left, curr_sum - node.left.val))
        if node.right:
            queue.append((node.right, curr_sum - node.right.val))
    return False
```

- Time: O(n), Space: O(w) where w = maximum width of the tree.

Thought process / design choices

- Recursive DFS is the most natural and concise solution for tree path problems.
- The base case check `if not root.left and not root.right` identifies leaf nodes.
- Returning the OR of left and right subtree results elegantly expresses "exists a valid path in either subtree."
- The current implementation is clean and idiomatic for this problem.

Common pitfalls

- Checking `targetSum == root.val` for all nodes, not just leaves → incorrect for internal nodes.
- Forgetting the empty tree base case → causes AttributeError when accessing `root.val` on None.
- Using AND instead of OR → would require both subtrees to have valid paths (incorrect logic).
- Not subtracting the current node's value before recursing → incorrect sum tracking.
- Checking only `if not root.left` or `if not root.right` separately → misses single-child nodes.

Follow-up problems

- Path Sum II: Return all root-to-leaf paths that sum to targetSum.
- Path Sum III: Count paths (not necessarily root-to-leaf) that sum to targetSum.
- Binary Tree Maximum Path Sum: Find the maximum sum of any path in the tree.

Notes

- This is a fundamental tree traversal problem testing recursion and DFS.
- The solution is optimal in both time (O(n)) and space (O(h) for recursion).
- Understanding this problem is essential for more complex tree path problems.

### Why DFS Works

- A root-to-leaf path is a sequence from the root to any leaf node.
- By subtracting the current node's value from the target sum and passing the remainder to child nodes, we track the "remaining sum needed" at each level.
- When we reach a leaf, the remaining sum should equal the leaf's value for a valid path.
- Using OR (`or`) ensures we return `True` if any path (left or right) satisfies the condition.

Time and space complexity

- Time: O(n) where n = number of nodes. In the worst case, we visit every node once (e.g., when no valid path exists and we must explore the entire tree).
- Space: O(h) where h = height of the tree, due to recursion stack.
  - Best case (balanced tree): O(log n).
  - Worst case (skewed tree): O(n).

Edge cases and robustness

- Empty tree (`root is None`) → return `False`.
- Single node tree → check if node value equals `targetSum`.
- Tree with only left or right subtrees (skewed) → works correctly with recursive calls.
- Negative node values → handled correctly (sum can increase or decrease).
- Target sum of 0 → handled if path sums to 0.
- Multiple valid paths → returns `True` if at least one valid path exists (doesn't enumerate all paths).

Example testcases (from repository)

- Tree [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 → `True` (path: 5→4→11→2)
- Tree [1,2], targetSum = 1 → `False` (no leaf with remaining sum 1; leaf at 2 has sum 1+2=3)
- Empty tree, targetSum = 0 → `False`
- Single node [7], targetSum = 7 → `True`
- Single node [7], targetSum = 10 → `False`

Step-by-step example

- Tree: 5 → (4, 8), 4 → (11, null), 11 → (7, 2). targetSum = 22.
- hasPathSum(5, 22):
  - Not a leaf, recurse:
  - hasPathSum(4, 17): // 22 - 5 = 17
    - Not a leaf, recurse:
    - hasPathSum(11, 13): // 17 - 4 = 13
      - Not a leaf, recurse:
      - hasPathSum(7, 2): // 13 - 11 = 2
        - Leaf node, 2 != 7 → False
      - hasPathSum(2, 2): // 13 - 11 = 2
        - Leaf node, 2 == 2 → **True**
      - Return True (left is False OR right is True)
    - Return True
  - Return True (left subtree found a valid path)
- Return True

Key insights

- The problem is a classic DFS tree traversal with path tracking.
- Subtracting the current value and passing the remainder is more elegant than maintaining a running sum.
- The base case for leaves is critical: only check the sum condition at leaf nodes, not internal nodes.
- Short-circuit evaluation with `or` ensures we stop searching once a valid path is found (though Python doesn't optimize recursion to stop early).

Alternative approaches

**Approach 1: Iterative DFS with stack**

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    stack = [(root, targetSum - root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
    return False
```

- Time: O(n), Space: O(h) for the stack.
- Avoids recursion; useful for very deep trees where stack overflow is a concern.

**Approach 2: BFS with queue**

```python
from collections import deque
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    queue = deque([(root, targetSum - root.val)])
    while queue:
        node, curr_sum = queue.popleft()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.left:
            queue.append((node.left, curr_sum - node.left.val))
        if node.right:
            queue.append((node.right, curr_sum - node.right.val))
    return False
```

- Time: O(n), Space: O(w) where w = maximum width of the tree.

Thought process / design choices

- Recursive DFS is the most natural and concise solution for tree path problems.
- The base case check `if not root.left and not root.right` identifies leaf nodes.
- Returning the OR of left and right subtree results elegantly expresses "exists a valid path in either subtree."
- The current implementation is clean and idiomatic for this problem.

Common pitfalls

- Checking `targetSum == root.val` for all nodes, not just leaves → incorrect for internal nodes.
- Forgetting the empty tree base case → causes AttributeError when accessing `root.val` on None.
- Using AND instead of OR → would require both subtrees to have valid paths (incorrect logic).
- Not subtracting the current node's value before recursing → incorrect sum tracking.
- Checking only `if not root.left` or `if not root.right` separately → misses single-child nodes.

Follow-up problems

- Path Sum II: Return all root-to-leaf paths that sum to targetSum.
- Path Sum III: Count paths (not necessarily root-to-leaf) that sum to targetSum.
- Binary Tree Maximum Path Sum: Find the maximum sum of any path in the tree.

Notes

- This is a fundamental tree traversal problem testing recursion and DFS.
- The solution is optimal in both time (O(n)) and space (O(h) for recursion).
- Understanding this problem is essential for more complex tree path problems.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n) where n = number of nodes. In the worst case, we visit every node once (e.g., when no valid path exists and we must explore the entire tree). - Space: O(h) where h = height of the tree, due to recursion stack.   - Best case (balanced tree): O(log n).   - Worst case (skewed tree): O(n). Edge cases and robustness - Empty tree (`root is None`) → return `False`. - Single node tree → check if node value equals `targetSum`. - Tree with only left or right subtrees (skewed) → works correctly with recursive calls. - Negative node values → handled correctly (sum can increase or decrease). - Target sum of 0 → handled if path sums to 0. - Multiple valid paths → returns `True` if at least one valid path exists (doesn't enumerate all paths). Example testcases (from repository) - Tree [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 → `True` (path: 5→4→11→2) - Tree [1,2], targetSum = 1 → `False` (no leaf with remaining sum 1; leaf at 2 has sum 1+2=3) - Empty tree, targetSum = 0 → `False` - Single node [7], targetSum = 7 → `True` - Single node [7], targetSum = 10 → `False` Step-by-step example - Tree: 5 → (4, 8), 4 → (11, null), 11 → (7, 2). targetSum = 22. - hasPathSum(5, 22):   - Not a leaf, recurse:   - hasPathSum(4, 17): // 22 - 5 = 17     - Not a leaf, recurse:     - hasPathSum(11, 13): // 17 - 4 = 13       - Not a leaf, recurse:       - hasPathSum(7, 2): // 13 - 11 = 2         - Leaf node, 2 != 7 → False       - hasPathSum(2, 2): // 13 - 11 = 2         - Leaf node, 2 == 2 → **True**       - Return True (left is False OR right is True)     - Return True   - Return True (left subtree found a valid path) - Return True Key insights - The problem is a classic DFS tree traversal with path tracking. - Subtracting the current value and passing the remainder is more elegant than maintaining a running sum. - The base case for leaves is critical: only check the sum condition at leaf nodes, not internal nodes. - Short-circuit evaluation with `or` ensures we stop searching once a valid path is found (though Python doesn't optimize recursion to stop early). Alternative approaches **Approach 1: Iterative DFS with stack** ```python def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:     if not root:         return False     stack = [(root, targetSum - root.val)]     while stack:         node, curr_sum = stack.pop()         if not node.left and not node.right and curr_sum == 0:             return True         if node.right:             stack.append((node.right, curr_sum - node.right.val))         if node.left:             stack.append((node.left, curr_sum - node.left.val))     return False ``` - Time: O(n), Space: O(h) for the stack. - Avoids recursion; useful for very deep trees where stack overflow is a concern. **Approach 2: BFS with queue** ```python from collections import deque def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:     if not root:         return False     queue = deque([(root, targetSum - root.val)])     while queue:         node, curr_sum = queue.popleft()         if not node.left and not node.right and curr_sum == 0:             return True         if node.left:             queue.append((node.left, curr_sum - node.left.val))         if node.right:             queue.append((node.right, curr_sum - node.right.val))     return False ``` - Time: O(n), Space: O(w) where w = maximum width of the tree. Thought process / design choices - Recursive DFS is the most natural and concise solution for tree path problems. - The base case check `if not root.left and not root.right` identifies leaf nodes. - Returning the OR of left and right subtree results elegantly expresses "exists a valid path in either subtree." - The current implementation is clean and idiomatic for this problem. Common pitfalls - Checking `targetSum == root.val` for all nodes, not just leaves → incorrect for internal nodes. - Forgetting the empty tree base case → causes AttributeError when accessing `root.val` on None. - Using AND instead of OR → would require both subtrees to have valid paths (incorrect logic). - Not subtracting the current node's value before recursing → incorrect sum tracking. - Checking only `if not root.left` or `if not root.right` separately → misses single-child nodes. Follow-up problems - Path Sum II: Return all root-to-leaf paths that sum to targetSum. - Path Sum III: Count paths (not necessarily root-to-leaf) that sum to targetSum. - Binary Tree Maximum Path Sum: Find the maximum sum of any path in the tree. Notes - This is a fundamental tree traversal problem testing recursion and DFS. - The solution is optimal in both time (O(n)) and space (O(h) for recursion). - Understanding this problem is essential for more complex tree path problems.

### Advantages

- Efficient dfs solution
- Clear and maintainable code

### Disadvantages

- May require additional space
