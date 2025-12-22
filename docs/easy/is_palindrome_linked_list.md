# Palindrome Linked List — Explanation, Approach, Complexity

**Problem Summary**

- Given the head of a singly linked list, determine if it is a palindrome.
- A palindrome reads the same forward and backward.
- Example: [1,2,2,1] is a palindrome; [1,2,3,4,5] is not.

**Approach (Stack-based comparison)**

- First pass: traverse the list and push all node values onto a stack.
- Second pass: traverse the list again, comparing each node value with values popped from the stack.
- If all values match (comparing front-to-back with back-to-front), it's a palindrome.
- Return `True` if `curr` becomes None (all matched), `False` otherwise.

Implementation:

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    stack = []
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next

    curr = head
    while curr and curr.val == stack.pop():
        curr = curr.next

    return curr is None
```

**Why It Works**

- A stack reverses the order of elements (LIFO - Last In First Out).
- After the first pass, the stack contains values in reverse order.
- By comparing front-to-back (list traversal) with back-to-front (stack pop), we verify palindrome property.
- The loop condition `curr and curr.val == stack.pop()` short-circuits on first mismatch.

**Complexity**

- Time: O(n) — two passes through the list (one to build stack, one to compare)
- Space: O(n) — stack stores all n node values

**Edge Cases**

- Empty list (None) → return True (vacuously a palindrome)
- Single node → return True (single element is always a palindrome)
- Two nodes identical → return True
- Two nodes different → return False
- All nodes identical → return True
- Mismatch at any position → return False

**Alternative Approaches**

**Approach 1: Reverse second half (O(1) space, optimal)**

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # Find middle using slow/fast pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare first and second halves
    left, right = head, prev
    while right:  # right is shorter or equal length
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
```

- Time: O(n), Space: O(1)
- Most optimal but more complex; modifies the list (can restore if needed)

**Approach 2: Recursion with backtracking**

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    self.front = head

    def recurse(node):
        if not node:
            return True
        if not recurse(node.next):
            return False
        if node.val != self.front.val:
            return False
        self.front = self.front.next
        return True

    return recurse(head)
```

- Time: O(n), Space: O(n) for recursion stack
- Elegant but uses implicit stack (recursion)

**Approach 3: Convert to array and check**

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]
```

- Time: O(n), Space: O(n)
- Most straightforward but uses extra space

**Thought Process / Design Choices**

- The stack approach is simple and intuitive: store all values, then compare in reverse.
- For O(1) space requirement (follow-up), use the reverse second half approach.
- The current implementation optimally stops on first mismatch via short-circuit evaluation.
- Stack-based is easier to understand than in-place reversal for beginners.

**Example Testcases (from repository)**

- [1,2,3,2,1] → True (odd-length palindrome)
- [1,2,2,1] → True (even-length palindrome)
- [1,2,3,4,5] → False (not a palindrome)
- [] → True (empty list)
- [42] → True (single node)
- [1,0] → False (two different nodes)
- [5,5] → True (two identical nodes)
- [7,7,7,7,7] → True (all identical)
- [1,2,3,2,5] → False (mismatch at end)

**Common Pitfalls**

- Not handling empty list → should return True.
- Comparing only half the list → must compare all elements.
- Off-by-one errors when finding middle → use slow/fast pointers carefully.
- Modifying list without restoring → may violate constraints if list must remain unchanged.
- Not short-circuiting on mismatch → wastes computation.

**Key Insight**

- Palindrome checking requires comparing elements symmetrically from both ends.
- For linked lists (no random access), we need either:
  - Extra space to store values for reverse comparison (stack/array)
  - In-place reversal of second half (optimal space)
  - Recursion to leverage call stack

**Follow-Up Question**

- Can you solve it in O(n) time and O(1) space? → Yes, using the reverse second half approach (Approach 1 above).
