# Delete Duplicates from Linked List

## Problem Summary

- Given the head of a sorted singly-linked list, remove duplicates such that each element appears only once.
- Return the modified linked list head. The input list is sorted in non-decreasing order.

Approach (in-place single-pass)

- Walk the list with a single pointer `curr` starting at `head`.
- For each node, if `curr.next` exists and `curr.val == curr.next.val`, skip the next node by linking `curr.next = curr.next.next`.
- Otherwise advance `curr = curr.next`.
- Continue until `curr` becomes `None`.
- This removes consecutive duplicate nodes in one pass without extra data structures.

Why this works (thought process)

- Because the list is sorted, duplicates (if any) appear in contiguous runs. Removing duplicates only requires checking adjacent nodes.
- Skipping duplicates by updating the `next` pointer preserves list order and requires no node copying.
- The algorithm preserves the first occurrence of each value (keeps the earliest node).

Time and space complexity

- Time: O(n), where n is the number of nodes — each node is visited at most once.
- Space: O(1) extra space — in-place modifications only.

Correctness and edge cases

- Empty list (`head is None`) → return `None`.
- Single-node list → unchanged.
- All nodes identical → result is a single node with that value.
- Non-adjacent duplicates cannot appear in a sorted list; sorting assumption is required.
- The implementation should carefully handle `curr` becoming `None` after skipping nodes to avoid attribute access on `None`.

Potential pitfalls / improvements

- Ensure you only advance `curr` when you did not skip a node; advancing unconditionally may skip checking newly linked nodes.
- The current implementation uses a while loop and breaks when `curr` becomes `None`. An alternative (clearer) loop structure:
  ```python
  curr = head
  while curr and curr.next:
      if curr.val == curr.next.val:
          curr.next = curr.next.next
      else:
          curr = curr.next
  return head
  ```
  This version avoids an explicit break and is idiomatic.
- If you need to remove all nodes that have duplicates (i.e., keep only values that occur exactly once), a different algorithm with a dummy head and two-pointer scanning is required.

Examples (from repository tests)

- Input: 1 -> 1 -> 2 => Output: 1 -> 2
- Input: 1 -> 1 -> 2 -> 3 -> 3 => Output: 1 -> 2 -> 3
- Input: None => Output: None

Notes

