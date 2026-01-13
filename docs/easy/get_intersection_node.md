# Intersection of Two Linked Lists

## Problem Summary

- Given two singly-linked lists that may have an intersection point, find the node where the two lists intersect.
- If the lists do not intersect, return None.
- The intersection is defined by reference (same node object), not by value.
- Example: List A = [4, 1, 8, 4, 5], List B = [5, 0, 1, 8, 4, 5]. They intersect at node 8.

Approach (two-pointer cycling)

- Initialize two pointers: `pointerA` at headA and `pointerB` at headB.
- Traverse both lists simultaneously. When a pointer reaches the end of its list, redirect it to the head of the other list.
- Continue until both pointers meet at the same node (intersection) or both become None (no intersection).
- The key insight: if lists intersect, by redirecting pointers to swap lists, we equalize the distance traveled before meeting at the intersection node.

Why this works (mathematical insight)

- Let lenA = length of list A, lenB = length of list B, lenC = length of common suffix (intersection part).
- If there is an intersection: lenA + lenB = lenB + lenA (always true).
  - pointerA travels: (lenA - lenC) nodes in A + lenC nodes in B = lenA - lenC + lenC.
  - pointerB travels: (lenB - lenC) nodes in B + lenC nodes in A = lenB - lenC + lenC.
  - Both travel the same distance and will meet at the first intersecting node.
- If there is no intersection: both pointers will reach None simultaneously after lenA + lenB steps.

Time and space complexity

- Time: O(m + n) where m = len(list A), n = len(list B).
  - Worst case: traverse both lists fully once, then traverse the longer list's unique part and the shorter list with its head swapped.
  - Bounded by m + n steps total.
- Space: O(1) — only two pointers used; no extra data structures.

Alternative approaches

- Hash set (O(m + n) time, O(m) space):
  ```python
  seen = set()
  while headA:
      seen.add(headA)
      headA = headA.next
  while headB:
      if headB in seen:
          return headB
      headB = headB.next
  return None
  ```
- Length balancing (O(m + n) time, O(1) space):
  ```python
  def get_length(head):
      length = 0
      while head:
          length += 1
          head = head.next
      lenA, lenB = get_length(headA), get_length(headB)
      for _ in range(abs(lenA - lenB)):
          if lenA > lenB:
              headA = headA.next
          else:
              headB = headB.next
      while headA and headB:
          if headA == headB:
              return headA
          headA, headB = headA.next, headB.next
      return None
  ```
  More verbose but equally efficient.

Edge cases

- Both lists are None → return None.
- One list is None, the other is not → return None (no intersection).
- Intersection at the head (headA == headB) → return immediately on first check.
- Intersection at the end (last nodes are the same, earlier nodes differ) → found after cycling.
- No intersection (lists are completely separate) → both pointers reach None simultaneously, return None.
- Lists of very different lengths (one very long, one very short) → cycling ensures we find intersection efficiently.

Example testcases (from repository)

- Intersection at node 8: headA=[4,1] → [8,4,5], headB=[5,0,1] → [8,4,5] → output: 8
- No intersection: headA=[2,6,4], headB=[1,5] → output: None
- Intersection at node 2: headA=[1] → [2,4], headB=[3] → [2,4] → output: 2
- Intersection at head: headA=headB=[7,8,9] → output: 7
- Intersection at last node: headA=[1,2,3] → [10], headB=[4,5,6] → [10] → output: 10

Key insights

- The pointer-swapping technique ensures both pointers traverse equal distances before meeting.
- No need to compute lengths explicitly; the cycling approach handles length differences implicitly.
- The condition `pointerA != pointerB` covers both cases: when they meet at a node (intersection) and when both are None (no intersection).

Thought process / design choices

- The two-pointer cycling approach is elegant and avoids explicitly calculating list lengths.
- It's more intuitive than the set-based approach and uses O(1) space.
- The algorithm is deterministic and guaranteed to terminate in at most m + n + m + n = 2(m + n) steps.

