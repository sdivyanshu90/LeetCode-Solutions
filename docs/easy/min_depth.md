# Minimum Depth of Binary Tree

## Problem Summary

Given a binary tree, find its **minimum depth**.

The minimum depth is the number of nodes along the **shortest path from the root node down to the nearest leaf node**.

**Note**: A leaf is a node with no children.

**LeetCode Problem**: [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

## Approach 1: Recursive DFS (Implemented)

### Strategy

The implemented solution uses a **recursive depth-first search** approach:

1. **Base case**: If root is `None`, return 0 (no depth)
2. **Leaf node**: If both children are `None`, return 1
3. **Single child**: If only one child exists, recurse on that child (skip nodes with only one path)
4. **Two children**: Return the minimum depth of both children + 1

**Key Insight**: Must go to a **leaf node** (node with no children). A node with one child is not a leaf - we must continue down the path.

**Code**:

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return self.minDepth(root.right) + 1
    if root.right is None:
        return self.minDepth(root.left) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

### How It Works

**Example 1** (Balanced tree):

```
Tree:        3
            / \
           9  20
             / \
            15  7

minDepth(3):
  - 3 has both children
  - Left path: minDepth(9)
    - 9 is a leaf → return 1
  - Right path: minDepth(20)
    - 20 has both children
    - Left: minDepth(15) → leaf → 1
    - Right: minDepth(7) → leaf → 1
    - return min(1, 1) + 1 = 2
  - return min(1, 2) + 1 = 2

Minimum depth: 2 (path 3→9)
```

**Example 2** (Skewed tree):

```
Tree:    1
         |
         2
         |
         3

minDepth(1):
  - 1 has only left child (no right)
  - return minDepth(left) + 1
    - minDepth(2):
      - 2 has only left child
      - return minDepth(left) + 1
        - minDepth(3):
          - 3 is a leaf
          - return 1
        - return 1 + 1 = 2
      - return 2 + 1 = 3
    - return 3

Minimum depth: 3 (must go to actual leaf)
```

### Why Handle Single Child Case?

**Common mistake**: Just taking `min(left_depth, right_depth) + 1` always

```python
# WRONG: Doesn't handle skewed trees correctly
return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

For a tree with only left child, this would return `0 + 1 = 1`, which is incorrect.

**Correct approach**: If one child is missing, we must go down the existing path:

```python
if root.left is None:
    return self.minDepth(root.right) + 1
```

### Complexity Analysis

- **Time Complexity**: O(n) worst case, O(h) best case
  - Worst case: Visit all nodes (e.g., complete binary tree)
  - Best case: O(h) where h is minimum depth (balanced tree with short path)
  - Early termination when finding first leaf
- **Space Complexity**: O(h)
  - Recursion call stack depth
  - h = height of tree = minimum depth in worst case

## Approach 2: Iterative BFS (Optimal for Unbalanced Trees)

Use **level-order traversal** to find the first leaf:

```python
from collections import deque

def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # Found a leaf
        if not node.left and not node.right:
            return depth

        # Add children to queue
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0
```

### How It Works

```
Tree:        3
            / \
           9  20
             / \
            15  7

Queue: [(3, 1)]

Step 1: Process (3, 1)
  - Not a leaf (has 2 children)
  - Add (9, 2) and (20, 2)
  - Queue: [(9, 2), (20, 2)]

Step 2: Process (9, 2)
  - Is a leaf! Return 2
```

### Advantages Over Recursion

- **Better for unbalanced trees**: Stops at first leaf
- **No stack overflow risk**: Uses queue instead of recursion stack
- **Faster practical performance**: BFS explores level by level

### Complexity

- **Time**: O(n) worst case, O(h) best case for unbalanced trees
  - Best case: O(h) - finds first leaf quickly
  - Only visits nodes on path to first leaf
- **Space**: O(w) where w is maximum width
  - Queue stores nodes at current level

## Approach 3: Cleaner Recursive

Simplified version with fewer conditions:

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_depth = self.minDepth(root.left)
    right_depth = self.minDepth(root.right)

    # If one subtree is empty, go down the other
    if left_depth == 0:
        return right_depth + 1
    if right_depth == 0:
        return left_depth + 1

    # Both subtrees exist
    return min(left_depth, right_depth) + 1
```

### Differences

- Clearer variable names
- Checks if subtree depths are 0 (not if children are None)
- Same logic, more readable

### Complexity

- **Time**: O(n) worst case
- **Space**: O(h)

## Approach 4: Recursive with Early Termination

Stop searching once minimum found:

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    # Leaf node
    if not root.left and not root.right:
        return 1

    # Prioritize checking subtree that might be smaller
    left = self.minDepth(root.left) if root.left else float('inf')

    # If left subtree is already minimum possible, don't check right
    if left < float('inf'):
        return min(left + 1, float('inf')) if root.right else left + 1

    return self.minDepth(root.right) + 1
```

### Notes

- More complex optimization
- Generally not worth the added complexity
- BFS approach is cleaner if optimization needed

## Comparison of Approaches

| Approach                    | Time (Best) | Time (Worst) | Space | Use Case                          |
| --------------------------- | ----------- | ------------ | ----- | --------------------------------- |
| Recursive DFS (Implemented) | O(h)        | O(n)         | O(h)  | Simple, balanced trees            |
| Iterative BFS               | O(h)        | O(n)         | O(w)  | Unbalanced trees, avoid recursion |
| Cleaner Recursive           | O(h)        | O(n)         | O(h)  | More readable code                |
| Early Termination           | O(h)        | O(n)         | O(h)  | Microoptimization                 |

**Best Overall**: BFS for unbalanced trees, DFS for balanced trees

## Edge Cases & Considerations

1. **Empty tree**:

   - `root = None` → `0`
   - Base case returns 0

2. **Single node**:

   - `root = [1]` → `1`
   - Leaf node check returns 1

3. **Only left children** (left-skewed):

   - `root = [1,2,3]` (1→2→3)
   - Must traverse all the way down
   - Returns 3 (not 1, which would be wrong)

4. **Only right children** (right-skewed):

   - `root = [1,None,2,None,3]` (1→2→3)
   - Must traverse all the way down
   - Returns 3

5. **Complete binary tree**:

   - Balanced with all levels filled
   - Minimum depth is `log(n) + 1`

6. **Degenerate tree** (like linked list):

   - All nodes have 0 or 1 child
   - Minimum depth equals height
   - BFS significantly faster than DFS

7. **Multiple leaves at same depth**:
   - `root = [1,2,3,4,5]`
   - Several valid leaf nodes at same depth
   - Returns depth of first leaf found

## Common Pitfalls

1. **Not handling single-child nodes**:

   ```python
   # WRONG: Returns 1 for skewed tree
   return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

   # CORRECT: Check for single child
   if root.left is None:
       return self.minDepth(root.right) + 1
   ```

2. **Confusing with max_depth**:

   ```python
   # WRONG: Doesn't check for leaf node requirement
   def minDepth(self, root):
       if not root:
           return 0
       return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

   # CORRECT: Must ensure it's a leaf
   if root.left is None and root.right is None:
       return 1
   ```

3. **Returning 0 instead of continuing path**:

   ```python
   # For node with only one child, returning 0 is wrong
   if root.left is None:
       return 0  # WRONG!

   # Should continue down the existing path
   if root.left is None:
       return self.minDepth(root.right) + 1  # CORRECT
   ```

4. **Using BFS with incorrect termination**:

   ```python
   # WRONG: Stops at any None child (not leaf node)
   if not node.left or not node.right:
       return depth

   # CORRECT: Stop only at leaf (both children None)
   if not node.left and not node.right:
       return depth
   ```

5. **Stack overflow with deeply unbalanced trees**:
   ```python
   # Recursive approach on 10,000 level tree → stack overflow
   # Use BFS instead
   ```

## Optimization Notes

**Time Complexity Considerations**:

- **Balanced tree**: Both DFS and BFS are O(n) in typical case
- **Highly unbalanced tree**: BFS is O(h), DFS is O(n)
  - Skewed tree with 1 million nodes:
    - DFS visits all 1 million nodes
    - BFS finds leaf in O(h) = 1 million steps but stops there
    - Actually, for single-chain tree, both are O(n)
    - BFS shines when there's a short path but deep tree

**When to use which**:

- **DFS Recursive**: Simple, clean code for interview
- **BFS Iterative**: Production code, handles large/unbalanced trees

**Space optimization**:

- Both O(h) and O(w) are logarithmic for balanced trees
- For unbalanced trees, BFS could use more space if tree is wide

## Visual Example

```
Balanced Tree:
            3         depth=1
           / \
          9  20       depth=2
            / \
           15  7      depth=3 (leaves)

Min path: 3→9 (length 2)
Answer: 2


Skewed Tree:
            1         depth=1
            |
            2         depth=2
            |
            3         depth=3 (leaf)

Only valid path: 1→2→3
Must go all the way
Answer: 3 (NOT 1, even though right child missing)


Degenerate Tree:
                    1
                   / \
                  2   3  (3 is leaf, depth 2)
                 /
                4      (4 is leaf, depth 3)
               /
              5        (5 is leaf, depth 4)

Minimum path: 1→3 (length 2)
Answer: 2
```

## Test Cases

```python
# Balanced tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# Expected: 2

# Single node
root = TreeNode(1)
# Expected: 1

# Empty tree
root = None
# Expected: 0

# Left-skewed
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
# Expected: 3

# Right-skewed
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
# Expected: 3

# Wide tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
# Expected: 2

# Complete binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# Expected: 3

# Linear tree (all left)
root = TreeNode(1)
for i in range(2, 6):
    root.left = TreeNode(i)
    root = root.left
# Expected: 5
```

## Thought Process

**Problem analysis**:

- Need to find the minimum depth (shortest path from root to leaf)
- A leaf is a node with no children
- Different from height or max depth

**Key observations**:

1. Must reach an actual **leaf node** (no children)
2. A node with one child is NOT a leaf - must continue
3. Different from max_depth which takes min of both subtrees

**Approach considerations**:

**Why simple min doesn't work**:

```
     1
     |
     2  (has no right child)
     |
     3  (leaf)

If we just do: min(left_depth, right_depth) + 1
- left_depth = minDepth(2) = 1
- right_depth = minDepth(None) = 0
- min(1, 0) + 1 = 1  ← WRONG! Should be 3

We MUST follow the path with a child, not take min of depths.
```

**Correct logic**:

- If no left child, go down right path
- If no right child, go down left path
- If both exist, take minimum
- This ensures we reach an actual leaf

This leads to an O(n) worst case, O(h) best case solution that correctly handles all tree shapes.

## Related Problems

- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
- [112. Path Sum](https://leetcode.com/problems/path-sum/)
