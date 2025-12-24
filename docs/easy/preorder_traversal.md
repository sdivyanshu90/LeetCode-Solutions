# Binary Tree Preorder Traversal

## Problem Summary

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

In preorder traversal, we visit nodes in this order: **Root → Left → Right**

**LeetCode Problem**: [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

**Follow-up**: Recursive solution is trivial, could you do it iteratively?

## Approach 1: Recursive DFS (Implemented)

### Strategy

The implemented solution uses a **recursive depth-first search** approach:

1. Handle base case: if node is `None`, return
2. Use a helper function `dfs` to traverse the tree
3. Process current node first (append to result)
4. Visit left subtree (recursive call)
5. Visit right subtree (recursive call)
6. Order: **Root → Left → Right**

**Code**:

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    res = []
    def dfs(node):
        if not node:
            return

        res.append(node.val)  # Process root
        dfs(node.left)         # Visit left
        dfs(node.right)        # Visit right

    dfs(root)
    return res
```

### How It Works

**Example 1**:

```
Tree:    1
          \
           2
          /
         3

Preorder: Root → Left → Right

Execution:
  dfs(1):
    append 1 → [1]
    dfs(left=None): return
    dfs(right=2):
      append 2 → [1, 2]
      dfs(left=3):
        append 3 → [1, 2, 3]
        dfs(left=None): return
        dfs(right=None): return
      dfs(right=None): return

Result: [1, 2, 3] ✓
```

**Example 2**:

```
Tree:      1
          / \
         2   3

Preorder: Root → Left → Right

Execution:
  dfs(1):
    append 1 → [1]
    dfs(left=2):
      append 2 → [1, 2]
      dfs(left=None): return
      dfs(right=None): return
    dfs(right=3):
      append 3 → [1, 2, 3]
      dfs(left=None): return
      dfs(right=None): return

Result: [1, 2, 3] ✓
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Visit each node exactly once
  - n = number of nodes in tree
- **Space Complexity**: O(h)
  - Recursion call stack depth
  - h = height of tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

### Advantages

- **Simple and intuitive**: Natural recursive implementation
- **Clean code**: Easy to read and understand
- **Standard approach**: Most common for interviews

### Disadvantages

- **Stack space**: Uses recursion stack
- **Not iterative**: Doesn't satisfy follow-up requirement

## Approach 2: Iterative with Stack

Use an explicit stack to simulate recursion:

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first, then left (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### How It Works

**Key insight**: Stack is LIFO, so push right before left

**Example**:

```
Tree:    1
        / \
       2   3

stack: [1]
result: []

Step 1: Pop 1
  result: [1]
  Push right=3, then left=2
  stack: [3, 2]

Step 2: Pop 2 (left child)
  result: [1, 2]
  No children
  stack: [3]

Step 3: Pop 3 (right child)
  result: [1, 2, 3]
  No children
  stack: []

Result: [1, 2, 3] ✓
```

### Complexity

- **Time**: O(n)
- **Space**: O(h) - Stack stores at most h nodes

### Advantages

- **Iterative**: Satisfies follow-up requirement
- **Explicit control**: No hidden recursion stack
- **Simple logic**: Easy to understand

### Disadvantages

- **More code**: Slightly longer than recursive
- **Manual stack management**: Need to track stack explicitly

## Approach 3: Morris Traversal

O(1) space solution using tree threading:

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    current = root

    while current:
        if current.left is None:
            # No left child, process current and go right
            result.append(current.val)
            current = current.right
        else:
            # Find predecessor (rightmost node in left subtree)
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # Create thread and process current
                result.append(current.val)
                predecessor.right = current
                current = current.left
            else:
                # Remove thread and go right
                predecessor.right = None
                current = current.right

    return result
```

### How It Works

**Key idea**: Temporarily modify tree to create "threads" back to ancestor nodes

**Steps**:

1. If no left child: process node, go right
2. If left child exists:
   - Find predecessor (rightmost in left subtree)
   - If predecessor.right is None: create thread, process node, go left
   - If predecessor.right points to current: remove thread, go right

### Complexity

- **Time**: O(n)
- **Space**: O(1) - No stack, only pointers

### Advantages

- **Optimal space**: True O(1) space
- **No recursion or stack**: Pure iteration

### Disadvantages

- **Complex logic**: Hard to understand and implement
- **Modifies tree temporarily**: Creates and removes threads
- **Rarely needed**: Usually not worth the complexity

## Approach 4: Cleaner Recursive

Alternative recursive with explicit list building:

```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

### Analysis

- **Time**: O(n)
- **Space**: O(n) for intermediate lists
- **Very clean**: One-liner logic
- **Less efficient**: Creates many intermediate lists

## Comparison of Approaches

| Approach                | Time | Space | Difficulty | Use Case            |
| ----------------------- | ---- | ----- | ---------- | ------------------- |
| Recursive (Implemented) | O(n) | O(h)  | Easy       | Default, interviews |
| Iterative Stack         | O(n) | O(h)  | Easy       | Satisfies follow-up |
| Morris                  | O(n) | O(1)  | Very Hard  | Space-critical      |
| Cleaner Recursive       | O(n) | O(n)  | Easy       | Quick prototyping   |

**Winner**: Recursive for simplicity, Iterative Stack for follow-up

## Traversal Types Comparison

```
Tree:      1
          / \
         2   3
        / \
       4   5

Preorder (Root → Left → Right):   [1, 2, 4, 5, 3]
Inorder (Left → Root → Right):    [4, 2, 5, 1, 3]
Postorder (Left → Right → Root):  [4, 5, 2, 3, 1]
```

**Mnemonic**:

- **Pre**order: Process **before** recursion
- **In**order: Process **in between** recursions
- **Post**order: Process **after** recursion

## Edge Cases & Considerations

1. **Empty tree**:

   - `root = None` → `[]`
   - Base case handled

2. **Single node**:

   - `root = TreeNode(1)` → `[1]`
   - No recursion needed

3. **Left-skewed tree**:

   ```
   1
   |
   2
   |
   3
   ```

   - Result: `[1, 2, 3]`
   - Maximum recursion depth

4. **Right-skewed tree**:

   ```
   1
    \
     2
      \
       3
   ```

   - Result: `[1, 2, 3]`
   - Maximum recursion depth

5. **Complete binary tree**:

   ```
       1
      / \
     2   3
    / \
   4   5
   ```

   - Result: `[1, 2, 4, 5, 3]`
   - Balanced recursion

6. **Subtree with one child**:
   ```
     1
      \
       2
      /
     3
   ```
   - Result: `[1, 2, 3]`
   - Mixed left/right traversal

## Common Pitfalls

1. **Wrong traversal order**:

   ```python
   # WRONG: This is inorder, not preorder
   def dfs(node):
       dfs(node.left)
       res.append(node.val)  # Process in middle
       dfs(node.right)

   # CORRECT: Process before recursion
   def dfs(node):
       res.append(node.val)  # Process first
       dfs(node.left)
       dfs(node.right)
   ```

2. **Wrong stack order in iterative**:

   ```python
   # WRONG: Left is processed last
   if node.left:
       stack.append(node.left)
   if node.right:
       stack.append(node.right)

   # CORRECT: Push right first (so left pops first)
   if node.right:
       stack.append(node.right)
   if node.left:
       stack.append(node.left)
   ```

3. **Not handling None nodes**:

   ```python
   # WRONG: Will crash on None
   def dfs(node):
       res.append(node.val)  # Error if node is None
       dfs(node.left)
       dfs(node.right)

   # CORRECT: Check for None first
   def dfs(node):
       if not node:
           return
       res.append(node.val)
       dfs(node.left)
       dfs(node.right)
   ```

4. **Forgetting to return result**:

   ```python
   # WRONG: Doesn't return anything
   def preorderTraversal(self, root):
       res = []
       # ... traversal logic
       # Missing: return res

   # CORRECT: Return the result
   return res
   ```

5. **List concatenation inefficiency**:

   ```python
   # INEFFICIENT: Creates many intermediate lists
   return [root.val] + traverse(left) + traverse(right)

   # BETTER: Append to single list
   res = []
   res.append(root.val)
   # ... continue appending
   ```

## Optimization Notes

The recursive approach is **simple and efficient**:

- **Time**: O(n) - Optimal, must visit all nodes
- **Space**: O(h) - Best we can do with recursion

For **iterative** optimization:

- Explicit stack: O(h) space - Same as recursion
- Morris: O(1) space - Complex, rarely needed

**When to use each**:

- **Interviews**: Recursive (unless asked for iterative)
- **Follow-up**: Iterative with stack
- **Production**: Recursive (simpler, less bugs)
- **Space-critical**: Morris (rare)

**Why preorder is useful**:

- **Tree copying**: Create nodes in preorder
- **Serialization**: Serialize tree structure
- **Expression trees**: Prefix notation
- **Top-down processing**: Process parent before children

## Visual Example

```
Tree:        1
            / \
           2   3
          / \
         4   5

Preorder traversal: Root → Left → Right

Step-by-step execution:

  Start at 1
  ├─ Process 1 → [1]
  ├─ Go left to 2
  │  ├─ Process 2 → [1, 2]
  │  ├─ Go left to 4
  │  │  ├─ Process 4 → [1, 2, 4]
  │  │  ├─ No left
  │  │  └─ No right
  │  ├─ Go right to 5
  │  │  ├─ Process 5 → [1, 2, 4, 5]
  │  │  ├─ No left
  │  │  └─ No right
  ├─ Go right to 3
  │  ├─ Process 3 → [1, 2, 4, 5, 3]
  │  ├─ No left
  │  └─ No right

Final result: [1, 2, 4, 5, 3] ✓
```

## Test Cases

```python
# Basic tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
preorderTraversal(root)            # [1, 2, 3]

# Empty tree
preorderTraversal(None)            # []

# Single node
preorderTraversal(TreeNode(1))     # [1]

# Balanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
preorderTraversal(root)            # [1, 2, 3]

# Left-skewed
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
preorderTraversal(root)            # [1, 2, 3]

# Right-skewed
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
preorderTraversal(root)            # [1, 2, 3]

# Complete tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
preorderTraversal(root)            # [1, 2, 4, 5, 3]
```

## Thought Process

**Problem analysis**:

- Need preorder traversal: Root → Left → Right
- Must visit all nodes in specific order
- Can use recursion or iteration

**Key observations**:

1. Preorder processes node **before** its children
2. Natural fit for recursive approach
3. DFS pattern: process, then explore

**Approach considerations**:

**Recursive approach** (implemented):

- Most natural and intuitive
- DFS with preorder: process node, visit left, visit right
- Base case: None node returns immediately
- Clean and simple: O(n) time, O(h) space

**Iterative approach**:

- Use explicit stack instead of call stack
- Push right child first (so left is processed first)
- Same time/space complexity as recursive
- Satisfies follow-up requirement

**Why preorder is useful**:

- **Tree copying**: Need to create parent before children
- **Tree serialization**: Store structure naturally
- **DFS search**: Process node as soon as you see it
- **Prefix expression**: Operator comes before operands

**Comparison with other traversals**:

- **Preorder**: Root first, good for copying/serialization
- **Inorder**: For BST, gives sorted order
- **Postorder**: Children first, good for deletion

This is a fundamental tree traversal pattern with straightforward implementation!

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
- [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)
