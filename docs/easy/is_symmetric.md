# Symmetric Tree

## Problem Summary

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**LeetCode Problem**: [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

## Approach 1: Recursive Mirror Check (Implemented)

### Strategy

The implemented solution uses a **recursive helper function** to check if two subtrees are mirrors of each other:

1. Define a helper function `isMirror(left, right)` that checks if two trees are mirrors
2. For the main tree, check if `root.left` and `root.right` are mirrors
3. Two trees are mirrors if:
   - Both are `None` (base case: symmetric)
   - Both exist with same values AND their outer/inner children are mirrors
   - Left's left ↔ Right's right (outer pair)
   - Left's right ↔ Right's left (inner pair)

**Code**:

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isMirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (left.val == right.val) and
               isMirror(left.left, right.right) and
               isMirror(left.right, right.left)

    if root is None:
        return True

    return isMirror(root.left, root.right)
```

### How It Works

**Symmetric Tree**:

```
        1
       / \
      2   2
     / \ / \
    3  4 4  3

Check: isMirror(left=2, right=2)
  - Values match: 2 == 2 ✓
  - Outer: isMirror(left.left=3, right.right=3) ✓
  - Inner: isMirror(left.right=4, right.left=4) ✓
Result: True
```

**Non-Symmetric Tree**:

```
        1
       / \
      2   2
       \   \
        3   3

Check: isMirror(left=2, right=2)
  - Values match: 2 == 2 ✓
  - Outer: isMirror(left.left=None, right.right=3) ✗
  - One is None, other isn't
Result: False
```

### Key Insight: Mirror Comparison

For symmetry, we compare:

- **Outer edges**: `left.left` with `right.right`
- **Inner edges**: `left.right` with `right.left`

This is different from checking if two trees are identical (which would compare `left.left` with `right.left`).

### Complexity Analysis

- **Time Complexity**: O(n) - Visit each node once
- **Space Complexity**: O(h) - Recursion stack depth
  - h = height of tree
  - Worst case (skewed): O(n)
  - Best case (balanced): O(log n)

### Edge Cases Handled

- **Empty tree**: `root = None` → `True` (by definition)
- **Single node**: Only root, no children → `True` (leaf is symmetric)
- **Two nodes**: One child → `False` (not symmetric)
- **Null children**: Properly handles when one subtree has children and other doesn't

## Approach 2: Iterative with Queue (BFS)

Use a queue to compare nodes level-by-level:

```python
from collections import deque

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()

        # Both None - continue checking
        if not left and not right:
            continue

        # One is None or values differ - not symmetric
        if not left or not right or left.val != right.val:
            return False

        # Add outer and inner pairs
        queue.append((left.left, right.right))  # Outer pair
        queue.append((left.right, right.left))  # Inner pair

    return True
```

### How It Works

- Use a queue to store pairs of nodes that should be mirrors
- Process each pair: check if they're equal and enqueue their children
- Order matters: enqueue outer pairs and inner pairs correctly

### Complexity

- **Time**: O(n) - Visit each node once
- **Space**: O(w) - Queue can hold up to width of tree
  - w = maximum nodes at any level
  - Worst case: O(n/2) for complete binary tree

### When to Use

- When you want to avoid recursion (no stack overflow risk)
- When you prefer iterative solutions
- Similar performance to recursive approach

## Approach 3: Iterative with Stack (DFS)

Similar to queue approach, but using a stack for DFS:

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False

        # Add pairs to stack
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))

    return True
```

### Complexity

- **Time**: O(n)
- **Space**: O(h) - Stack depth equals tree height

### Difference from Queue

- Stack (DFS): Explores depth-first
- Queue (BFS): Explores breadth-first
- Both work correctly; choice is stylistic

## Approach 4: Level-Order Comparison

Check if each level reads the same forwards and backwards:

```python
from collections import deque

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_vals = []

        for _ in range(level_size):
            node = queue.popleft()

            if node:
                level_vals.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_vals.append(None)

        # Check if level is palindrome
        if level_vals != level_vals[::-1]:
            return False

    return True
```

### Complexity

- **Time**: O(n)
- **Space**: O(w) - Queue and level array

### Drawback

- Less efficient (stores all level values)
- More complex logic
- Not recommended; first approach is cleaner

## Comparison of Approaches

| Approach         | Time | Space | Pros                               | Cons                          |
| ---------------- | ---- | ----- | ---------------------------------- | ----------------------------- |
| Recursive Mirror | O(n) | O(h)  | Clean, intuitive, concise          | Stack overflow for deep trees |
| Iterative BFS    | O(n) | O(w)  | No recursion, level-by-level       | More code                     |
| Iterative DFS    | O(n) | O(h)  | No recursion, similar to recursive | More code                     |
| Level Palindrome | O(n) | O(w)  | Conceptually simple                | Inefficient, complex          |

**Legend**: h = height, w = width (max nodes at any level)

## Edge Cases & Considerations

1. **Empty Tree**:

   - `root = None` → `True`
   - By definition, an empty tree is symmetric
   - Handled by initial check

2. **Single Node**:

   ```
   1
   ```

   - Only root, no children → `True`
   - `isMirror(None, None)` returns `True`

3. **Two Nodes (Asymmetric)**:

   ```
   1
   /
   2
   ```

   - Left child but no right → `False`
   - `isMirror(TreeNode(2), None)` returns `False`

4. **Perfect Symmetry**:

   ```
       1
      / \
     2   2
    / \ / \
   3  4 4  3
   ```

   - All levels are symmetric → `True`

5. **Value Match but Structure Mismatch**:

   ```
       1
      / \
     2   2
      \   \
       3   3
   ```

   - Same values but different positions → `False`
   - Structure must also be symmetric

6. **Deep Trees**:
   - Recursive approach may cause stack overflow
   - Iterative approach is safer for very deep trees

## Common Pitfalls

1. **Wrong Comparison Order**:

   ```python
   # WRONG: Comparing left.left with right.left (same tree check, not mirror)
   return isMirror(left.left, right.left) and isMirror(left.right, right.right)

   # CORRECT: Comparing outer and inner pairs
   return isMirror(left.left, right.right) and isMirror(left.right, right.left)
   ```

2. **Forgetting to Check Values**:

   ```python
   # WRONG: Only checking structure
   return isMirror(left.left, right.right) and isMirror(left.right, right.left)

   # CORRECT: Must also check values match
   return (left.val == right.val) and isMirror(...) and isMirror(...)
   ```

3. **Incorrect Null Handling**:

   ```python
   # WRONG: Will cause AttributeError
   if left.val == right.val:
       return isMirror(...)

   # CORRECT: Check for None first
   if left is None and right is None:
       return True
   if left is None or right is None:
       return False
   ```

4. **Checking Root Incorrectly**:

   ```python
   # WRONG: Checking if entire tree equals itself
   return isMirror(root, root)

   # CORRECT: Check if left and right subtrees are mirrors
   return isMirror(root.left, root.right)
   ```

5. **Using `==` Instead of `is` for None**:
   - Both work, but `is None` is more Pythonic and slightly faster
   - `is` checks identity, `==` checks equality

## Optimization Notes

The recursive mirror check is **optimal** for this problem:

- Clean and intuitive
- O(n) time - must visit all nodes
- O(h) space - minimal for tree problems

Potential optimizations:

1. **Early termination**: Already implemented (returns `False` on first mismatch)
2. **Iterative for very deep trees**: Use queue/stack approach
3. **No further optimization possible**: Must check all nodes for complete verification

## Visual Example

**Symmetric Tree**:

```
        1           → Root
       / \
      2   2         → Compare these
     / \ / \
    3  4 4  3       → Compare outer (3↔3) and inner (4↔4)

Mirror pairs:
- (2, 2) with values match ✓
  - Outer: (3, 3) ✓
  - Inner: (4, 4) ✓
Result: True
```

**Non-Symmetric Tree**:

```
        1           → Root
       / \
      2   2         → Compare these
       \   \
        3   3       → Compare outer (None↔3) fails

Mirror pairs:
- (2, 2) with values match ✓
  - Outer: (None, 3) ✗ One is None
Result: False
```

## Test Cases

```python
# Symmetric tree
root = [1,2,2,3,4,4,3]
isSymmetric(root)  # True

# Non-symmetric (structure)
root = [1,2,2,null,3,null,3]
isSymmetric(root)  # False

# Non-symmetric (values)
root = [1,2,2,3,4,5,3]
isSymmetric(root)  # False (4 ≠ 5)

# Empty tree
root = []
isSymmetric(root)  # True

# Single node
root = [1]
isSymmetric(root)  # True

# Two levels symmetric
root = [1,2,2]
isSymmetric(root)  # True

# Two levels asymmetric
root = [1,2,3]
isSymmetric(root)  # False

# Deep symmetric tree
root = [1,2,2,3,4,4,3,5,null,null,null,null,null,null,5]
isSymmetric(root)  # True

# All same values but asymmetric
root = [1,1,1,1,1,null,1]
isSymmetric(root)  # False (structure different)
```

## Thought Process

The problem asks if a binary tree is symmetric around its center. This is equivalent to asking if the left and right subtrees are **mirror images** of each other.

**Key insights**:

1. A tree is symmetric if its left and right subtrees are mirrors
2. Two trees are mirrors if:
   - Both roots have the same value
   - Left tree's left subtree mirrors right tree's right subtree (outer pair)
   - Left tree's right subtree mirrors right tree's left subtree (inner pair)

**Why not check if left == right?**

- That would check if they're identical, not mirrored
- Mirror requires crossing comparison: left's left with right's right

**Implementation approach**:

- Recursive solution naturally expresses the mirror relationship
- Base cases handle null nodes
- Recursive cases check values and cross-compare children

This gives us O(n) time and O(h) space - optimal for this problem.

## Related Problems

- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [951. Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
