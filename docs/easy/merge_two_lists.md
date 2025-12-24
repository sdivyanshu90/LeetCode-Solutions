# Merge Two Sorted Lists

## Problem Summary

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

**LeetCode Problem**: [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Approach 1: Iterative with Dummy Node (Implemented)

### Strategy

The implemented solution uses an **iterative approach with a dummy node**:

1. Create a dummy node to simplify edge cases
2. Use a pointer `curr` to build the merged list
3. Compare nodes from both lists and attach the smaller one
4. Move pointers forward in the list we took from
5. After one list is exhausted, attach the remainder of the other list
6. Return `temp.next` (skip the dummy node)

**Code**:

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    curr = temp = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1, curr = list1.next, list1
        else:
            curr.next = list2
            list2, curr = list2.next, list2
    if list1 or list2:
        if list1:
            curr.next = list1
        else:
            curr.next = list2
    return temp.next
```

### How It Works

**Example**: `list1 = [1,2,4]`, `list2 = [1,3,4]`

```
Initial:
  dummy → None
  list1: 1 → 2 → 4
  list2: 1 → 3 → 4

Step 1: Compare 1 vs 1
  - 1 <= 1, attach list2's 1
  - dummy → 1
  - list2 moves to 3

Step 2: Compare 1 vs 3
  - 1 < 3, attach list1's 1
  - dummy → 1 → 1
  - list1 moves to 2

Step 3: Compare 2 vs 3
  - 2 < 3, attach list1's 2
  - dummy → 1 → 1 → 2
  - list1 moves to 4

Step 4: Compare 4 vs 3
  - 3 < 4, attach list2's 3
  - dummy → 1 → 1 → 2 → 3
  - list2 moves to 4

Step 5: Compare 4 vs 4
  - 4 <= 4, attach list2's 4
  - dummy → 1 → 1 → 2 → 3 → 4
  - list2 moves to None

Step 6: list2 is None, attach remaining list1
  - dummy → 1 → 1 → 2 → 3 → 4 → 4

Result: [1, 1, 2, 3, 4, 4]
```

### Key Techniques

**Dummy Node Pattern**:

- Simplifies edge cases (empty lists, single node)
- No need to special-case the first node
- Return `dummy.next` to skip the dummy

**Simultaneous Assignment**:

```python
list1, curr = list1.next, list1
```

This is equivalent to:

```python
temp = list1.next
curr = list1
list1 = temp
```

### Complexity Analysis

- **Time Complexity**: O(n + m) - Where n and m are lengths of the two lists
  - Visit each node exactly once
- **Space Complexity**: O(1) - Only using pointers, not creating new nodes
  - We're rearranging existing nodes, not allocating new ones

### Edge Cases Handled

- **Both empty**: `list1=None, list2=None` → `None`
- **One empty**: `list1=None, list2=[1,2]` → `[1,2]`
- **Different lengths**: Automatically handled by final attachment
- **All elements from one list first**: Works correctly
- **Duplicate values**: Attaches from list2 when equal (stable merge)

## Approach 2: Recursive

Elegant recursive solution:

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1

    # Recursive case
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
```

### How It Works

1. If one list is empty, return the other
2. Compare heads of both lists
3. Take the smaller node and recursively merge the rest
4. The smaller node becomes the head of merged result

### Visual Recursion

```
mergeTwoLists([1,2,4], [1,3,4])
  ├─ 1 < 1? No, take list2's 1
  └─ 1.next = mergeTwoLists([1,2,4], [3,4])
       ├─ 1 < 3? Yes, take list1's 1
       └─ 1.next = mergeTwoLists([2,4], [3,4])
            ├─ 2 < 3? Yes, take list1's 2
            └─ 2.next = mergeTwoLists([4], [3,4])
                 ├─ 4 < 3? No, take list2's 3
                 └─ 3.next = mergeTwoLists([4], [4])
                      ├─ 4 < 4? No, take list2's 4
                      └─ 4.next = mergeTwoLists([4], None)
                           └─ return [4]
```

### Complexity

- **Time**: O(n + m) - Each node processed once
- **Space**: O(n + m) - Recursion call stack

### When to Use

- Very clean and elegant
- Natural for recursive thinking
- Good for interviews to show recursion skills

### Drawback

- Uses O(n+m) stack space
- Risk of stack overflow for very long lists
- Iterative is more space-efficient

## Approach 3: Cleaner Iterative

Simplified version with cleaner final attachment:

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    # Attach remaining nodes (at most one list is non-empty)
    curr.next = list1 if list1 else list2

    return dummy.next
```

### Improvements

- Clearer pointer updates (no simultaneous assignment)
- Simpler final attachment: `list1 if list1 else list2`
- More readable for beginners

### Complexity

- **Time**: O(n + m)
- **Space**: O(1)

## Approach 4: In-Place Modification of list1

Modify list1 to include list2 nodes:

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1

    head = list1 if list1.val < list2.val else list2

    while list1 and list2:
        # Ensure list1.val <= list2.val
        if list1.val > list2.val:
            list1, list2 = list2, list1

        # Insert list2 nodes into list1
        while list1.next and list1.next.val <= list2.val:
            list1 = list1.next

        list1.next, list2 = list2, list1.next

    return head
```

### Complexity

- **Time**: O(n + m)
- **Space**: O(1)

### Note

- More complex logic
- Not recommended unless specifically asked for in-place modification
- Dummy node approach is cleaner

## Comparison of Approaches

| Approach                | Time   | Space  | Pros                    | Cons                                |
| ----------------------- | ------ | ------ | ----------------------- | ----------------------------------- |
| Iterative (Implemented) | O(n+m) | O(1)   | Space efficient, clear  | Simultaneous assignment may confuse |
| Recursive               | O(n+m) | O(n+m) | Elegant, concise        | Stack space, overflow risk          |
| Cleaner Iterative       | O(n+m) | O(1)   | Most readable           | None                                |
| In-Place Modification   | O(n+m) | O(1)   | Minimal pointer changes | Complex logic                       |

## Edge Cases & Considerations

1. **Both Lists Empty**:

   - `list1 = None, list2 = None` → `None`
   - Handled by returning `temp.next` which is `None`

2. **One List Empty**:

   - `list1 = None, list2 = [0]` → `[0]`
   - `list1 = [0], list2 = None` → `[0]`
   - Final attachment handles this

3. **Different Lengths**:

   - `list1 = [1,2,3,4,5], list2 = [1,2]` → `[1,1,2,2,3,4,5]`
   - Remaining nodes attached after loop

4. **All Elements Equal**:

   - `list1 = [1,1,1], list2 = [1,1,1]` → `[1,1,1,1,1,1]`
   - Stable merge (takes from list2 when equal)

5. **No Overlap**:

   - `list1 = [1,2,3], list2 = [4,5,6]` → `[1,2,3,4,5,6]`
   - First list exhausted, then second attached

6. **Complete Interleaving**:

   - `list1 = [1,3,5], list2 = [2,4,6]` → `[1,2,3,4,5,6]`
   - Alternates between lists

7. **Single Node Lists**:
   - `list1 = [1], list2 = [2]` → `[1,2]`
   - Works correctly

## Common Pitfalls

1. **Not Using Dummy Node**:

   ```python
   # WRONG: Complex edge case handling
   if not list1:
       return list2
   if not list2:
       return list1

   if list1.val < list2.val:
       head = list1
       list1 = list1.next
   else:
       head = list2
       list2 = list2.next
   # ... more complex code

   # BETTER: Use dummy node
   dummy = ListNode()
   curr = dummy
   # ... simple loop
   return dummy.next
   ```

2. **Forgetting to Return dummy.next**:

   ```python
   # WRONG: Returns dummy node
   return temp

   # CORRECT: Skip dummy node
   return temp.next
   ```

3. **Creating New Nodes Instead of Reusing**:

   ```python
   # WRONG: Wastes space, not required
   curr.next = ListNode(list1.val)

   # CORRECT: Reuse existing nodes
   curr.next = list1
   ```

4. **Not Moving curr Pointer**:

   ```python
   # WRONG: curr never moves
   while list1 and list2:
       if list1.val < list2.val:
           curr.next = list1
           list1 = list1.next
       # Missing: curr = curr.next

   # CORRECT: Move curr forward
   curr = curr.next
   ```

5. **Off-by-One in Final Attachment**:

   ```python
   # Works but verbose
   if list1 or list2:
       if list1:
           curr.next = list1
       else:
           curr.next = list2

   # Better: Direct attachment
   curr.next = list1 if list1 else list2
   # Or even simpler:
   curr.next = list1 or list2
   ```

## Optimization Notes

The iterative solution is **optimal**:

- O(n + m) time - must visit all nodes
- O(1) space - only using pointers
- In-place rearrangement of existing nodes

No further time/space optimization possible.

**Code style improvements**:

- The cleaner iterative version (Approach 3) is more readable
- Consider using it over the simultaneous assignment version

## Visual Example

```
list1: 1 → 2 → 4
list2: 1 → 3 → 4

Merge process:
dummy → ?

Step 1: 1 ≤ 1, take list2
dummy → 1₂
        ↓
list1: 1 → 2 → 4
list2: 3 → 4

Step 2: 1 < 3, take list1
dummy → 1₂ → 1₁
              ↓
list1: 2 → 4
list2: 3 → 4

Step 3: 2 < 3, take list1
dummy → 1₂ → 1₁ → 2
                  ↓
list1: 4
list2: 3 → 4

Step 4: 4 > 3, take list2
dummy → 1₂ → 1₁ → 2 → 3
                      ↓
list1: 4
list2: 4

Step 5: 4 ≤ 4, take list2
dummy → 1₂ → 1₁ → 2 → 3 → 4₂
                          ↓
list1: 4
list2: None

Step 6: Attach remaining list1
dummy → 1₂ → 1₁ → 2 → 3 → 4₂ → 4₁

Result: [1, 1, 2, 3, 4, 4]
```

## Test Cases

```python
# Basic merge
mergeTwoLists([1,2,4], [1,3,4])           # [1,1,2,3,4,4]

# Empty lists
mergeTwoLists([], [])                     # []
mergeTwoLists([], [0])                    # [0]
mergeTwoLists([0], [])                    # [0]

# Different lengths
mergeTwoLists([5,6,7], [1,2,3,4])         # [1,2,3,4,5,6,7]
mergeTwoLists([1,2], [1,2,3,4,5])         # [1,1,2,2,3,4,5]

# Interleaved
mergeTwoLists([2,4,6], [1,3,5])           # [1,2,3,4,5,6]
mergeTwoLists([1,3,5], [2,4,6])           # [1,2,3,4,5,6]

# All equal
mergeTwoLists([1,1,1], [1,1,1])           # [1,1,1,1,1,1]

# No overlap
mergeTwoLists([1,2,3], [4,5,6])           # [1,2,3,4,5,6]
mergeTwoLists([4,5,6], [1,2,3])           # [1,2,3,4,5,6]

# Single nodes
mergeTwoLists([1], [2])                   # [1,2]
mergeTwoLists([2], [1])                   # [1,2]

# One much longer
mergeTwoLists([1,3,5,7,9], [2,4,6,8,10]) # [1,2,3,4,5,6,7,8,9,10]
```

## Thought Process

The problem asks to merge two sorted linked lists into one sorted list.

**Key observations**:

1. Both input lists are already sorted
2. We need to maintain the sorted property
3. We can reuse existing nodes (don't need to create new ones)

**Approach considerations**:

**Merge strategy**:

- Similar to merge step in merge sort
- Compare heads of both lists
- Take the smaller one
- Continue until one list is exhausted
- Attach the remainder of the other list

**Implementation details**:

- **Dummy node trick**: Simplifies edge cases

  - No special handling for first node
  - No null checks for head
  - Just return `dummy.next`

- **Two pointers**:

  - `curr` builds the merged list
  - `list1` and `list2` traverse input lists

- **Final attachment**:
  - After loop, at most one list is non-empty
  - Directly attach it (all remaining nodes are already sorted and larger)

This leads to a clean O(n+m) time, O(1) space solution.

## Related Problems

- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [148. Sort List](https://leetcode.com/problems/sort-list/)
- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
