# Sum of Left Leaves

## Problem Summary

Given the `root` of a binary tree, return the **sum of all left leaves**.

A **left leaf** is a leaf node which is the left child of its parent node.

**LeetCode Problem**: [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)

## Approach: DFS with Parent Context (Implemented)

### Strategy

The implemented solution uses **depth-first search (DFS) with a flag to track if a node is a left child**:

1. Use a recursive helper function that takes current node and a boolean flag `left`
2. The flag indicates whether the current node is the left child of its parent
3. Recursively traverse left subtree (passing `True`) and right subtree (passing `False`)
4. When reaching a leaf node, check if it's a left leaf (`not left child and not right child and left=True`)
5. If it's a left leaf, add its value to the total

**Code**:

```python
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    self.total = 0

    def dfs(node, left):
        if not node:
            return

        dfs(node.left, True)
        dfs(node.right, False)

        if not node.left and not node.right and left:
            self.total += node.val

    dfs(root, False)
    return self.total
```

### How It Works

**Key insight**: A left leaf is identified by two conditions:

1. It's a leaf (no left and no right children)
2. It's a left child of its parent (flag `left = True`)

**Example 1**: Binary tree structure

```
Tree:
        3
       / \
      9   20
         /  \
        15   7

DFS traversal:

dfs(3, False):  # Root has no parent context
  dfs(3.left=9, True):  # 9 is left child of 3
    dfs(9.left=None, True):
      return
    dfs(9.right=None, False):
      return

    Check: 9 is leaf? Yes (no left, no right)
    Check: is left child? Yes (left=True)
    Add 9 to total → total = 9 ✓

  dfs(3.right=20, False):  # 20 is right child of 3
    dfs(20.left=15, True):  # 15 is left child of 20
      dfs(15.left=None, True):
        return
      dfs(15.right=None, False):
        return

      Check: 15 is leaf? Yes (no left, no right)
      Check: is left child? Yes (left=True)
      Add 15 to total → total = 9 + 15 = 24 ✓

    dfs(20.right=7, False):  # 7 is right child of 20
      dfs(7.left=None, True):
        return
      dfs(7.right=None, False):
        return

      Check: 7 is leaf? Yes (no left, no right)
      Check: is left child? No (left=False)
      Don't add 7 (it's a right leaf, not left leaf)

    Check: 20 is leaf? No (has left and right children)
    Don't add 20

  Check: 3 is leaf? No (has left and right children)
  Don't add 3

Return total = 24 ✓
```

**Example 2**: Single node

```
Tree:
  1

dfs(1, False):  # Root has no parent context
  dfs(1.left=None, True):
    return
  dfs(1.right=None, False):
    return

  Check: 1 is leaf? Yes (no left, no right)
  Check: is left child? No (left=False, root has no parent)
  Don't add 1

Return total = 0 ✓
```

**Example 3**: Only left child

```
Tree:
    1
   /
  2

dfs(1, False):
  dfs(1.left=2, True):  # 2 is left child of 1
    dfs(2.left=None, True):
      return
    dfs(2.right=None, False):
      return

    Check: 2 is leaf? Yes
    Check: is left child? Yes (left=True)
    Add 2 → total = 2 ✓

  dfs(1.right=None, False):
    return

  Check: 1 is leaf? No
  Don't add 1

Return total = 2 ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Visit each node exactly once in DFS
  - n = number of nodes in tree
  - Constant work at each node
- **Space Complexity**: O(h)
  - Recursion call stack depth
  - h = height of tree
  - Worst case: O(n) for skewed tree
  - Average case: O(log n) for balanced tree

### Advantages

- **Efficient**: O(n) time, visits each node once
- **Clear logic**: Explicit flag makes intent obvious
- **Single pass**: Only one DFS traversal needed
- **Simple**: Easy to understand and implement

### Disadvantages

- **Uses class variable**: `self.total` requires state management
- **Not pure function**: Modifies instance state
- **Requires parent context**: Can't easily work with iterative approach

## Alternative Approach 1: Return from Recursion

Return the sum instead of using class variable:

```python
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def dfs(node, is_left):
        if not node:
            return 0

        # If leaf and left child, add it
        if not node.left and not node.right and is_left:
            return node.val

        # Otherwise, sum left and right subtrees
        return dfs(node.left, True) + dfs(node.right, False)

    return dfs(root, False)
