# Same Tree

## Problem Summary

Given the roots of two binary trees `p` and `q`, determine if they are the same tree. Two binary trees are considered the same if they are structurally identical and the nodes have the same values.

**LeetCode Problem**: [100. Same Tree](https://leetcode.com/problems/same-tree/)

## Approach 1: Recursive DFS (Implemented)

### Strategy

The implemented solution uses a recursive depth-first approach:

1. **Base case 1**: If both nodes are `None`, they're the same (return `True`)
2. **Base case 2**: If one is `None` and the other isn't, they're different (return `False`)
3. **Recursive case**: Check if current values match AND left subtrees match AND right subtrees match

**Code**:

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if (p is None and q) or (p and q is None):
        return False

    if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
        return True

    return False
```

### How It Works

The algorithm performs a **simultaneous traversal** of both trees:

```
Tree p:      1              Tree q:      1
           /   \                        /   \
          2     3                      2     3

Step 1: Compare roots (1 == 1) ✓
Step 2: Compare left subtrees (2 == 2) ✓
Step 3: Compare right subtrees (3 == 3) ✓
Result: True
```

For different trees:

```
Tree p:      1              Tree q:      1
           /                              \
          2                                2

Step 1: Compare roots (1 == 1) ✓
Step 2: Compare left subtrees (2 vs None) ✗
Result: False
```

### Complexity Analysis

- **Time Complexity**: O(min(n, m)) - where n and m are the number of nodes in each tree
  - We traverse all nodes until we find a mismatch
  - In the worst case (identical trees), we visit all nodes
- **Space Complexity**: O(min(h₁, h₂)) - where h₁ and h₂ are the heights
  - Due to recursion call stack
  - Worst case: O(n) for skewed tree
  - Best case: O(log n) for balanced tree

### Edge Cases Handled

- **Both trees empty**: `None` and `None` → `True` ✓
- **One tree empty**: `None` and `TreeNode` → `False` ✓
- **Different structures**: Left child vs right child → `False` ✓
- **Different values**: Same structure, different values → `False` ✓
- **Single node trees**: Works correctly

## Approach 2: Cleaner Recursive (Optimized)

A more concise version that combines all checks:

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Both None - identical
    if not p and not q:
        return True

    # One is None - different
    if not p or not q:
        return True

    # Check value and recurse on children
    return (p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))
```

### Improvements

- More Pythonic with `not p` instead of `p is None`
- Clearer logic flow
- Single return statement for recursive case
- Same complexity as original

## Approach 3: Iterative BFS with Queue

Use a queue to perform level-order traversal of both trees simultaneously:

```python
from collections import deque

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = deque([(p, q)])

    while queue:
        node1, node2 = queue.popleft()

        # Both None - continue
        if not node1 and not node2:
            continue

        # One is None or values differ - not same
        if not node1 or not node2 or node1.val != node2.val:
            return False

        # Add children to queue
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))

    return True
```

### How It Works

- Process nodes level by level
- Queue stores pairs of corresponding nodes
- Compare each pair and add their children

### Complexity

- **Time**: O(min(n, m)) - Same as recursive
- **Space**: O(min(n, m)) - Queue can hold up to one level of nodes

### When to Use

- When you want to avoid recursion (no stack overflow risk)
- When you prefer iterative solutions
- When debugging level-by-level is easier

## Approach 4: Iterative DFS with Stack

Use a stack for depth-first traversal:

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()

        # Both None - continue
        if not node1 and not node2:
            continue

        # One is None or values differ - not same
        if not node1 or not node2 or node1.val != node2.val:
            return False

        # Add children to stack (order matters for DFS)
        stack.append((node1.right, node2.right))
        stack.append((node1.left, node2.left))

    return True
```

### Complexity

- **Time**: O(min(n, m))
- **Space**: O(min(h₁, h₂)) - Stack depth equals tree height

### Difference from BFS

- DFS explores depth-first (goes deep before wide)
- BFS explores breadth-first (goes wide before deep)
- Both work correctly; choice is stylistic

## Approach 5: Serialization Comparison

Serialize both trees to strings and compare:

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def serialize(node):
        if not node:
            return "N"
        return f"{node.val},{serialize(node.left)},{serialize(node.right)}"

    return serialize(p) == serialize(q)
```

### Complexity

- **Time**: O(n + m) - Must serialize both trees completely
- **Space**: O(n + m) - Store both serialization strings

### Drawbacks

- Less efficient (must traverse entire trees even if early difference)
- Uses more space (stores string representations)
- Not recommended for this problem

## Comparison of Approaches

| Approach      | Time        | Space  | Pros                               | Cons                               |
| ------------- | ----------- | ------ | ---------------------------------- | ---------------------------------- |
| Recursive DFS | O(min(n,m)) | O(h)   | Clean, intuitive, concise          | Stack overflow risk for deep trees |
| Iterative BFS | O(min(n,m)) | O(w)   | No recursion, level-by-level       | More code, queue overhead          |
| Iterative DFS | O(min(n,m)) | O(h)   | No recursion, similar to recursive | More code than recursive           |
| Serialization | O(n+m)      | O(n+m) | Simple concept                     | Inefficient, no early termination  |

**Legend**: h = height, w = width (max nodes at any level)

## Edge Cases & Considerations

1. **Both Trees Empty**:

   - `p = None, q = None` → `True`
   - Correctly handled by first condition

2. **One Tree Empty**:

   - `p = TreeNode(1), q = None` → `False`
   - `p = None, q = TreeNode(1)` → `False`
   - Correctly handled by second condition

3. **Different Structures**:

   ```
   p: 1        q: 1
     /              \
    2                2
   ```

   - Should return `False`
   - Detected when comparing children

4. **Same Structure, Different Values**:

   ```
   p: 1        q: 1
     / \          / \
    2   3        3   2
   ```

   - Should return `False`
   - Detected by value comparison

5. **Deep Trees**:

   - Recursive approach may cause stack overflow for extremely deep trees
   - Iterative approaches are safer

6. **Large Trees**:
   - All approaches efficiently handle large trees
   - Early termination on first mismatch is important

## Common Pitfalls

1. **Incorrect Null Handling**:

   ```python
   # WRONG: Will throw AttributeError when accessing None.val
   if p.val == q.val:
       return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
   ```

   Must check for `None` before accessing `val`.

2. **Missing Structural Check**:

   ```python
   # WRONG: Doesn't check if both are None or one is None
   return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
   ```

   Must handle the cases where nodes are `None`.

3. **Forgetting to Check Both Children**:

   ```python
   # WRONG: Only checks left children
   return p.val == q.val and self.isSameTree(p.left, q.left)
   ```

   Must check both left AND right subtrees.

4. **Order Matters in Comparisons**:

   ```python
   # WRONG: Comparing left with right
   return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
   ```

   Must compare corresponding positions: left with left, right with right.

5. **Not Using Short-Circuit Evaluation**:
   - The `and` operator in Python short-circuits
   - If `p.val != q.val`, the recursive calls don't execute
   - This is efficient and correct

## Optimization Notes

The recursive DFS solution is **optimal** for this problem:

- Minimal code
- Clear logic
- Early termination on first mismatch
- No unnecessary space overhead

Potential optimizations:

1. **Early termination**: Already implemented (returns `False` on first mismatch)
2. **Avoid unnecessary comparisons**: The `and` operator short-circuits automatically
3. **Iterative for very deep trees**: Use iterative approach to avoid stack overflow

## Test Cases

```python
# Identical trees
p = [1,2,3]
q = [1,2,3]
isSameTree(p, q)  # True

# Different structure
p = [1,2]
q = [1,null,2]
isSameTree(p, q)  # False

# Different values
p = [1,2,1]
q = [1,1,2]
isSameTree(p, q)  # False

# Both empty
p = []
q = []
isSameTree(p, q)  # True

# One empty
p = [1]
q = []
isSameTree(p, q)  # False

# Single node, same
p = [1]
q = [1]
isSameTree(p, q)  # True

# Single node, different
p = [1]
q = [2]
isSameTree(p, q)  # False

# Large identical trees
p = [1,2,3,4,5,6,7]
q = [1,2,3,4,5,6,7]
isSameTree(p, q)  # True

# Subtly different
p = [1,2,3,4]
q = [1,2,3,null,4]
isSameTree(p, q)  # False
```

## Thought Process

The problem asks whether two binary trees are identical in both structure and values. The natural approach is to:

1. **Handle base cases**:

   - If both are empty, they're the same
   - If one is empty, they're different

2. **Compare current nodes**:

   - Values must match

3. **Recurse on subtrees**:
   - Left subtrees must match
   - Right subtrees must match

The recursive solution elegantly mirrors this logical structure. The key insight is that two trees are the same if and only if:

- Their roots have the same value
- Their left subtrees are the same
- Their right subtrees are the same

This naturally leads to a recursive solution with O(n) time and O(h) space complexity.

## Related Problems

- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
