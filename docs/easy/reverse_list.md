# Reverse Linked List

## Problem Summary

Given the head of a singly linked list, reverse the list and return the reversed list.

**LeetCode Problem**: [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Approach 1: Iterative with Simultaneous Assignment (Implemented)

### Strategy

The implemented solution uses an **iterative approach with Python's simultaneous assignment** feature:

1. Initialize `prev = None` (will become new tail)
2. Initialize `curr = head` (current node being processed)
3. While `curr` is not None:
   - Simultaneously update: `curr.next`, `prev`, `curr` using tuple unpacking
   - This reverses the pointer and advances both variables in one line
4. Return `prev` (new head of reversed list)

**Code**:

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev
```

### How It Works

**Example**: `1 -> 2 -> 3 -> 4 -> 5 -> None`

```
Initial state:
  prev = None
  curr = 1 -> 2 -> 3 -> 4 -> 5 -> None

Iteration 1:
  curr.next, prev, curr = prev, curr, curr.next
  curr.next, prev, curr = None, 1, 2

  Result: 1 -> None
          prev = 1
          curr = 2 -> 3 -> 4 -> 5 -> None

Iteration 2:
  curr.next, prev, curr = prev, curr, curr.next
  curr.next, prev, curr = 1, 2, 3

  Result: 2 -> 1 -> None
          prev = 2
          curr = 3 -> 4 -> 5 -> None

Iteration 3:
  curr.next, prev, curr = 1, 3, 4

  Result: 3 -> 2 -> 1 -> None
          prev = 3
          curr = 4 -> 5 -> None

Iteration 4:
  curr.next, prev, curr = 3, 4, 5

  Result: 4 -> 3 -> 2 -> 1 -> None
          prev = 4
          curr = 5 -> None

Iteration 5:
  curr.next, prev, curr = 4, 5, None

  Result: 5 -> 4 -> 3 -> 2 -> 1 -> None
          prev = 5
          curr = None

curr is None, exit loop
Return prev = 5

Final: 5 -> 4 -> 3 -> 2 -> 1 -> None
```

### Understanding Simultaneous Assignment

**Python's simultaneous assignment**:

```python
curr.next, prev, curr = prev, curr, curr.next
```

**What happens**:

1. Right side is evaluated **first** (creating tuple): `(prev, curr, curr.next)`
2. Then assigned to left side: `curr.next = prev`, `prev = curr`, `curr = curr.next`

**This is equivalent to**:

```python
temp = curr.next        # Save next node
curr.next = prev        # Reverse pointer
prev = curr             # Move prev forward
curr = temp             # Move curr forward
```

**Why simultaneous assignment is clever**:

- No need for explicit `temp` variable
- More concise and Pythonic
- All assignments happen "at once" conceptually

### Complexity Analysis

- **Time Complexity**: O(n)
  - Visit each node exactly once
  - n = number of nodes in list
- **Space Complexity**: O(1)
  - Only use two pointers (`prev`, `curr`)
  - No recursion stack or additional data structures
  - In-place reversal

### Advantages

- **Optimal time and space**: O(n) time, O(1) space
- **Concise**: Pythonic one-liner in loop
- **Easy to understand**: Clear pointer manipulation
- **In-place**: Doesn't create new nodes

### Disadvantages

- **Destructive**: Modifies original list structure
- **Python-specific**: Simultaneous assignment not available in all languages

## Approach 2: Iterative with Explicit Temp Variable

Standard iterative approach used in most languages:

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        temp = curr.next    # Save next node
        curr.next = prev    # Reverse the pointer
        prev = curr         # Move prev forward
        curr = temp         # Move curr forward

    return prev
```

### How It Works

**Visual step-by-step for `[1, 2, 3]`**:

```
Initial:
  None <- prev    curr -> 1 -> 2 -> 3 -> None

Step 1:
  temp = curr.next        # temp = 2
  curr.next = prev        # 1 -> None
  prev = curr             # prev = 1
  curr = temp             # curr = 2

  None <- 1    prev    curr -> 2 -> 3 -> None

Step 2:
  temp = curr.next        # temp = 3
  curr.next = prev        # 2 -> 1
  prev = curr             # prev = 2
  curr = temp             # curr = 3

  None <- 1 <- 2    prev    curr -> 3 -> None

Step 3:
  temp = curr.next        # temp = None
  curr.next = prev        # 3 -> 2
  prev = curr             # prev = 3
  curr = temp             # curr = None

  None <- 1 <- 2 <- 3    prev    curr = None

curr is None, exit loop
Return prev = 3

Final: 3 -> 2 -> 1 -> None
```

### Complexity

- **Time**: O(n) - visit each node once
- **Space**: O(1) - constant extra space

### Advantages

- **Clear logic**: Explicit steps, easier to debug
- **Universal**: Works in any programming language
- **Same efficiency**: O(n) time, O(1) space

### Disadvantages

- **More verbose**: Extra temp variable and line
- **Less Pythonic**: Doesn't use language features

## Approach 3: Recursive Solution

Use recursion to reverse the list:

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Base case: empty list or single node
    if not head or not head.next:
        return head

    # Recursively reverse the rest of the list
    new_head = self.reverseList(head.next)

    # Reverse the pointer
    head.next.next = head
    head.next = None

    return new_head
```

### How It Works

**Example**: `1 -> 2 -> 3 -> None`

```
Call stack (going down):
  reverseList(1 -> 2 -> 3 -> None)
    reverseList(2 -> 3 -> None)
      reverseList(3 -> None)
        Base case: return 3

Unwinding (going up):
  At reverseList(2 -> 3 -> None):
    new_head = 3
    head.next.next = head  →  3.next = 2
    head.next = None       →  2.next = None
    Result: 3 -> 2 -> None
    Return new_head = 3

  At reverseList(1 -> 2 -> 3 -> None):
    new_head = 3
    head.next.next = head  →  2.next = 1
    head.next = None       →  1.next = None
    Result: 3 -> 2 -> 1 -> None
    Return new_head = 3

Final: 3 -> 2 -> 1 -> None
```

**Visual recursion tree**:

```
reverseList(1 -> 2 -> 3)
  |
  └─> reverseList(2 -> 3)
        |
        └─> reverseList(3)
              |
              return 3

        After: 3 -> 2 -> None
        return 3

  After: 3 -> 2 -> 1 -> None
  return 3
```

### Complexity

- **Time**: O(n) - visit each node once
- **Space**: O(n) - recursion call stack

### Advantages

- **Elegant**: Clean recursive structure
- **Concise**: Fewer lines of code
- **Educational**: Good for understanding recursion

### Disadvantages

- **Not optimal space**: O(n) stack space
- **Stack overflow risk**: Deep recursion for large lists
- **Harder to debug**: Call stack can be confusing

## Approach 4: Stack-Based Solution

Use a stack to reverse the list:

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    # Push all nodes onto stack
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next

    # Pop from stack to create reversed list
    new_head = stack.pop()
    curr = new_head

    while stack:
        curr.next = stack.pop()
        curr = curr.next

    curr.next = None  # Set tail to None

    return new_head
```

### Complexity

- **Time**: O(n) - two passes through list
- **Space**: O(n) - stack stores all nodes

### Advantages

- **Intuitive**: Stack naturally reverses order
- **Non-destructive until rebuild**: Original structure preserved during push phase

### Disadvantages

- **Extra space**: O(n) for stack
- **Two passes**: Less efficient than single pass
- **Overkill**: Simpler solutions exist

## Comparison of Approaches

| Approach                 | Time | Space | Difficulty | Pros              | Cons                |
| ------------------------ | ---- | ----- | ---------- | ----------------- | ------------------- |
| Iterative (Simultaneous) | O(n) | O(1)  | Easy       | Pythonic, concise | Python-specific     |
| Iterative (Temp)         | O(n) | O(1)  | Easy       | Universal, clear  | More verbose        |
| Recursive                | O(n) | O(n)  | Medium     | Elegant           | Stack overflow risk |
| Stack-Based              | O(n) | O(n)  | Easy       | Intuitive         | Extra space         |

**Winner**: Iterative approaches (both variants) for optimal O(1) space

## Edge Cases & Considerations

1. **Empty list**:

   - `head = None` → Return `None`
   - Loop never executes, returns `prev = None` ✓

2. **Single node**:

   - `head = 1 -> None` → Return `1 -> None`
   - One iteration: `1.next = None`, return `1` ✓

3. **Two nodes**:

   - `1 -> 2 -> None` → `2 -> 1 -> None`
   - Two iterations correctly reverse ✓

4. **All identical values**:

   - `7 -> 7 -> 7 -> None` → `7 -> 7 -> 7 -> None`
   - Still reverses structure (though result looks same)

5. **Negative numbers**:

   - `[-1, -2, -3]` → `[-3, -2, -1]`
   - Values don't affect logic ✓

6. **Large lists**:

   - Iterative: O(1) space, handles any size
   - Recursive: O(n) stack, may overflow for very large n

7. **List with cycle** (not in problem):
   - Would cause infinite loop
   - Problem guarantees no cycles

## Common Pitfalls

1. **Forgetting to save next pointer**:

   ```python
   # WRONG: Loses reference to rest of list
   curr.next = prev
   curr = curr.next  # This is now prev, not original next!

   # CORRECT: Save next first
   temp = curr.next
   curr.next = prev
   curr = temp
   ```

2. **Not setting tail to None**:

   ```python
   # WRONG: Creates cycle
   while curr:
       temp = curr.next
       curr.next = prev
       prev = curr
       curr = temp
   # If you don't return prev, old head still points to second node

   # CORRECT: Simultaneous assignment handles this
   curr.next, prev, curr = prev, curr, curr.next
   # curr.next is set to prev, eventually making tail -> None
   ```

3. **Wrong return value**:

   ```python
   # WRONG: Returns old head (now tail)
   def reverseList(self, head):
       prev = None
       curr = head
       while curr:
           # ... reversal logic ...
       return head  # Wrong! This is now the tail

   # CORRECT: Return prev (new head)
   return prev
   ```

4. **Off-by-one errors in recursion**:

   ```python
   # WRONG: Base case doesn't handle single node
   if not head:
       return None

   # CORRECT: Handle both empty and single node
   if not head or not head.next:
       return head
   ```

5. **Modifying node values instead of pointers**:

   ```python
   # WRONG: Don't swap values, reverse pointers!
   # This would require O(n) space to store values

   # CORRECT: Reverse the .next pointers themselves
   curr.next = prev
   ```

6. **Incorrect simultaneous assignment order**:

   ```python
   # WRONG: Right side must evaluate before assignment
   curr, prev, curr.next = curr.next, curr, prev

   # CORRECT: Order matters!
   curr.next, prev, curr = prev, curr, curr.next
   ```

## Optimization Notes

The implemented solution is **already optimal**:

- **Time**: O(n) - must visit every node, cannot be faster
- **Space**: O(1) - only two pointers, cannot use less

**Interview tips**:

- Start with iterative approach (most practical)
- Mention recursive solution (shows versatility)
- Discuss trade-offs (space complexity)
- Code carefully to avoid pointer bugs

**Simultaneous assignment benefits**:

- Eliminates temp variable
- More Pythonic and concise
- Same performance as explicit version
- Reduces chance of pointer errors

**Language considerations**:

- Python, Ruby: Support simultaneous assignment
- Java, C++, Go: Need explicit temp variable
- All approaches achieve O(n) time, O(1) space iteratively

## Visual Example

```
Original: 1 -> 2 -> 3 -> 4 -> 5 -> None

Iterative reversal process:

Step 0:
  None <- prev    curr = 1 -> 2 -> 3 -> 4 -> 5 -> None

Step 1:
  None <- 1 <- prev    curr = 2 -> 3 -> 4 -> 5 -> None

Step 2:
  None <- 1 <- 2 <- prev    curr = 3 -> 4 -> 5 -> None

Step 3:
  None <- 1 <- 2 <- 3 <- prev    curr = 4 -> 5 -> None

Step 4:
  None <- 1 <- 2 <- 3 <- 4 <- prev    curr = 5 -> None

Step 5:
  None <- 1 <- 2 <- 3 <- 4 <- 5 <- prev    curr = None

Result: 5 -> 4 -> 3 -> 2 -> 1 -> None


Pointer changes at each step:
  1.next: 2 → None
  2.next: 3 → 1
  3.next: 4 → 2
  4.next: 5 → 3
  5.next: None → 4
```

## Test Cases

```python
# Standard list
reverseList([1, 2, 3, 4, 5])        # [5, 4, 3, 2, 1]

# Empty list
reverseList([])                      # []

# Single node
reverseList([42])                    # [42]

# Two nodes
reverseList([1, 99])                 # [99, 1]

# All identical
reverseList([7, 7, 7, 7])            # [7, 7, 7, 7]

# Duplicates
reverseList([1, 2, 3, 2, 1])         # [1, 2, 3, 2, 1]

# Longer list
reverseList([10, 20, 30, 40, 50])    # [50, 40, 30, 20, 10]

# With zero
reverseList([5, 0, -5])              # [-5, 0, 5]

# Palindromic (structure changes)
reverseList([1, 2, 1])               # [1, 2, 1]

# Negative numbers
reverseList([-1, -2, -3, -4])        # [-4, -3, -2, -1]
```

## Thought Process

**Problem analysis**:

- Need to reverse singly linked list
- Only have forward pointers (no backward links)
- Must handle empty list and single node

**Key observations**:

1. Singly linked means we can only traverse forward
2. Need to reverse all `.next` pointers
3. New head will be old tail
4. Old head will become new tail (point to None)

**Approach considerations**:

**Iterative approach**:

- Use two pointers: `prev` and `curr`
- Traverse list, reversing pointers as we go
- O(1) space - optimal!
- Clear, predictable flow

**Why iterative is best**:

- O(1) space (no recursion stack)
- Single pass through list
- No stack overflow risk
- Easy to implement and debug

**Recursive approach**:

- Elegant but uses O(n) stack space
- Risk of stack overflow on large lists
- Good for learning recursion
- Not optimal for this problem

**The simultaneous assignment trick**:

```python
curr.next, prev, curr = prev, curr, curr.next
```

This is Python magic that:

- Evaluates right side first (creates tuple)
- Assigns all at once (no temp needed)
- Makes code more concise
- Same efficiency as explicit version

This is a classic interview question testing understanding of:

- Pointer manipulation
- Iterative vs recursive trade-offs
- Space complexity optimization
- Edge case handling

## Related Problems

- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- [143. Reorder List](https://leetcode.com/problems/reorder-list/)