```

### How It Works

**Recursive return pattern**:

- Each call returns the sum of left leaves in its subtree
- Leaf nodes return their value (if left) or 0
- Internal nodes return sum of both subtrees

**Example**: `[3, 9, 20, null, null, 15, 7]`

```
dfs(3, False):
  Is leaf? No, so sum subtrees

  dfs(3.left=9, True):
    Is leaf and left? Yes → return 9

  dfs(3.right=20, False):
    Is leaf? No, so sum subtrees

    dfs(20.left=15, True):
      Is leaf and left? Yes → return 15

    dfs(20.right=7, False):
      Is leaf but not left? → return 0

    Return 15 + 0 = 15

  Return 9 + 15 = 24 ✓
```

### Complexity

- **Time**: O(n) - visit each node once
- **Space**: O(h) - recursion stack

### Advantages

- **Pure function**: No mutable state
- **More functional**: Returns values instead of modifying state
- **Cleaner**: Standard recursive pattern

### Disadvantages

- **Redundant checks**: Evaluates leaf condition separately
- **Similar complexity**: Same as original approach

## Alternative Approach 2: Post-order Traversal

Use explicit post-order traversal (Left → Right → Root):

```python
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    total = 0

    def dfs(node, is_left):
        nonlocal total

        if not node:
            return

        # Post-order: Left, Right, Root
        dfs(node.left, True)
        dfs(node.right, False)

        # Process node after children
        if not node.left and not node.right and is_left:
            total += node.val

    dfs(root, False)
    return total
```

### How It Works

Explicitly uses post-order traversal pattern:

- Process left subtree first
- Then right subtree
- Finally check current node

### Complexity

- **Time**: O(n)
- **Space**: O(h)

### Advantages

- **Explicit traversal order**: Clear post-order pattern
- **Uses nonlocal**: Less stateful than class variable

### Disadvantages

- **Requires nonlocal**: Less clean than pure recursion
- **More verbose**: Extra keyword needed

## Alternative Approach 3: Iterative with Stack

Use stack-based iterative traversal:

```python
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    # Stack stores (node, is_left_child)
    stack = [(root, False)]
    total = 0

    while stack:
        node, is_left = stack.pop()

        # Check if left leaf
        if not node.left and not node.right and is_left:
            total += node.val

        # Add children to stack (right first for pre-order)
        if node.right:
            stack.append((node.right, False))
        if node.left:
            stack.append((node.left, True))

    return total
```

### How It Works

**Stack-based traversal**:

- Use stack instead of recursion
- Each element stores node and whether it's left child
- Process nodes one by one

**Example**: `[3, 9, 20, null, null, 15, 7]`

```
stack = [(3, False)]

Pop (3, False):
  Is leaf and left? No
  Push (20, False), then (9, True)
  stack = [(20, False), (9, True)]

Pop (9, True):
  Is leaf and left? Yes → total = 9
  No children
  stack = [(20, False)]

Pop (20, False):
  Is leaf and left? No
  Push (7, False), then (15, True)
  stack = [(7, False), (15, True)]

Pop (15, True):
  Is leaf and left? Yes → total = 24
  No children
  stack = [(7, False)]

Pop (7, False):
  Is leaf and left? No
  No children
  stack = []

