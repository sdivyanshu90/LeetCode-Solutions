# Linked List Cycle — Explanation, Approach, Complexity

Problem summary

- Given the head of a singly-linked list, determine if the list has a cycle in it.
- A cycle exists if a node can be reached again by continuously following the `next` pointer.
- Return `True` if a cycle exists, otherwise `False`.

Approach (Floyd's Cycle Detection / Tortoise and Hare)

- Use two pointers: `slow` (moves one step at a time) and `fast` (moves two steps at a time).
- Both start at the head.
- While `fast` and `fast.next` are not None:
  - Move `slow` one step forward: `slow = slow.next`.
  - Move `fast` two steps forward: `fast = fast.next.next`.
  - If `slow == fast` (pointers meet), a cycle exists → return `True`.
- If `fast` reaches the end (None), no cycle exists → return `False`.

Why this works (mathematical proof)

- **No cycle case**: `fast` will eventually reach the end of the list (None) before or at the same time as `slow`.
- **Cycle case**: Once both pointers enter the cycle, they will eventually meet.
  - The distance between them decreases by 1 with each iteration (fast gains 2 steps, slow gains 1 step).
  - Since the cycle has finite length, they must eventually collide.
  - Proof: If slow is k steps behind fast in a cycle of length C, after k iterations they meet (fast "laps" slow).

Time and space complexity

- Time: O(n) where n = number of nodes.
  - No cycle: fast traverses the list once (~n/2 steps).
  - Cycle: slow enters the cycle and fast catches up in at most C iterations (C = cycle length ≤ n).
  - Overall: O(n).
- Space: O(1) — only two pointer variables used; no extra data structures.

Alternative approaches

**Approach 1: Hash set (O(n) space)**

```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
```

- Time: O(n), Space: O(n) for the set.
- Simpler but uses extra memory.

**Approach 2: Modifying the list (destructive, not recommended)**

- Mark visited nodes by changing their values or `next` pointers.
- Not acceptable if the list cannot be modified or values are meaningful.

Why Floyd's algorithm is optimal

- O(n) time is optimal (must visit nodes to detect cycle).
- O(1) space is optimal (no extra storage needed).
- Non-destructive (doesn't modify the list).
- Works for any linked list structure.

Edge cases

- Empty list (`head is None`) → return `False` (while condition fails immediately).
- Single node without cycle → return `False` (fast.next is None).
- Single node with cycle (points to itself) → return `True` (slow and fast meet at the same node).
- Two nodes with cycle → return `True`.
- Very long list without cycle → return `False` after traversing the entire list.
- Cycle at the beginning vs. middle vs. end → all detected correctly.

Example testcases (from repository)

- List [3 → 2 → 0 → -4] with -4 → 2 (cycle) → `True`
- List [1 → 2] (no cycle) → `False`
- Single node [1] (no cycle) → `False`
- Single node [1] with self-loop → `True`
- Empty list → `False`

Step-by-step example (with cycle)

- List: 1 → 2 → 3 → 4 → 2 (cycle back to node 2)
- Initial: slow = 1, fast = 1
- Iteration 1: slow = 2, fast = 3
- Iteration 2: slow = 3, fast = 2 (wrapped around)
- Iteration 3: slow = 4, fast = 4 → meet! Return `True`

Key insights

- Fast pointer moves twice as fast, so if there's a cycle, it will "lap" the slow pointer.
- The meeting point is not necessarily the start of the cycle (finding the cycle start is a follow-up problem).
- The algorithm is deterministic and always terminates.

Thought process / design choices

- Floyd's algorithm is the standard solution for cycle detection in linked lists.
- It balances simplicity, efficiency, and space usage.
- The two-pointer technique is a fundamental pattern in linked list problems.
- No need to know the list length or cycle position in advance.

Common pitfalls

- Not checking `fast.next` before accessing `fast.next.next` → causes AttributeError on None.
- Starting both pointers at different positions → may miss the cycle or complicate logic.
- Using `while fast:` instead of `while fast and fast.next:` → crashes when fast reaches a node with next = None.
- Comparing node values instead of node references (`slow.val == fast.val`) → incorrect for lists with duplicate values.

Follow-up problems

- Find the starting node of the cycle (Linked List Cycle II).
- Determine the length of the cycle.
- Remove the cycle from the list.

Applications

- Cycle detection in state machines and graphs.
- Detecting infinite loops in program execution.
- Finding duplicate elements in arrays (using the array as an implicit linked list).

Notes

- This is a classic interview problem testing understanding of linked lists and two-pointer techniques.
- Floyd's Cycle Detection algorithm is elegant and widely applicable.
- The solution is optimal in both time and space complexity.
- Also known as the "tortoise and hare" algorithm.
