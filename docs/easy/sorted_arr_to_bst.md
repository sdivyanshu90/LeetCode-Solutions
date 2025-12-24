# Convert Sorted Array to Binary Search Tree

## Problem Summary

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a **height-balanced binary search tree**.

A **height-balanced binary tree** is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**LeetCode Problem**: [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Approach: Recursive Middle-Pick (Implemented)

### Strategy

The implemented solution uses **recursion to pick the middle element as root**:

1. Define a recursive helper function that takes left and right bounds
2. If left > right, return None (base case)
3. Pick the middle element at index `mid = (left + right) // 2` as root
4. Recursively construct left subtree with elements from `left` to `mid - 1`
5. Recursively construct right subtree with elements from `mid + 1` to `right`
6. Return the constructed tree

**Code**:

```python
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def construct_bst(left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = construct_bst(left, mid - 1)
        root.right = construct_bst(mid + 1, right)

        return root
    return construct_bst(0, len(nums) - 1)
```

### How It Works

**Key insight**: Picking the middle element ensures balanced heights because the sorted property guarantees roughly equal distribution.

**Example 1**: `nums = [-10, -3, 0, 5, 9]`

```
Initial call: construct_bst(0, 4)

Step 1: Find middle
  left=0, right=4
  mid = (0 + 4) // 2 = 2
  nums[2] = 0 (root)

  Create root = TreeNode(0)

Step 2: Construct left subtree
  construct_bst(0, 1)
  left=0, right=1
  mid = (0 + 1) // 2 = 0
  nums[0] = -10 (left child of 0)

    Create TreeNode(-10)

    Left subtree: construct_bst(0, -1) → None
    Right subtree: construct_bst(1, 1)
      left=1, right=1
      mid = 1
      nums[1] = -3

      Create TreeNode(-3)

      Left: construct_bst(1, 0) → None
      Right: construct_bst(2, 1) → None

      Return TreeNode(-3)

    Return TreeNode(-10) with right child -3

Step 3: Construct right subtree
  construct_bst(3, 4)
  left=3, right=4
  mid = (3 + 4) // 2 = 3
  nums[3] = 5 (right child of 0)

    Create TreeNode(5)

    Left: construct_bst(3, 2) → None
    Right: construct_bst(4, 4)
      left=4, right=4
      mid = 4
      nums[4] = 9

      Create TreeNode(9)

      Left: construct_bst(4, 3) → None
      Right: construct_bst(5, 4) → None

      Return TreeNode(9)

    Return TreeNode(5) with right child 9

Final tree:
        0
       / \
     -10  5
       \   \
       -3   9

Tree structure:
Height at node 0: max(height(-10), height(5)) + 1 = max(1, 1) + 1 = 2
Height at node -10: max(height(None), height(-3)) + 1 = max(0, 0) + 1 = 1
Height at node 5: max(height(None), height(9)) + 1 = max(0, 0) + 1 = 1
Height at node -3: max(height(None), height(None)) + 1 = 0 + 1 = 0
Height at node 9: max(height(None), height(None)) + 1 = 0 + 1 = 0

✓ Height-balanced: all node depths differ by at most 1
✓ BST: left < parent < right for all nodes
```

**Example 2**: `nums = [1, 2]`

```
construct_bst(0, 1)

mid = (0 + 1) // 2 = 0
nums[0] = 1 (root)

Create TreeNode(1)

Left subtree: construct_bst(0, -1) → None
Right subtree: construct_bst(1, 1)
  left=1, right=1
  mid = 1
  nums[1] = 2

  Create TreeNode(2)

  Left: construct_bst(1, 0) → None
  Right: construct_bst(2, 1) → None

  Return TreeNode(2)

Final tree:
  1
   \
    2

✓ Height-balanced
✓ BST
```

**Example 3**: `nums = [1, 2, ..., 15]`

```
Middle element: nums[7] = 8 (0-indexed)

Construct subtree with [1, 2, 3, 4, 5, 6, 7]
  Middle: nums[3] = 4

Construct subtree with [9, 10, 11, 12, 13, 14, 15]
  Middle: nums[11] = 12

Resulting tree:
           8
         /   \
        4     12
       / \    / \
      2   6  10  14
     / \ / \ / \ / \
    1  3 5 7 9 11 13 15

✓ Perfectly balanced binary tree
```

### Why Middle Element?

**Balanced height property**:

```
Array: [1, 2, 3, 4, 5, 6, 7]

If pick middle (index 3):
  Left part: [1, 2, 3] - 3 elements
  Right part: [5, 6, 7] - 3 elements
  Balanced! ✓

If pick first element (wrong):
  Left part: [] - 0 elements
  Right part: [2, 3, 4, 5, 6, 7] - 6 elements
  Unbalanced! ✗

If pick last element (wrong):
  Left part: [1, 2, 3, 4, 5, 6] - 6 elements
  Right part: [] - 0 elements
  Unbalanced! ✗

Only middle element balances!
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - Visit each element exactly once
  - Create TreeNode for each element
  - n = length of array
- **Space Complexity**: O(log n)
  - Recursion depth = height of balanced tree
  - Height of balanced tree with n nodes = log₂(n)
  - Call stack uses O(log n) space
  - Plus O(n) for the tree nodes themselves

### Advantages

- **Guaranteed balanced**: Middle element ensures balance
- **Simple logic**: Clear recursive structure
- **In-order property**: Results in valid BST
- **Elegant**: Natural use of recursion

### Disadvantages

- **Recursion overhead**: Call stack uses extra space
- **Limited to arrays**: Doesn't work directly with linked lists

## Alternative Approach: Iterative with Queue

Use iteration instead of recursion:

```python
from collections import deque

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    # Queue stores (left, right, parent_node, is_left_child)
    root = TreeNode(nums[(0 + len(nums) - 1) // 2])
    queue = deque([(0, len(nums) - 1, root, None)])

    while queue:
        left, right, node, parent = queue.popleft()

        if left > right:
            continue

        mid = (left + right) // 2

        # Process left subtree
        if left <= mid - 1:
            left_node = TreeNode(nums[(left + mid - 1) // 2])
            node.left = left_node
            queue.append((left, mid - 1, left_node, node))

        # Process right subtree
        if mid + 1 <= right:
            right_node = TreeNode(nums[(mid + 1 + right) // 2])
            node.right = right_node
            queue.append((mid + 1, right, right_node, node))

    return root
```

### How It Works

Uses a queue to process ranges level by level instead of recursively.

**Example**: `nums = [1, 2, 3]`

```
Initial:
  root = TreeNode(2) (middle of [1,2,3])
  queue = [(0, 2, root, None)]

Iteration 1:
  left=0, right=2, node=TreeNode(2)
  mid=1

  Left child: left=0, right=0
    mid = 0
    TreeNode(1)
    node.left = TreeNode(1)
    queue.append((0, 0, TreeNode(1), root))

  Right child: left=2, right=2
    mid = 2
    TreeNode(3)
    node.right = TreeNode(3)
    queue.append((2, 2, TreeNode(3), root))

Iteration 2 (process left child):
  left=0, right=0, node=TreeNode(1)
  mid=0
  No subtrees (left > mid-1, right < mid+1)

Iteration 3 (process right child):
  left=2, right=2, node=TreeNode(3)
  mid=2
  No subtrees

Final tree:
    2
   / \
  1   3
```

### Complexity

- **Time**: O(n) - visit each element once
- **Space**: O(n) - queue can hold many nodes

### Advantages

- **No recursion**: Avoids call stack depth
- **Iterative**: More familiar to some

### Disadvantages

- **More complex**: Requires queue management
- **Higher space**: Queue stores more references
- **Less elegant**: Harder to understand

## Approach 3: Random Middle Pick (Non-optimal)

What if we pick randomly instead of middle?

```python
import random

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def construct(left, right):
        if left > right:
            return None

        # Pick random middle within range
        mid = random.randint(left, right)

        root = TreeNode(nums[mid])
        root.left = construct(left, mid - 1)
        root.right = construct(mid + 1, right)

        return root

    return construct(0, len(nums) - 1)
```

### Issues

- **Unbalanced**: Random picks don't guarantee balance
- **Variable heights**: Tree structure changes each run
- **Fails constraint**: BST may be unbalanced

## Comparison of Approaches

| Approach                            | Time | Space    | Balance        | Difficulty |
| ----------------------------------- | ---- | -------- | -------------- | ---------- |
| Middle-Pick Recursive (Implemented) | O(n) | O(log n) | Guaranteed     | Easy       |
| Iterative Queue                     | O(n) | O(n)     | Guaranteed     | Medium     |
| Random Pick                         | O(n) | O(log n) | Not guaranteed | Easy       |

**Winner**: Middle-pick recursive for simplicity and guaranteed balance

## Edge Cases & Considerations

1. **Empty array**:

   - `nums = []` → `None`
   - Base case: left > right returns None ✓

2. **Single element**:

   - `nums = [1]` → TreeNode(1)
   - mid = 0, creates single node ✓

3. **Two elements**:

   - `nums = [1, 2]` → root=1, right=2
   - Not perfectly balanced, but still height-balanced ✓

4. **Negative numbers**:

   - `nums = [-10, -3, 0, 5, 9]` → Works correctly
   - BST and balance maintained ✓

5. **Large array**:

   - `nums = [1..1000]` → log₂(1000) ≈ 10 height
   - Reasonable recursion depth ✓

6. **Even length array**:

   - `nums = [1, 2, 3, 4]` → root=2 or 3
   - Integer division picks one of two middles ✓

7. **Odd length array**:
   - `nums = [1, 2, 3, 4, 5]` → root=3
   - Clear middle element ✓

## Common Pitfalls

1. **Using wrong middle formula**:

   ```python
   # WRONG: Arithmetic mean (works here but confusing)
   mid = (left + right) // 2

   # This is actually correct for indices
   # But for clarity could show alternatives

   # CORRECT: Use (left + right) // 2
   mid = (left + right) // 2
   ```

2. **Off-by-one in recursive bounds**:

   ```python
   # WRONG: Incorrect bounds
   root.left = construct_bst(left, mid)  # Includes mid!
   root.right = construct_bst(mid, right)  # Includes mid!

   # CORRECT: Exclude mid
   root.left = construct_bst(left, mid - 1)
   root.right = construct_bst(mid + 1, right)
   ```

3. **Forgetting base case**:

   ```python
   # WRONG: No base case
   def construct(left, right):
       mid = (left + right) // 2  # Infinite recursion!

   # CORRECT: Check bounds
   if left > right:
       return None
   ```

4. **Creating node before children**:

   ```python
   # This is actually fine, but could be:
   root = TreeNode(nums[mid])
   root.left = construct_bst(left, mid - 1)
   root.right = construct_bst(mid + 1, right)

   # Just make sure to assign children before return
   ```

5. **Returning None instead of handling**:

   ```python
   # WRONG: Returns None for empty
   if not nums:
       return None

   # CORRECT: Actually works fine, but base case handles it
   # Base case left > right catches it
   ```

## Optimization Notes

The implemented solution is **already optimal for this problem**:

- **Time**: O(n) - must create n nodes
- **Space**: O(log n) recursion depth (optimal for balanced tree)
- **Balance**: Always guaranteed

**Interview tips**:

- Explain why middle element guarantees balance
- Show step-by-step recursion
- Discuss time/space complexity
- Mention iterative alternative
- Note the in-order traversal gives sorted array

**Key insight for interviews**:

```
Why middle guarantees balance:

Sorted array splits naturally in half:
- Left half: smaller than middle
- Right half: larger than middle

Each recursive call splits remaining range in half:
- Height = O(log n)

For any node: depth of left subtree ≈ depth of right subtree
All heights differ by at most 1!
```

## Tree Properties Verification

For the result to be valid:

1. **BST property**: For each node, all left descendants < node < all right descendants

   - ✓ Guaranteed: sorted array, middle element splits correctly

2. **Height-balanced property**: Depth difference between subtrees ≤ 1

   - ✓ Guaranteed: middle element creates even split

3. **Structure**: Binary tree with n nodes
   - ✓ Guaranteed: each element becomes a node

## Visual Example

```
Array: [-10, -3, 0, 5, 9]

Building process:

Step 1: Find middle
  Array: [-10, -3, 0, 5, 9]
         0   1  2  3  4
  mid = 2, value = 0

         0
        / \
       ?   ?

Step 2: Left subtree [-10, -3]
  Array: [-10, -3]
         0    1
  mid = 0, value = -10

         0
        / \
      -10  ?
      / \
     ?   ?

  Right of -10: [-3]
  mid = 1, value = -3

         0
        / \
      -10  ?
        \
        -3

Step 3: Right subtree [5, 9]
  Array: [5, 9]
         3  4
  mid = 3, value = 5

         0
        / \
      -10  5
        \  / \
        -3 ?  ?

  Right of 5: [9]
  mid = 4, value = 9

         0
        / \
      -10  5
        \   \
        -3   9


Final balanced BST:
         0
        / \
      -10  5
        \   \
        -3   9

Height: 2 (balanced!)
```

## Test Cases

```python
# Basic cases
sortedArrayToBST([-10, -3, 0, 5, 9])        # Root=0

# Single element
sortedArrayToBST([1])                       # Root=1

# Two elements
sortedArrayToBST([1, 2])                    # Root=1 (or 2)

# Empty array
sortedArrayToBST([])                        # None

# Larger array
sortedArrayToBST(list(range(1, 16)))        # Root=8

# Negative numbers
sortedArrayToBST([-5, -2, 0, 1, 3])         # Root=0

# Large range
sortedArrayToBST([-1000, -500, 0, 500, 1000])  # Root=0

# Powers of 2
sortedArrayToBST([1, 2, 4, 8])              # Root=2

# Odd length
sortedArrayToBST([1, 2, 3, 4, 5])           # Root=3

# Even length
sortedArrayToBST([1, 2, 3, 4])              # Root=2 or 3
```

## Thought Process

**Problem analysis**:

- Convert sorted array to height-balanced BST
- Need to maintain both BST and balance properties
- Array is already sorted (key property)

**Key observations**:

1. Sorted array has natural ordering
2. Any middle element separates smaller (left) and larger (right)
3. BST property: this becomes root with left/right subtrees
4. Balance: splitting array in half creates even subtree sizes

**Algorithm insight**:

```
Recursive approach:
1. Pick middle as root (guarantees balance)
2. Recursively build left subtree (smaller elements)
3. Recursively build right subtree (larger elements)

Why this works:
- Each middle pick splits problem in half
- Subtrees also get middle picks
- Height naturally becomes log(n)
- All subtrees within 1 level of each other
```

**Why middle is crucial**:

```
If pick first: Degenerate tree (linked list-like)
  Tree height: O(n)

If pick last: Degenerate tree (linked list-like)
  Tree height: O(n)

If pick middle: Balanced tree
  Tree height: O(log n) ✓
  All nodes balanced ✓
```

**Optimal solution**:

- Time: O(n) - must create all nodes
- Space: O(log n) - recursion depth of balanced tree
- Both are optimal for this problem

**Interview strategy**:

1. Recognize sorted property
2. Explain why middle works
3. Code recursive solution
4. Walk through example
5. Analyze complexity
6. Mention iterative alternative

This problem demonstrates:

- Recursion with divide-and-conquer
- Tree construction and balance
- Binary search tree properties
- Using sorted data intelligently

## Related Problems

- [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)
- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