Return total = 24 ✓
```

### Complexity

- **Time**: O(n) - visit each node
- **Space**: O(h) - stack size

### Advantages

- **No recursion**: Avoids call stack
- **Explicit control**: More predictable
- **Iterative pattern**: Familiar to imperative programmers

### Disadvantages

- **More code**: Explicit stack management
- **Less elegant**: More verbose than recursion

## Comparison of Approaches

| Approach                    | Time | Space | Difficulty | Pros             | Cons                |
| --------------------------- | ---- | ----- | ---------- | ---------------- | ------------------- |
| DFS with flag (Implemented) | O(n) | O(h)  | Easy       | Clear, efficient | Class state         |
| Return from recursion       | O(n) | O(h)  | Easy       | Pure function    | Separate leaf check |
| Post-order explicit         | O(n) | O(h)  | Easy       | Clear pattern    | Uses nonlocal       |
| Iterative stack             | O(n) | O(h)  | Medium     | No recursion     | More code           |

**Winner**: Return from recursion for cleanliness and functionality

## Edge Cases & Considerations

1. **Empty tree**:

   - `root = None` → `0`
   - Base case: dfs returns early ✓

2. **Single node**:

   - `root = 1` → `0`
   - Root has no parent, never counted as left leaf ✓

3. **Only left child**:

   - `root = 1, root.left = 2` → `2`
   - 2 is a left leaf ✓

4. **Only right child**:

   - `root = 1, root.right = 2` → `0`
   - No left leaves exist ✓

5. **Left child is internal node**:

   - `root = 1, root.left = 2, root.left.left = 3`
   - 2 is not a leaf, so don't count it
   - 3 is a left leaf ✓

6. **Balanced tree**:

   - Perfect binary tree with many nodes
   - Correctly identifies all left leaves ✓

7. **Skewed tree (left)**:

   - All nodes left child of parent
   - Recursion depth = n
   - Still O(h) = O(n) ✓

8. **Skewed tree (right)**:

   - All nodes right child of parent
   - No left leaves exist
   - Return 0 ✓

9. **Negative values**:

   - Tree with negative node values
   - Sum correctly includes negatives ✓

10. **Large values**:
    - Integer overflow possible in some languages
    - Python handles arbitrary precision ✓

## Key Insight

**Left leaf definition requires two conditions**:

1. **Is a leaf**: No left child AND no right child
2. **Is left child**: Parent's left child (tracked by `is_left` flag)

A node that's a left child but has children is NOT a left leaf. For example:

```
    1
   / \
  2   3
 /
4

Node 2 is a left child of 1, but NOT a left leaf (has child 4)
Node 4 IS a left leaf (left child of 2 AND has no children)
```

## Common Pitfalls

1. **Counting all left children**:

   ```python
   # WRONG: Counts internal left nodes too
   if is_left:
       total += node.val

   # CORRECT: Only leaf left children
   if not node.left and not node.right and is_left:
       total += node.val
   ```

2. **Using wrong traversal order**:

   ```python
   # WRONG: Checking leaf before recursing (wrong order)
   if not node.left and not node.right and is_left:
       total += node.val
   dfs(node.left, True)
   dfs(node.right, False)

   # CORRECT: Recurse first, then check (post-order)
   dfs(node.left, True)
   dfs(node.right, False)
   if not node.left and not node.right and is_left:
       total += node.val
   ```

3. **Not tracking parent context**:

   ```python
   # WRONG: No way to know if node is left child
   def dfs(node):
       if is_leaf(node):
           total += node.val  # All leaves counted!

   # CORRECT: Track parent relationship
   def dfs(node, is_left):
       if is_leaf(node) and is_left:
           total += node.val
   ```

4. **Forgetting root has no parent context**:

   ```python
   # Starting with True
   dfs(root, True)  # Root isn't any child!

   # CORRECT: Start with False
   dfs(root, False)  # Root has no parent
   ```

5. **Modifying flag incorrectly**:

   ```python
   # WRONG: Both children get same flag
   dfs(node.left, left)
   dfs(node.right, left)

   # CORRECT: Left gets True, right gets False
   dfs(node.left, True)
   dfs(node.right, False)
   ```

## Optimization Notes

The implemented solution is **already optimal**:

- **Time**: O(n) - must visit every node to find all left leaves
- **Space**: O(h) - recursion depth for any tree algorithm
- **Single pass**: Only one DFS traversal

**Interview tips**:

- Explain the two conditions for left leaf
- Show why the flag is necessary
- Walk through a concrete example
- Mention that internal left nodes don't count
- Discuss alternative approaches (return vs class variable)

**Key insight for interviews**:

```
This problem combines two concepts:
1. Tree traversal (DFS/recursion)
2. Tracking node relationships (parent context via flag)