Common pitfalls

- Comparing node values instead of node references → will incorrectly find matches even if nodes are different objects.
- Forgetting to redirect pointers when reaching the end → pointers would just become None and never meet.
- Using `if pointerA.val == pointerB.val` instead of `if pointerA == pointerB` → incorrect for nodes with the same value but different identity.

Notes

- This problem tests understanding of linked list traversal and creative problem-solving.
- The two-pointer cycling technique is a classic approach applicable to other linked list problems.
- The solution is optimal in both time (O(m + n)) and space (O(1)).

## Approach: Two Pointers (Implemented)

### Strategy

The solution uses two pointers to solve the problem efficiently.

```python
  seen = set()
  while headA:
      seen.add(headA)
      headA = headA.next
  while headB:
      if headB in seen:
          return headB
      headB = headB.next
  return None
  ```

### How It Works

Problem summary

- Given two singly-linked lists that may have an intersection point, find the node where the two lists intersect.
- If the lists do not intersect, return None.
- The intersection is defined by reference (same node object), not by value.
- Example: List A = [4, 1, 8, 4, 5], List B = [5, 0, 1, 8, 4, 5]. They intersect at node 8.

Approach (two-pointer cycling)

- Initialize two pointers: `pointerA` at headA and `pointerB` at headB.
- Traverse both lists simultaneously. When a pointer reaches the end of its list, redirect it to the head of the other list.
- Continue until both pointers meet at the same node (intersection) or both become None (no intersection).
- The key insight: if lists intersect, by redirecting pointers to swap lists, we equalize the distance traveled before meeting at the intersection node.

Why this works (mathematical insight)

- Let lenA = length of list A, lenB = length of list B, lenC = length of common suffix (intersection part).
- If there is an intersection: lenA + lenB = lenB + lenA (always true).
  - pointerA travels: (lenA - lenC) nodes in A + lenC nodes in B = lenA - lenC + lenC.
  - pointerB travels: (lenB - lenC) nodes in B + lenC nodes in A = lenB - lenC + lenC.
  - Both travel the same distance and will meet at the first intersecting node.
- If there is no intersection: both pointers will reach None simultaneously after lenA + lenB steps.

Time and space complexity

- Time: O(m + n) where m = len(list A), n = len(list B).
  - Worst case: traverse both lists fully once, then traverse the longer list's unique part and the shorter list with its head swapped.
  - Bounded by m + n steps total.
- Space: O(1) — only two pointers used; no extra data structures.

Alternative approaches

- Hash set (O(m + n) time, O(m) space):
  ```python
  seen = set()
  while headA:
      seen.add(headA)
      headA = headA.next
  while headB:
      if headB in seen:
          return headB
      headB = headB.next
  return None
  ```
- Length balancing (O(m + n) time, O(1) space):
  ```python
  def get_length(head):
      length = 0
      while head:
          length += 1
          head = head.next
      lenA, lenB = get_length(headA), get_length(headB)
      for _ in range(abs(lenA - lenB)):
          if lenA > lenB:
              headA = headA.next
          else:
              headB = headB.next
      while headA and headB:
          if headA == headB:
              return headA
          headA, headB = headA.next, headB.next
      return None
  ```
  More verbose but equally efficient.

Edge cases

- Both lists are None → return None.
- One list is None, the other is not → return None (no intersection).
- Intersection at the head (headA == headB) → return immediately on first check.
- Intersection at the end (last nodes are the same, earlier nodes differ) → found after cycling.
- No intersection (lists are completely separate) → both pointers reach None simultaneously, return None.
- Lists of very different lengths (one very long, one very short) → cycling ensures we find intersection efficiently.

Example testcases (from repository)

- Intersection at node 8: headA=[4,1] → [8,4,5], headB=[5,0,1] → [8,4,5] → output: 8
- No intersection: headA=[2,6,4], headB=[1,5] → output: None
- Intersection at node 2: headA=[1] → [2,4], headB=[3] → [2,4] → output: 2
- Intersection at head: headA=headB=[7,8,9] → output: 7
- Intersection at last node: headA=[1,2,3] → [10], headB=[4,5,6] → [10] → output: 10

