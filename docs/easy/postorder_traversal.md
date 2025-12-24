# Binary Tree Postorder Traversal

## Problem Summary

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

In postorder traversal, we visit nodes in this order: **Left → Right → Root**

**LeetCode Problem**: [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

**Follow-up**: Recursive solution is trivial, could you do it iteratively?

## Approach 1: Recursive DFS (Implemented)

### Strategy

The implemented solution uses a **recursive depth-first search** approach:

1. Handle base case: if node is `None`, return
2. Use a helper function `dfs` to traverse the tree
3. Visit left subtree first (recursive call)
4. Visit right subtree second (recursive call)
5. Process current node (append to result)
6. Order: **Left → Right → Root**

**Code**:

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    def dfs(node):
        if not node:
            return

        dfs(node.left)   # Visit left
        dfs(node.right)  # Visit right
        res.append(node.val)  # Process root

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

Postorder: Left → Right → Root

Execution:
  dfs(1):
    dfs(left=None): return
    dfs(right=2):
      dfs(left=3):
        dfs(left=None): return
        dfs(right=None): return
        append 3 → [3]
      dfs(right=None): return
      append 2 → [3, 2]
    append 1 → [3, 2, 1]

Result: [3, 2, 1] ✓
```

**Example 2**:

```
Tree:      1
          / \
         2   3

Postorder: Left → Right → Root

Execution:
  dfs(1):
    dfs(left=2):
      dfs(left=None): return
      dfs(right=None): return
      append 2 → [2]
    dfs(right=3):
      dfs(left=None): return
      dfs(right=None): return
      append 3 → [2, 3]
    append 1 → [2, 3, 1]

Result: [2, 3, 1] ✓
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

## Approach 2: Iterative with Two Stacks

Use two stacks to simulate postorder traversal:

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left first, then right (reversed for postorder)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Reverse to get postorder
    result = []
    while stack2:
        result.append(stack2.pop().val)

    return result
```

### How It Works

**Key insight**: Postorder is reverse of modified preorder

- Preorder: Root → Left → Right
- Modified preorder: Root → Right → Left
- Reverse of modified: Left → Right → Root (Postorder!)

**Example**:

```
Tree:    1
        / \
       2   3

stack1: [1]
stack2: []

Step 1: Pop 1 from stack1, push to stack2
  stack1: []
  stack2: [1]
  Push children to stack1: left=2, right=3
  stack1: [2, 3]

Step 2: Pop 3 from stack1, push to stack2
  stack1: [2]
  stack2: [1, 3]
  No children

Step 3: Pop 2 from stack1, push to stack2
  stack1: []
  stack2: [1, 3, 2]
  No children

Reverse stack2 by popping: [2, 3, 1] ✓
```

### Complexity

- **Time**: O(n)
- **Space**: O(n) - Two stacks

### Advantages

- **Iterative**: No recursion
- **Clever trick**: Uses reverse property

### Disadvantages

- **Two stacks**: More memory than single stack
- **Less intuitive**: Requires understanding the trick

## Approach 3: Iterative with One Stack

Efficient single-stack iterative approach:

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    stack = []
    current = root
    last_visited = None

    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Peek at top of stack
        peek = stack[-1]

        # If right child exists and hasn't been visited, go right
        if peek.right and peek.right != last_visited:
            current = peek.right
        else:
            # Visit this node
            result.append(peek.val)
            last_visited = stack.pop()

    return result
```

### How It Works

**Key idea**: Track last visited node to avoid revisiting right subtree

**Example**:

```
Tree:    1
        / \
       2   3

current=1, stack=[], last=None

Step 1: Go left to 2
  stack=[1, 2], current=None

Step 2: Peek=2, no right child
  Append 2, pop 2, last=2
  result=[2], stack=[1]

Step 3: Peek=1, has right=3, 3≠last
  current=3, go right

Step 4: Go left from 3 (none)
  stack=[1, 3], current=None

Step 5: Peek=3, no right child
  Append 3, pop 3, last=3
  result=[2, 3], stack=[1]

Step 6: Peek=1, has right=3, 3==last (visited!)
  Append 1, pop 1, last=1
  result=[2, 3, 1] ✓
```

### Complexity

- **Time**: O(n)
- **Space**: O(h) - Single stack, optimal

### Advantages

- **Optimal space**: Single stack
- **Iterative**: Satisfies follow-up
- **Most efficient**: Best space complexity

### Disadvantages

- **Complex logic**: Harder to understand
- **More code**: Longer implementation

## Approach 4: Morris Traversal

O(1) space solution using threading:

```python
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    dummy = TreeNode(0)
    dummy.left = root
    current = dummy

    while current:
        if current.left is None:
            current = current.right
        else:
            # Find predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # Create thread
                predecessor.right = current
                current = current.left
            else:
                # Remove thread and process
                predecessor.right = None
                # Reverse and add nodes from current.left to predecessor
                reverse_add_nodes(current.left, predecessor, result)
                current = current.right

    return result
```

### Complexity

- **Time**: O(n)
- **Space**: O(1) - No stack, only result array

### Notes

- **Most complex**: Hardest to implement correctly
- **Rarely needed**: Usually not worth the complexity
- **Modifies tree temporarily**: Creates temporary threads

## Comparison of Approaches

| Approach                | Time | Space | Difficulty | Use Case            |
| ----------------------- | ---- | ----- | ---------- | ------------------- |
| Recursive (Implemented) | O(n) | O(h)  | Easy       | Default, interviews |
| Two Stacks              | O(n) | O(n)  | Medium     | Learning iterative  |
| One Stack               | O(n) | O(h)  | Hard       | Optimal iterative   |
| Morris                  | O(n) | O(1)  | Very Hard  | Space-critical      |

**Winner**: Recursive for simplicity, One Stack for optimal iterative

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

   - Result: `[3, 2, 1]`
   - Maximum recursion depth

4. **Right-skewed tree**:

   ```
   1
    \
     2
      \
       3
   ```

   - Result: `[3, 2, 1]`
   - Maximum recursion depth

5. **Complete binary tree**:

   ```
       1
      / \
     2   3
    / \
   4   5
   ```

   - Result: `[4, 5, 2, 3, 1]`
   - Balanced recursion

6. **Subtree with one child**:
   ```
     1
      \
       2
      /
     3
   ```
   - Result: `[3, 2, 1]`
   - Mixed left/right traversal

## Common Pitfalls

1. **Wrong traversal order**:

   ```python
   # WRONG: This is preorder, not postorder
   def dfs(node):
       res.append(node.val)  # Process first
       dfs(node.left)
       dfs(node.right)

   # CORRECT: Process after children
   def dfs(node):
       dfs(node.left)
       dfs(node.right)
       res.append(node.val)  # Process last
   ```

2. **Not handling None nodes**:

   ```python
   # WRONG: Will crash on None
   def dfs(node):
       dfs(node.left)  # Error if node is None
       dfs(node.right)
       res.append(node.val)

   # CORRECT: Check for None first
   def dfs(node):
       if not node:
           return
       dfs(node.left)
       dfs(node.right)
       res.append(node.val)
   ```

3. **Forgetting to return result**:

   ```python
   # WRONG: Doesn't return anything
   def postorderTraversal(self, root):
       res = []
       # ... traversal logic
       # Missing: return res

   # CORRECT: Return the result
   return res
   ```

4. **Using class variable incorrectly**:

   ```python
   # RISKY: res persists across calls if not careful
   class Solution:
       res = []  # Class variable!
       def postorderTraversal(self, root):
           # res accumulates across calls

   # CORRECT: Use instance variable or local
   def postorderTraversal(self, root):
       res = []  # Local variable
       # ...
       return res
   ```

5. **Iterative stack order confusion**:

   ```python
   # WRONG: Wrong order for postorder
   if node.left:
       stack.append(node.left)
   if node.right:
       stack.append(node.right)

   # CORRECT: Right first, then left (for two-stack approach)
   # Or use more complex single-stack logic
   ```

## Optimization Notes

The recursive approach is **simple and efficient**:

- **Time**: O(n) - Optimal, must visit all nodes
- **Space**: O(h) - Best we can do with recursion

For **iterative** optimization:

- Single stack: O(h) space - Optimal
- Two stacks: O(n) space - Simpler but more space
- Morris: O(1) space - Complex, rarely worth it

**When to use each**:

- **Interviews**: Recursive (unless asked for iterative)
- **Production**: Recursive (simpler, less bugs)
- **Space-critical**: One-stack iterative or Morris
- **Learning**: Try all approaches

## Visual Example

```
Tree:        1
            / \
           2   3
          / \
         4   5

Postorder traversal: Left → Right → Root

Step-by-step execution:

  Start at 1
  ├─ Go left to 2
  │  ├─ Go left to 4
  │  │  ├─ No left
  │  │  ├─ No right
  │  │  └─ Process 4 → [4]
  │  ├─ Go right to 5
  │  │  ├─ No left
  │  │  ├─ No right
  │  │  └─ Process 5 → [4, 5]
  │  └─ Process 2 → [4, 5, 2]
  ├─ Go right to 3
  │  ├─ No left
  │  ├─ No right
  │  └─ Process 3 → [4, 5, 2, 3]
  └─ Process 1 → [4, 5, 2, 3, 1]

Final result: [4, 5, 2, 3, 1] ✓
```

## Test Cases

```python
# Basic tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
postorderTraversal(root)           # [3, 2, 1]

# Empty tree
postorderTraversal(None)           # []

# Single node
postorderTraversal(TreeNode(1))    # [1]

# Balanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
postorderTraversal(root)           # [2, 3, 1]

# Left-skewed
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
postorderTraversal(root)           # [3, 2, 1]

# Right-skewed
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
postorderTraversal(root)           # [3, 2, 1]

# Complete tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
postorderTraversal(root)           # [4, 5, 2, 3, 1]
```

## Thought Process

**Problem analysis**:

- Need postorder traversal: Left → Right → Root
- Must visit all nodes in specific order
- Can use recursion or iteration

**Key observations**:

1. Postorder processes node **after** its children
2. Natural fit for recursive approach
3. Iterative requires careful stack management

**Approach considerations**:

**Recursive approach** (implemented):

- Most natural and intuitive
- DFS with postorder: visit left, visit right, process node
- Base case: None node returns immediately
- Clean and simple: O(n) time, O(h) space

**Why postorder is useful**:

- **Deleting trees**: Delete children before parent
- **Expression evaluation**: Evaluate operands before operator
- **Dependency resolution**: Process dependencies first
- **Bottom-up processing**: Work from leaves to root

**Comparison with other traversals**:

- **Preorder**: Root first, good for copying trees
- **Inorder**: For BST, gives sorted order
- **Postorder**: Children first, good for deletion/cleanup

This is the standard tree traversal problem with straightforward recursive solution!

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
- [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