The flag is crucial because we need to know if a node
is the LEFT child of its parent, not just any child.
```

## Visual Example

```
Original tree:
        3
       / \
      9   20
         /  \
        15   7

Marking which nodes are left children:

        3 (no parent)
       / \
      9   20 (right child)
    (left)  / \
           15   7
        (left) (right)

Left leaves (left child AND leaf):
- 9: left child ✓, leaf ✓ → COUNT
- 15: left child ✓, leaf ✓ → COUNT
- 7: right child ✗, leaf ✓ → DON'T COUNT

Sum = 9 + 15 = 24 ✓


Another tree:
      1
     / \
    2   3
   / \
  4   5

Left leaves:
- 2: left child ✓, leaf ✗ (has children) → DON'T COUNT
- 4: left child ✓, leaf ✓ → COUNT
- 5: right child ✗, leaf ✓ → DON'T COUNT

Sum = 4 ✓
```

## Test Cases

```python
# Basic example
#     3
#    / \
#   9   20
#      /  \
#     15   7
sumOfLeftLeaves([3,9,20,None,None,15,7])     # 24

# Single node (root)
sumOfLeftLeaves([1])                         # 0

# Only left child (is a leaf)
sumOfLeftLeaves([1,2])                       # 2

# Only right child (no left leaves)
sumOfLeftLeaves([1,None,3])                  # 0

# Left child with children
#     1
#    /
#   2
#  /
# 4
sumOfLeftLeaves([1,2,None,4])                # 4

# No nodes
sumOfLeftLeaves(None)                        # 0

# Multiple left leaves
#       1
#      / \
#     2   3
#    /
#   4
sumOfLeftLeaves([1,2,3,4])                   # 4

# Multiple levels
#       1
#      /
#     2
#    /
#   3
sumOfLeftLeaves([1,2,None,3])                # 3

# Balanced tree with multiple left leaves
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
sumOfLeftLeaves([1,2,3,4,5,6,7])             # 4 + 6 = 10

# All right skewed (no left leaves)
#     1
#      \
#       2
#        \
#         3
sumOfLeftLeaves([1,None,2,None,3])           # 0

# Negative values
sumOfLeftLeaves([1,-2,None,-4])              # -4
```

## Thought Process

**Problem analysis**:

- Need to identify left leaves specifically
- A left leaf has two conditions:
  1. It's a leaf (terminal node)
  2. It's a left child of its parent
- Sum all values of nodes meeting both conditions

**Key observations**:

1. Can't just count all left children (some might be internal)
2. Can't just count all leaves (some might be right children)
3. Need to track parent-child relationship
4. Tree traversal (DFS) naturally explores all nodes

**Algorithm insight**:

```
For each node:
  1. Recurse on left child (mark as left)
  2. Recurse on right child (mark as right)
  3. If node is leaf AND marked as left: add to sum

The "mark" (is_left flag) tracks the parent relationship.
```

**Why this approach works**:

- DFS visits all nodes in a systematic way
- Flag tells us parent relationship
- Check both conditions before counting
- Single pass, efficient

**Optimal solution**:

- Time: O(n) - must check every node
- Space: O(h) - recursion depth
- Both are optimal (can't do better)

**Interview strategy**:

1. Define what makes a "left leaf"
2. Explain why both conditions matter
3. Show need for parent context flag
4. Code the recursive solution
5. Walk through example
6. Analyze complexity
7. Mention alternatives

This problem tests:

- Tree traversal (DFS/recursion)
- Node relationships in trees
- Understanding problem constraints
- State tracking in recursion
- Edge case handling

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
