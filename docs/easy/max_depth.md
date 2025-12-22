# Maximum Depth of Binary Tree

## Problem Summary

Given the `root` of a binary tree, return its **maximum depth**. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**LeetCode Problem**: [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Approach 1: Recursive DFS (Implemented)

### Strategy

The implemented solution uses a **recursive depth-first approach**:

1. Base case: If the node is `None`, return 0 (no depth)
2. Recursive case: Return 1 + max(depth of left subtree, depth of right subtree)
3. The maximum depth is the greater of the two subtree depths, plus 1 for the current node

**Code**:

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    else:
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
```

**Cleaner version**:

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### How It Works

**Example Tree**:

```
        3
       / \
      9   20
         /  \
        15   7
```

**Recursive calls**:

```
maxDepth(3):
  left = maxDepth(9):
    left = maxDepth(None) = 0
    right = maxDepth(None) = 0
    return 1 + max(0, 0) = 1

  right = maxDepth(20):
    left = maxDepth(15):
      left = maxDepth(None) = 0
      right = maxDepth(None) = 0
      return 1 + max(0, 0) = 1

    right = maxDepth(7):
      left = maxDepth(None) = 0
      right = maxDepth(None) = 0
      return 1 + max(0, 0) = 1

    return 1 + max(1, 1) = 2

  return 1 + max(1, 2) = 3
```

### Complexity Analysis

- **Time Complexity**: O(n) - Visit each node exactly once
- **Space Complexity**: O(h) - Recursion call stack depth
  - h = height of tree
  - Worst case (skewed tree): O(n)
  - Best case (balanced tree): O(log n)

### Edge Cases Handled

- **Empty tree**: `root = None` → 0
- **Single node**: Only root → 1
- **Skewed tree**: All nodes in one direction → n (number of nodes)
- **Balanced tree**: Depth is log₂(n)

## Approach 2: Iterative BFS with Queue

Use level-order traversal to count levels:

```python
from collections import deque

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
```

### How It Works

- Process tree level by level
- For each level, increment depth counter
- Add all children of current level to queue
- Continue until queue is empty

### Example

```
Tree:     3
         / \
        9   20
           /  \
          15   7

Level 1: [3], depth=1
Level 2: [9, 20], depth=2
Level 3: [15, 7], depth=3

Final depth: 3
```

### Complexity

- **Time**: O(n) - Visit each node once
- **Space**: O(w) - Queue holds at most w nodes (width of tree)
  - w = maximum nodes at any level
  - Worst case: O(n/2) for complete binary tree

### When to Use

- When you need level-by-level processing
- When you want to avoid recursion (stack overflow risk for deep trees)
- When you prefer iterative solutions

## Approach 3: Iterative DFS with Stack

Use a stack to simulate recursive DFS:

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return max_depth
```

### How It Works

- Stack stores pairs: (node, depth_at_that_node)
- Process nodes depth-first
- Track maximum depth seen so far
- Update max_depth as we explore

### Complexity

- **Time**: O(n)
- **Space**: O(h) - Stack depth equals tree height

### Advantages

- No recursion (avoids stack overflow)
- Simulates recursive DFS
- Can track depth explicitly

## Approach 4: Morris Traversal (Advanced)

Traverse without recursion or stack using threading:

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    max_depth = 0
    current = root
    depth = 0

    while current:
        if not current.left:
            depth += 1
            max_depth = max(max_depth, depth)
            current = current.right
        else:
            # Find predecessor
            predecessor = current.left
            temp_depth = 1
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
                temp_depth += 1

            if not predecessor.right:
                predecessor.right = current
                depth += 1
                current = current.left
            else:
                predecessor.right = None
                max_depth = max(max_depth, depth)
                depth -= temp_depth
                current = current.right

    return max_depth
```

### Complexity

- **Time**: O(n)
- **Space**: O(1) - No recursion or stack!

### Drawbacks

- Very complex
- Temporarily modifies tree structure
- Difficult to understand and implement
- Overkill for this problem

## Comparison of Approaches

| Approach         | Time | Space | Pros                         | Cons                   |
| ---------------- | ---- | ----- | ---------------------------- | ---------------------- |
| Recursive DFS    | O(n) | O(h)  | Clean, intuitive, concise    | Stack overflow risk    |
| Iterative BFS    | O(n) | O(w)  | Level-by-level, no recursion | Queue overhead         |
| Iterative DFS    | O(n) | O(h)  | No recursion, explicit depth | More code              |
| Morris Traversal | O(n) | O(1)  | Constant space               | Complex, modifies tree |

**Legend**: h = height, w = width (max nodes at any level)

## Edge Cases & Considerations

1. **Empty Tree**:

   - `root = None` → 0
   - Base case handles this

2. **Single Node**:

   ```
   1
   ```

   - Depth = 1
   - Both subtrees return 0, so 1 + max(0, 0) = 1

3. **Left-Skewed Tree**:

   ```
   1
   /
   2
   /
   3
   ```

   - Depth = 3
   - Each level adds 1

4. **Right-Skewed Tree**:

   ```
   1
    \
     2
      \
       3
   ```

   - Depth = 3
   - Same as left-skewed

5. **Balanced Tree**:

   ```
       1
      / \
     2   3
    / \
   4   5
   ```

   - Depth = 3
   - Efficient O(log n) space

6. **Complete Binary Tree**:
   - All levels fully filled except possibly last
   - Depth = ⌈log₂(n+1)⌉

## Common Pitfalls

1. **Off-by-One Error**:

   ```python
   # WRONG: Not adding 1 for current node
   return max(self.maxDepth(root.left), self.maxDepth(root.right))

   # CORRECT: Add 1 for current node
   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```

2. **Wrong Placement of +1**:

   ```python
   # Less clear (but works)
   return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

   # Better (clearer intent)
   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```

3. **Not Handling None**:

   ```python
   # WRONG: Will cause AttributeError
   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

   # CORRECT: Check for None first
   if not root:
       return 0
   return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   ```

4. **Counting Edges Instead of Nodes**:

   - Problem asks for number of nodes on path, not edges
   - Depth of single node is 1 (not 0)
   - Implementation correctly counts nodes

5. **Modifying Tree in Iterative Solutions**:
   - Don't modify the tree structure
   - Use auxiliary data structures (stack/queue) to track state

## Optimization Notes

The recursive DFS solution is **optimal** for this problem:

- O(n) time - must visit all nodes
- O(h) space - minimal for recursive tree algorithms
- Clean and readable
- Natural expression of the problem

No further optimization needed for typical use cases.

**When to use alternatives**:

- Very deep trees (risk of stack overflow) → Use iterative BFS/DFS
- Need to process level-by-level → Use BFS
- Extreme space constraints → Morris traversal (rarely needed)

## Visual Examples

**Example 1**: Balanced Tree

```
        3           Depth 1
       / \
      9   20        Depth 2
         /  \
        15   7      Depth 3

Maximum Depth: 3
```

**Example 2**: Skewed Tree

```
1                   Depth 1
 \
  2                 Depth 2
   \
    3               Depth 3
     \
      4             Depth 4

Maximum Depth: 4
```

**Example 3**: Single Node

```
1                   Depth 1

Maximum Depth: 1
```

## Test Cases

```python
# Balanced tree
root = [3,9,20,null,null,15,7]
maxDepth(root)  # 3

# Single node
root = [1]
maxDepth(root)  # 1

# Empty tree
root = []
maxDepth(root)  # 0

# Left-skewed
root = [1,2,null,3,null,4]
maxDepth(root)  # 4

# Right-skewed
root = [1,null,2,null,3,null,4]
maxDepth(root)  # 4

# Two nodes
root = [1,2]
maxDepth(root)  # 2

# Complete binary tree
root = [1,2,3,4,5,6,7]
maxDepth(root)  # 3

# Asymmetric tree
root = [1,2,3,4,null,null,5]
maxDepth(root)  # 3

# Deep tree (10 levels)
root = [1,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9,null,10]
maxDepth(root)  # 10
```

## Thought Process

The problem asks for the maximum depth (longest path from root to leaf).

**Key observations**:

1. Depth of a tree = 1 + maximum depth of its subtrees
2. Empty tree has depth 0
3. Leaf node has depth 1

**Recursive insight**:

- The problem has optimal substructure
- Depth of tree = 1 + max(depth of left, depth of right)
- Base case: empty node has depth 0

**Implementation**:

```
maxDepth(node):
  if node is empty:
    return 0
  else:
    return 1 + max(maxDepth(left), maxDepth(right))
```

This naturally leads to a clean recursive solution. The recursion handles the tree traversal, and we just need to define what happens at each node.

**Alternative thought process** (iterative):

- Count levels using BFS
- Each level adds 1 to depth
- Continue until no more nodes

Both approaches work, but recursive is more natural for tree problems.

## Related Problems

- [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [559. Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