Key insights

- The pointer-swapping technique ensures both pointers traverse equal distances before meeting.
- No need to compute lengths explicitly; the cycling approach handles length differences implicitly.
- The condition `pointerA != pointerB` covers both cases: when they meet at a node (intersection) and when both are None (no intersection).

Thought process / design choices

- The two-pointer cycling approach is elegant and avoids explicitly calculating list lengths.
- It's more intuitive than the set-based approach and uses O(1) space.
- The algorithm is deterministic and guaranteed to terminate in at most m + n + m + n = 2(m + n) steps.

Common pitfalls

- Comparing node values instead of node references → will incorrectly find matches even if nodes are different objects.
- Forgetting to redirect pointers when reaching the end → pointers would just become None and never meet.
- Using `if pointerA.val == pointerB.val` instead of `if pointerA == pointerB` → incorrect for nodes with the same value but different identity.

Notes

- This problem tests understanding of linked list traversal and creative problem-solving.
- The two-pointer cycling technique is a classic approach applicable to other linked list problems.
- The solution is optimal in both time (O(m + n)) and space (O(1)).

### Why Two Pointers Works

- Let lenA = length of list A, lenB = length of list B, lenC = length of common suffix (intersection part).
- If there is an intersection: lenA + lenB = lenB + lenA (always true).
  - pointerA travels: (lenA - lenC) nodes in A + lenC nodes in B = lenA - lenC + lenC.
  - pointerB travels: (lenB - lenC) nodes in B + lenC nodes in A = lenB - lenC + lenC.
  - Both travel the same distance and will meet at the first intersecting node.
- If there is no intersection: both pointers will reach None simultaneously after lenA + lenB steps.

Time and space complexity

- Time: O(m + n) where m = len(list A), n = len(list B).
  - Worst case: traverse both lists fully once, then traverse the longer list's unique part and the shorter list with its head swapped.
  - Bounded by m + n steps total.
- Space: O(1) — only two pointers used; no extra data structures.

Alternative approaches

- Hash set (O(m + n) time, O(m) space):
  ```python
  seen = set()
  while headA:
      seen.add(headA)
      headA = headA.next
  while headB:
      if headB in seen:
          return headB
      headB = headB.next
  return None
  ```
- Length balancing (O(m + n) time, O(1) space):
  ```python
  def get_length(head):
      length = 0
      while head:
          length += 1
          head = head.next
      lenA, lenB = get_length(headA), get_length(headB)
      for _ in range(abs(lenA - lenB)):
          if lenA > lenB:
              headA = headA.next
          else:
              headB = headB.next
      while headA and headB:
          if headA == headB:
              return headA
          headA, headB = headA.next, headB.next
      return None
  ```
  More verbose but equally efficient.

Edge cases

- Both lists are None → return None.
- One list is None, the other is not → return None (no intersection).
- Intersection at the head (headA == headB) → return immediately on first check.
- Intersection at the end (last nodes are the same, earlier nodes differ) → found after cycling.
- No intersection (lists are completely separate) → both pointers reach None simultaneously, return None.
- Lists of very different lengths (one very long, one very short) → cycling ensures we find intersection efficiently.

Example testcases (from repository)

- Intersection at node 8: headA=[4,1] → [8,4,5], headB=[5,0,1] → [8,4,5] → output: 8
- No intersection: headA=[2,6,4], headB=[1,5] → output: None
- Intersection at node 2: headA=[1] → [2,4], headB=[3] → [2,4] → output: 2
- Intersection at head: headA=headB=[7,8,9] → output: 7
- Intersection at last node: headA=[1,2,3] → [10], headB=[4,5,6] → [10] → output: 10

Key insights