- Works in-place and is efficient for large lists.
- Keep the precondition (sorted list) in mind; behavior is undefined for unsorted input with regard to removing all duplicate values.

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
  curr = head
  while curr and curr.next:
      if curr.val == curr.next.val:
          curr.next = curr.next.next
      else:
          curr = curr.next
  return head
  ```

### How It Works

- Walk the list with a single pointer `curr` starting at `head`.
- For each node, if `curr.next` exists and `curr.val == curr.next.val`, skip the next node by linking `curr.next = curr.next.next`.
- Otherwise advance `curr = curr.next`.
- Continue until `curr` becomes `None`.
- This removes consecutive duplicate nodes in one pass without extra data structures.

Why this works (thought process)

- Because the list is sorted, duplicates (if any) appear in contiguous runs. Removing duplicates only requires checking adjacent nodes.
- Skipping duplicates by updating the `next` pointer preserves list order and requires no node copying.
- The algorithm preserves the first occurrence of each value (keeps the earliest node).

Time and space complexity

- Time: O(n), where n is the number of nodes — each node is visited at most once.
- Space: O(1) extra space — in-place modifications only.

Correctness and edge cases

- Empty list (`head is None`) → return `None`.
- Single-node list → unchanged.
- All nodes identical → result is a single node with that value.
- Non-adjacent duplicates cannot appear in a sorted list; sorting assumption is required.
- The implementation should carefully handle `curr` becoming `None` after skipping nodes to avoid attribute access on `None`.

Potential pitfalls / improvements

- Ensure you only advance `curr` when you did not skip a node; advancing unconditionally may skip checking newly linked nodes.
- The current implementation uses a while loop and breaks when `curr` becomes `None`. An alternative (clearer) loop structure:
  ```python
  curr = head
  while curr and curr.next:
      if curr.val == curr.next.val:
          curr.next = curr.next.next
      else:
          curr = curr.next
  return head
  ```
  This version avoids an explicit break and is idiomatic.
- If you need to remove all nodes that have duplicates (i.e., keep only values that occur exactly once), a different algorithm with a dummy head and two-pointer scanning is required.

Examples (from repository tests)

- Input: 1 -> 1 -> 2 => Output: 1 -> 2
- Input: 1 -> 1 -> 2 -> 3 -> 3 => Output: 1 -> 2 -> 3
- Input: None => Output: None

Notes

- Works in-place and is efficient for large lists.
- Keep the precondition (sorted list) in mind; behavior is undefined for unsorted input with regard to removing all duplicate values.

### Why Two Pointers Works

- Because the list is sorted, duplicates (if any) appear in contiguous runs. Removing duplicates only requires checking adjacent nodes.
- Skipping duplicates by updating the `next` pointer preserves list order and requires no node copying.
- The algorithm preserves the first occurrence of each value (keeps the earliest node).

Time and space complexity

- Time: O(n), where n is the number of nodes — each node is visited at most once.
- Space: O(1) extra space — in-place modifications only.

Correctness and edge cases

- Empty list (`head is None`) → return `None`.
- Single-node list → unchanged.
- All nodes identical → result is a single node with that value.
- Non-adjacent duplicates cannot appear in a sorted list; sorting assumption is required.
- The implementation should carefully handle `curr` becoming `None` after skipping nodes to avoid attribute access on `None`.

Potential pitfalls / improvements

- Ensure you only advance `curr` when you did not skip a node; advancing unconditionally may skip checking newly linked nodes.
- The current implementation uses a while loop and breaks when `curr` becomes `None`. An alternative (clearer) loop structure:
  ```python
  curr = head
  while curr and curr.next:
      if curr.val == curr.next.val:
          curr.next = curr.next.next
      else:
          curr = curr.next
  return head
  ```
  This version avoids an explicit break and is idiomatic.
- If you need to remove all nodes that have duplicates (i.e., keep only values that occur exactly once), a different algorithm with a dummy head and two-pointer scanning is required.

Examples (from repository tests)

- Input: 1 -> 1 -> 2 => Output: 1 -> 2
- Input: 1 -> 1 -> 2 -> 3 -> 3 => Output: 1 -> 2 -> 3
- Input: None => Output: None

Notes

- Works in-place and is efficient for large lists.
- Keep the precondition (sorted list) in mind; behavior is undefined for unsorted input with regard to removing all duplicate values.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n), where n is the number of nodes — each node is visited at most once. - Space: O(1) extra space — in-place modifications only. Correctness and edge cases - Empty list (`head is None`) → return `None`. - Single-node list → unchanged. - All nodes identical → result is a single node with that value. - Non-adjacent duplicates cannot appear in a sorted list; sorting assumption is required. - The implementation should carefully handle `curr` becoming `None` after skipping nodes to avoid attribute access on `None`. Potential pitfalls / improvements - Ensure you only advance `curr` when you did not skip a node; advancing unconditionally may skip checking newly linked nodes. - The current implementation uses a while loop and breaks when `curr` becomes `None`. An alternative (clearer) loop structure:   ```python   curr = head   while curr and curr.next:       if curr.val == curr.next.val:           curr.next = curr.next.next       else:           curr = curr.next   return head   ```   This version avoids an explicit break and is idiomatic. - If you need to remove all nodes that have duplicates (i.e., keep only values that occur exactly once), a different algorithm with a dummy head and two-pointer scanning is required. Examples (from repository tests) - Input: 1 -> 1 -> 2 => Output: 1 -> 2 - Input: 1 -> 1 -> 2 -> 3 -> 3 => Output: 1 -> 2 -> 3 - Input: None => Output: None Notes - Works in-place and is efficient for large lists. - Keep the precondition (sorted list) in mind; behavior is undefined for unsorted input with regard to removing all duplicate values.

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
