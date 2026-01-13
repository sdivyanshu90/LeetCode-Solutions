# Implement Stack Using Queues

## Problem Summary

**Problem Summary**
- Implement a stack (LIFO) using only queue operations. Supported operations:
  - push(x): add element x onto the stack
  - pop(): remove and return the top element
  - top(): return the top element without removing it
  - empty(): return whether the stack is empty

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

```python
from collections import deque

class MyStack:
		def __init__(self):
				self.q = deque()

		def push(self, x: int) -> None:
				self.q.append(x)
				# rotate so that x becomes the front (stack top)
				for _ in range(len(self.q) - 1):
						self.q.append(self.q.popleft())

		def pop(self) -> int:
				return self.q.popleft()

		def top(self) -> int:
				return self.q[0]

		def empty(self) -> bool:
				return not self.q
```

### How It Works

**Problem Summary**

- Implement a stack (LIFO) using only queue operations. Supported operations:
  - push(x): add element x onto the stack
  - pop(): remove and return the top element
  - top(): return the top element without removing it
  - empty(): return whether the stack is empty
- Constraint: you may only use queue operations (enqueue, dequeue, size, empty) — no direct stack/list indexing.

**Note on Current File**

- The repository’s `MyStack` currently uses a Python list as a stack (append/pop). That solves the stack behavior, but it does not adhere to the “use queues only” constraint. Below are two standard queue-based implementations to meet the problem requirement.

**Approach A — Single Queue (Rotate on push)**

- Idea: keep the newest element at the front of the queue so it behaves like a stack top.
- Steps:
  - push(x): enqueue x, then rotate the previous elements by dequeuing and enqueuing them back so x moves to the front.
  - pop(): dequeue from the front and return it.
  - top(): return the front element (peek).
  - empty(): check if the queue is empty.
- Complexity:
  - push: O(n) due to rotation
  - pop: O(1)
  - top: O(1)
  - space: O(n)

Example (Python, using `collections.deque`):

```python
from collections import deque

class MyStack:
		def __init__(self):
				self.q = deque()

		def push(self, x: int) -> None:
				self.q.append(x)
				# rotate so that x becomes the front (stack top)
				for _ in range(len(self.q) - 1):
						self.q.append(self.q.popleft())

		def pop(self) -> int:
				return self.q.popleft()

		def top(self) -> int:
				return self.q[0]

		def empty(self) -> bool:
				return not self.q
```

**Approach B — Two Queues (Expensive push)**

- Idea: always keep the stack order in `q1` so the front is the current stack top.
- Steps:
  - push(x): enqueue x in `q2`, move all items from `q1` to `q2`, then swap `q1` and `q2`.
  - pop(): dequeue from `q1`.
  - top(): peek front of `q1`.
  - empty(): check `q1` empty.
- Complexity:
  - push: O(n)
  - pop: O(1)
  - top: O(1)
  - space: O(n)

Example:

```python
from collections import deque

class MyStack:
		def __init__(self):
				self.q1 = deque()
				self.q2 = deque()

		def push(self, x: int) -> None:
				self.q2.append(x)
				while self.q1:
						self.q2.append(self.q1.popleft())
				# swap
				self.q1, self.q2 = self.q2, self.q1

		def pop(self) -> int:
				return self.q1.popleft()

		def top(self) -> int:
				return self.q1[0]

		def empty(self) -> bool:
				return not self.q1
```

**Thought Process**

- A stack is LIFO; a queue is FIFO. To emulate LIFO using FIFO primitives, we either: - Reorder on each push so the newest element is at the front (single-queue rotation), or - Rebuild the active queue each push so its front is the newest element (two-queue transfer).
  Both achieve correct stack semantics while only using queue operations.

**Edge Cases**

- empty(): should return True when no elements are present.
- pop()/top() on empty stack: typically raises underflow; handle with exceptions or problem-defined behavior.
- Mixed operations (push/pop/top interleaved): both approaches preserve correctness (LIFO).

**Complexity Summary**

- Either approach yields O(n) push and O(1) pop/top, with O(n) space.
- The single-queue rotation usually has slightly better constants and simpler code.

### Why Stack Works

The stack approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient stack solution
- Clear and maintainable code

### Disadvantages

- May require additional space
