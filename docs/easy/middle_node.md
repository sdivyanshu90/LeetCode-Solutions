# Middle of the Linked List

Problem summary

- Given the head of a singly linked list, return the middle node.
- If two middle nodes (even length), return the second one.
- Example: [1,2,3,4,5] -> return node with value 3.

Current implementation (in repository)

- Implementation uses fast and slow pointer technique:
  - Initializes two pointers: fast and slow, both at head.
  - Moves slow one step, fast two steps per iteration.
  - When fast reaches end, slow is at middle.
  - Returns slow pointer as middle node.
- Example code:
  ```python
  fast = head
  slow = head
  while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
  return slow
  ```

Why this works

- Fast pointer moves twice as fast as slow pointer.
- When fast reaches end (or last node), slow has moved half the distance.
- For odd length: fast lands on None, slow on exact middle.
- For even length: fast lands on None, slow on second of two middles.
- Mathematical: if length n, slow moves n/2 steps, landing at position n//2 (0-indexed).

Time complexity

- Let n = number of nodes.
- Visits each node at most once (fast pointer visits all, slow half).
- Overall time complexity: O(n).

Space complexity

- Only using two pointer variables.
- Space complexity: O(1).

Thought process and trade-offs

- Two-pointer technique: classic linked list pattern.
- Single-pass solution: doesn't require counting length first.
- Alternative: count length, then traverse to middle - two passes, same O(n) complexity.
- Current approach: more elegant, one pass.
- Handles even/odd length naturally through loop condition.