- The pointer-swapping technique ensures both pointers traverse equal distances before meeting.
- No need to compute lengths explicitly; the cycling approach handles length differences implicitly.
- The condition `pointerA != pointerB` covers both cases: when they meet at a node (intersection) and when both are None (no intersection).

Thought process / design choices

- The two-pointer cycling approach is elegant and avoids explicitly calculating list lengths.
- It's more intuitive than the set-based approach and uses O(1) space.
- The algorithm is deterministic and guaranteed to terminate in at most m + n + m + n = 2(m + n) steps.

Common pitfalls

- Comparing node values instead of node references → will incorrectly find matches even if nodes are different objects.
- Forgetting to redirect pointers when reaching the end → pointers would just become None and never meet.
- Using `if pointerA.val == pointerB.val` instead of `if pointerA == pointerB` → incorrect for nodes with the same value but different identity.

Notes

- This problem tests understanding of linked list traversal and creative problem-solving.
- The two-pointer cycling technique is a classic approach applicable to other linked list problems.
- The solution is optimal in both time (O(m + n)) and space (O(1)).

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(m + n) where m = len(list A), n = len(list B).   - Worst case: traverse both lists fully once, then traverse the longer list's unique part and the shorter list with its head swapped.   - Bounded by m + n steps total. - Space: O(1) — only two pointers used; no extra data structures. Alternative approaches - Hash set (O(m + n) time, O(m) space):   ```python   seen = set()   while headA:       seen.add(headA)       headA = headA.next   while headB:       if headB in seen:           return headB       headB = headB.next   return None   ``` - Length balancing (O(m + n) time, O(1) space):   ```python   def get_length(head):       length = 0       while head:           length += 1           head = head.next       lenA, lenB = get_length(headA), get_length(headB)       for _ in range(abs(lenA - lenB)):           if lenA > lenB:               headA = headA.next           else:               headB = headB.next       while headA and headB:           if headA == headB:               return headA           headA, headB = headA.next, headB.next       return None   ```   More verbose but equally efficient. Edge cases - Both lists are None → return None. - One list is None, the other is not → return None (no intersection). - Intersection at the head (headA == headB) → return immediately on first check. - Intersection at the end (last nodes are the same, earlier nodes differ) → found after cycling. - No intersection (lists are completely separate) → both pointers reach None simultaneously, return None. - Lists of very different lengths (one very long, one very short) → cycling ensures we find intersection efficiently. Example testcases (from repository) - Intersection at node 8: headA=[4,1] → [8,4,5], headB=[5,0,1] → [8,4,5] → output: 8 - No intersection: headA=[2,6,4], headB=[1,5] → output: None - Intersection at node 2: headA=[1] → [2,4], headB=[3] → [2,4] → output: 2 - Intersection at head: headA=headB=[7,8,9] → output: 7 - Intersection at last node: headA=[1,2,3] → [10], headB=[4,5,6] → [10] → output: 10 Key insights - The pointer-swapping technique ensures both pointers traverse equal distances before meeting. - No need to compute lengths explicitly; the cycling approach handles length differences implicitly. - The condition `pointerA != pointerB` covers both cases: when they meet at a node (intersection) and when both are None (no intersection). Thought process / design choices - The two-pointer cycling approach is elegant and avoids explicitly calculating list lengths. - It's more intuitive than the set-based approach and uses O(1) space. - The algorithm is deterministic and guaranteed to terminate in at most m + n + m + n = 2(m + n) steps. Common pitfalls - Comparing node values instead of node references → will incorrectly find matches even if nodes are different objects. - Forgetting to redirect pointers when reaching the end → pointers would just become None and never meet. - Using `if pointerA.val == pointerB.val` instead of `if pointerA == pointerB` → incorrect for nodes with the same value but different identity. Notes - This problem tests understanding of linked list traversal and creative problem-solving. - The two-pointer cycling technique is a classic approach applicable to other linked list problems. - The solution is optimal in both time (O(m + n)) and space (O(1)).

### Advantages

- Efficient two pointers solution
- Clear and maintainable code

### Disadvantages

- May require additional space
