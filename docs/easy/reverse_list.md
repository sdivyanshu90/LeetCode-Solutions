# Reverse Linked List

## Problem Summary

Given the head of a singly linked list, reverse the list and return the reversed list.

**LeetCode Problem**: [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**LeetCode Problem**: [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

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

### Why Two Pointers Works

The two pointers approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: optimization - Edge case handling

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
