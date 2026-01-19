# Merge Two Sorted Lists

## Problem Summary

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

**LeetCode Problem**: [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

**LeetCode Problem**: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

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

### Why Two Pointers Works

The two pointers approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
