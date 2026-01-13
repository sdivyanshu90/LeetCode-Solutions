# Implement Queue using Stacks

## Problem Summary

- Implement a queue (FIFO - First In First Out) using only two stacks (LIFO - Last In First Out).
- Support the following operations:
  - `push(x)`: Add element x to the back of the queue.
  - `pop()`: Remove and return the front element of the queue.
  - `peek()`: Return the front element without removing it.
  - `empty()`: Return whether the queue is empty.

Approach (expensive push method)

- Use two stacks: `s1` (main stack) and `s2` (helper stack).
- **Push operation** (O(n)):
  1. Move all elements from s1 to s2 (reverse the order).
  2. Push the new element onto the now-empty s1.
  3. Move all elements back from s2 to s1 (restore order with new element at bottom).
- **Pop operation** (O(1)): Simply pop from s1 (top of s1 is the front of the queue).
- **Peek operation** (O(1)): Return the top element of s1 (`s1[-1]`).
- **Empty operation** (O(1)): Check if s1 is empty.

Why this works (thought process)

- Stacks are LIFO, queues are FIFO — opposite ordering.
- By transferring elements twice during push, we maintain queue order in s1:
  - The first element pushed is at the bottom of s1 (top when popped).
  - The most recent element pushed is at the top of s1 (last to be popped).
- This ensures pop() always removes the oldest element (FIFO behavior).

Time complexity

- `push(x)`: O(n) — transfer n elements to s2, push new element, transfer n elements back to s1.
- `pop()`: O(1) — single pop from s1.
- `peek()`: O(1) — access top of s1.
- `empty()`: O(1) — check if s1 is empty.

Space complexity

- O(n) for storing n elements across both stacks.
- At any moment, elements are either in s1 or s2, never duplicated.

Alternative approach (expensive pop / amortized O(1))

**Lazy transfer approach (recommended for better amortized performance):**

```python
class MyQueue:
    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        self.s1.append(x)  # O(1) - just push to s1

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.s2.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _transfer_if_needed(self):
        if not self.s2:  # Only transfer when s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
```

- `push(x)`: O(1) — simply append to s1.
- `pop()`: Amortized O(1) — each element is moved at most once from s1 to s2.
- `peek()`: Amortized O(1) — same as pop.
- Space: O(n).

Comparison of approaches
| Operation | Expensive Push (current) | Expensive Pop (lazy) |
|-----------|-------------------------|---------------------|
| push() | O(n) | O(1) |
| pop() | O(1) | Amortized O(1) |
| peek() | O(1) | Amortized O(1) |
| empty() | O(1) | O(1) |

- **Expensive push**: Simple to understand, but push is slow.
- **Expensive pop**: More efficient in practice; push is fast, pop/peek are amortized constant time.

Edge cases

- Empty queue → `empty()` returns True.
- Single element → push, then pop returns that element.
- Multiple pushes followed by multiple pops → FIFO order maintained.
- Interleaved push and pop operations → works correctly.
- Peek without pop → non-destructive, returns front element.

Example testcases (from repository)

- Initialize queue → empty() returns True
- Push 10 → empty() returns False, peek() returns 10
- Push 20 → peek() returns 10 (first in)
- Pop → returns 10, peek() returns 20
- Pop → returns 20, empty() returns True
- Push 1, 2, 3 → pop returns 1, 2, 3 in order (FIFO verified)

Step-by-step example (expensive push)

- Initial: s1 = [], s2 = []
- Push 1:
  - Transfer s1 to s2: s1 = [], s2 = []
  - Push 1 to s1: s1 = [1], s2 = []
  - Transfer s2 to s1: s1 = [1], s2 = []
- Push 2:
  - Transfer s1 to s2: s1 = [], s2 = [1]
  - Push 2 to s1: s1 = [2], s2 = [1]
  - Transfer s2 to s1: s1 = [2, 1], s2 = []
- Push 3:
  - Transfer s1 to s2: s1 = [], s2 = [1, 2]
  - Push 3 to s1: s1 = [3], s2 = [1, 2]
  - Transfer s2 to s1: s1 = [3, 2, 1], s2 = []
- Pop: s1.pop() → 1 (correct FIFO)
- Pop: s1.pop() → 2
- Pop: s1.pop() → 3

Thought process / design choices

- The current implementation uses expensive push for simplicity and clarity.
- The lazy transfer approach is more efficient for real-world use (fewer element movements).
- Both approaches correctly implement queue semantics using only stack operations.

Common pitfalls

- Forgetting to transfer elements back to s1 after push → incorrect ordering.
- Using only one stack → cannot maintain FIFO order.
- Not checking for empty stacks before pop/peek → index errors.
- In lazy approach, forgetting to transfer before peek/pop → returns wrong element.

Applications and use cases

- Understanding data structure conversions and trade-offs.
- Interview problem testing understanding of stacks and queues.
- Demonstrating amortized analysis (lazy transfer approach).

Notes

- This problem teaches the relationship between stacks and queues.
- The expensive pop (lazy transfer) approach is generally preferred for performance.
- Both implementations are correct; choice depends on operation frequency (more pushes vs. more pops).
- Python lists implement both stack (append/pop) and queue operations natively, but this problem constrains to stack operations only.

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

```python
class MyQueue:
    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        self.s1.append(x)  # O(1) - just push to s1

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.s2.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _transfer_if_needed(self):
        if not self.s2:  # Only transfer when s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
```

### How It Works

Problem summary

- Implement a queue (FIFO - First In First Out) using only two stacks (LIFO - Last In First Out).
- Support the following operations:
  - `push(x)`: Add element x to the back of the queue.
  - `pop()`: Remove and return the front element of the queue.
  - `peek()`: Return the front element without removing it.
  - `empty()`: Return whether the queue is empty.

Approach (expensive push method)

- Use two stacks: `s1` (main stack) and `s2` (helper stack).
- **Push operation** (O(n)):
  1. Move all elements from s1 to s2 (reverse the order).
  2. Push the new element onto the now-empty s1.
  3. Move all elements back from s2 to s1 (restore order with new element at bottom).
- **Pop operation** (O(1)): Simply pop from s1 (top of s1 is the front of the queue).
- **Peek operation** (O(1)): Return the top element of s1 (`s1[-1]`).
- **Empty operation** (O(1)): Check if s1 is empty.

Why this works (thought process)

- Stacks are LIFO, queues are FIFO — opposite ordering.
- By transferring elements twice during push, we maintain queue order in s1:
  - The first element pushed is at the bottom of s1 (top when popped).
  - The most recent element pushed is at the top of s1 (last to be popped).
- This ensures pop() always removes the oldest element (FIFO behavior).

Time complexity

- `push(x)`: O(n) — transfer n elements to s2, push new element, transfer n elements back to s1.
- `pop()`: O(1) — single pop from s1.
- `peek()`: O(1) — access top of s1.
- `empty()`: O(1) — check if s1 is empty.

Space complexity

- O(n) for storing n elements across both stacks.
- At any moment, elements are either in s1 or s2, never duplicated.

Alternative approach (expensive pop / amortized O(1))

**Lazy transfer approach (recommended for better amortized performance):**

```python
class MyQueue:
    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        self.s1.append(x)  # O(1) - just push to s1

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.s2.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _transfer_if_needed(self):
        if not self.s2:  # Only transfer when s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
```

- `push(x)`: O(1) — simply append to s1.
- `pop()`: Amortized O(1) — each element is moved at most once from s1 to s2.
- `peek()`: Amortized O(1) — same as pop.
- Space: O(n).

Comparison of approaches
| Operation | Expensive Push (current) | Expensive Pop (lazy) |
|-----------|-------------------------|---------------------|
| push() | O(n) | O(1) |
| pop() | O(1) | Amortized O(1) |
| peek() | O(1) | Amortized O(1) |
| empty() | O(1) | O(1) |

- **Expensive push**: Simple to understand, but push is slow.
- **Expensive pop**: More efficient in practice; push is fast, pop/peek are amortized constant time.

Edge cases

- Empty queue → `empty()` returns True.
- Single element → push, then pop returns that element.
- Multiple pushes followed by multiple pops → FIFO order maintained.
- Interleaved push and pop operations → works correctly.
- Peek without pop → non-destructive, returns front element.

Example testcases (from repository)

- Initialize queue → empty() returns True
- Push 10 → empty() returns False, peek() returns 10
- Push 20 → peek() returns 10 (first in)
- Pop → returns 10, peek() returns 20
- Pop → returns 20, empty() returns True
- Push 1, 2, 3 → pop returns 1, 2, 3 in order (FIFO verified)

Step-by-step example (expensive push)

- Initial: s1 = [], s2 = []
- Push 1:
  - Transfer s1 to s2: s1 = [], s2 = []
  - Push 1 to s1: s1 = [1], s2 = []
  - Transfer s2 to s1: s1 = [1], s2 = []
- Push 2:
  - Transfer s1 to s2: s1 = [], s2 = [1]
  - Push 2 to s1: s1 = [2], s2 = [1]
  - Transfer s2 to s1: s1 = [2, 1], s2 = []
- Push 3:
  - Transfer s1 to s2: s1 = [], s2 = [1, 2]
  - Push 3 to s1: s1 = [3], s2 = [1, 2]
  - Transfer s2 to s1: s1 = [3, 2, 1], s2 = []
- Pop: s1.pop() → 1 (correct FIFO)
- Pop: s1.pop() → 2
- Pop: s1.pop() → 3

Thought process / design choices

- The current implementation uses expensive push for simplicity and clarity.
- The lazy transfer approach is more efficient for real-world use (fewer element movements).
- Both approaches correctly implement queue semantics using only stack operations.

Common pitfalls

- Forgetting to transfer elements back to s1 after push → incorrect ordering.
- Using only one stack → cannot maintain FIFO order.
- Not checking for empty stacks before pop/peek → index errors.
- In lazy approach, forgetting to transfer before peek/pop → returns wrong element.

Applications and use cases

- Understanding data structure conversions and trade-offs.
- Interview problem testing understanding of stacks and queues.
- Demonstrating amortized analysis (lazy transfer approach).

Notes

- This problem teaches the relationship between stacks and queues.
- The expensive pop (lazy transfer) approach is generally preferred for performance.
- Both implementations are correct; choice depends on operation frequency (more pushes vs. more pops).
- Python lists implement both stack (append/pop) and queue operations natively, but this problem constrains to stack operations only.

### Why Stack Works

- Stacks are LIFO, queues are FIFO — opposite ordering.
- By transferring elements twice during push, we maintain queue order in s1:
  - The first element pushed is at the bottom of s1 (top when popped).
  - The most recent element pushed is at the top of s1 (last to be popped).
- This ensures pop() always removes the oldest element (FIFO behavior).

Time complexity

- `push(x)`: O(n) — transfer n elements to s2, push new element, transfer n elements back to s1.
- `pop()`: O(1) — single pop from s1.
- `peek()`: O(1) — access top of s1.
- `empty()`: O(1) — check if s1 is empty.

Space complexity

- O(n) for storing n elements across both stacks.
- At any moment, elements are either in s1 or s2, never duplicated.

Alternative approach (expensive pop / amortized O(1))

**Lazy transfer approach (recommended for better amortized performance):**

```python
class MyQueue:
    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        self.s1.append(x)  # O(1) - just push to s1

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.s2.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _transfer_if_needed(self):
        if not self.s2:  # Only transfer when s2 is empty
            while self.s1:
                self.s2.append(self.s1.pop())
```

- `push(x)`: O(1) — simply append to s1.
- `pop()`: Amortized O(1) — each element is moved at most once from s1 to s2.
- `peek()`: Amortized O(1) — same as pop.
- Space: O(n).

Comparison of approaches
| Operation | Expensive Push (current) | Expensive Pop (lazy) |
|-----------|-------------------------|---------------------|
| push() | O(n) | O(1) |
| pop() | O(1) | Amortized O(1) |
| peek() | O(1) | Amortized O(1) |
| empty() | O(1) | O(1) |

- **Expensive push**: Simple to understand, but push is slow.
- **Expensive pop**: More efficient in practice; push is fast, pop/peek are amortized constant time.

Edge cases

- Empty queue → `empty()` returns True.
- Single element → push, then pop returns that element.
- Multiple pushes followed by multiple pops → FIFO order maintained.
- Interleaved push and pop operations → works correctly.
- Peek without pop → non-destructive, returns front element.

Example testcases (from repository)

- Initialize queue → empty() returns True
- Push 10 → empty() returns False, peek() returns 10
- Push 20 → peek() returns 10 (first in)
- Pop → returns 10, peek() returns 20
- Pop → returns 20, empty() returns True
- Push 1, 2, 3 → pop returns 1, 2, 3 in order (FIFO verified)

Step-by-step example (expensive push)

- Initial: s1 = [], s2 = []
- Push 1:
  - Transfer s1 to s2: s1 = [], s2 = []
  - Push 1 to s1: s1 = [1], s2 = []
  - Transfer s2 to s1: s1 = [1], s2 = []
- Push 2:
  - Transfer s1 to s2: s1 = [], s2 = [1]
  - Push 2 to s1: s1 = [2], s2 = [1]
  - Transfer s2 to s1: s1 = [2, 1], s2 = []
- Push 3:
  - Transfer s1 to s2: s1 = [], s2 = [1, 2]
  - Push 3 to s1: s1 = [3], s2 = [1, 2]
  - Transfer s2 to s1: s1 = [3, 2, 1], s2 = []
- Pop: s1.pop() → 1 (correct FIFO)
- Pop: s1.pop() → 2
- Pop: s1.pop() → 3

Thought process / design choices

- The current implementation uses expensive push for simplicity and clarity.
- The lazy transfer approach is more efficient for real-world use (fewer element movements).
- Both approaches correctly implement queue semantics using only stack operations.

Common pitfalls

- Forgetting to transfer elements back to s1 after push → incorrect ordering.
- Using only one stack → cannot maintain FIFO order.
- Not checking for empty stacks before pop/peek → index errors.
- In lazy approach, forgetting to transfer before peek/pop → returns wrong element.

Applications and use cases

- Understanding data structure conversions and trade-offs.
- Interview problem testing understanding of stacks and queues.
- Demonstrating amortized analysis (lazy transfer approach).

Notes

- This problem teaches the relationship between stacks and queues.
- The expensive pop (lazy transfer) approach is generally preferred for performance.
- Both implementations are correct; choice depends on operation frequency (more pushes vs. more pops).
- Python lists implement both stack (append/pop) and queue operations natively, but this problem constrains to stack operations only.

### Complexity Analysis

- **Time Complexity**: - `push(x)`: O(n) — transfer n elements to s2, push new element, transfer n elements back to s1. - `pop()`: O(1) — single pop from s1. - `peek()`: O(1) — access top of s1. - `empty()`: O(1) — check if s1 is empty. Space complexity - O(n) for storing n elements across both stacks. - At any moment, elements are either in s1 or s2, never duplicated. Alternative approach (expensive pop / amortized O(1)) **Lazy transfer approach (recommended for better amortized performance):** ```python class MyQueue:     def __init__(self):         self.s1 = []  # Input stack         self.s2 = []  # Output stack     def push(self, x: int) -> None:         self.s1.append(x)  # O(1) - just push to s1     def pop(self) -> int:         self._transfer_if_needed()         return self.s2.pop()     def peek(self) -> int:         self._transfer_if_needed()         return self.s2[-1]     def empty(self) -> bool:         return not self.s1 and not self.s2     def _transfer_if_needed(self):         if not self.s2:  # Only transfer when s2 is empty             while self.s1:                 self.s2.append(self.s1.pop()) ``` - `push(x)`: O(1) — simply append to s1. - `pop()`: Amortized O(1) — each element is moved at most once from s1 to s2. - `peek()`: Amortized O(1) — same as pop. - Space: O(n). Comparison of approaches | Operation | Expensive Push (current) | Expensive Pop (lazy) | |-----------|-------------------------|---------------------| | push() | O(n) | O(1) | | pop() | O(1) | Amortized O(1) | | peek() | O(1) | Amortized O(1) | | empty() | O(1) | O(1) | - **Expensive push**: Simple to understand, but push is slow. - **Expensive pop**: More efficient in practice; push is fast, pop/peek are amortized constant time. Edge cases - Empty queue → `empty()` returns True. - Single element → push, then pop returns that element. - Multiple pushes followed by multiple pops → FIFO order maintained. - Interleaved push and pop operations → works correctly. - Peek without pop → non-destructive, returns front element. Example testcases (from repository) - Initialize queue → empty() returns True - Push 10 → empty() returns False, peek() returns 10 - Push 20 → peek() returns 10 (first in) - Pop → returns 10, peek() returns 20 - Pop → returns 20, empty() returns True - Push 1, 2, 3 → pop returns 1, 2, 3 in order (FIFO verified) Step-by-step example (expensive push) - Initial: s1 = [], s2 = [] - Push 1:   - Transfer s1 to s2: s1 = [], s2 = []   - Push 1 to s1: s1 = [1], s2 = []   - Transfer s2 to s1: s1 = [1], s2 = [] - Push 2:   - Transfer s1 to s2: s1 = [], s2 = [1]   - Push 2 to s1: s1 = [2], s2 = [1]   - Transfer s2 to s1: s1 = [2, 1], s2 = [] - Push 3:   - Transfer s1 to s2: s1 = [], s2 = [1, 2]   - Push 3 to s1: s1 = [3], s2 = [1, 2]   - Transfer s2 to s1: s1 = [3, 2, 1], s2 = [] - Pop: s1.pop() → 1 (correct FIFO) - Pop: s1.pop() → 2 - Pop: s1.pop() → 3 Thought process / design choices - The current implementation uses expensive push for simplicity and clarity. - The lazy transfer approach is more efficient for real-world use (fewer element movements). - Both approaches correctly implement queue semantics using only stack operations. Common pitfalls - Forgetting to transfer elements back to s1 after push → incorrect ordering. - Using only one stack → cannot maintain FIFO order. - Not checking for empty stacks before pop/peek → index errors. - In lazy approach, forgetting to transfer before peek/pop → returns wrong element. Applications and use cases - Understanding data structure conversions and trade-offs. - Interview problem testing understanding of stacks and queues. - Demonstrating amortized analysis (lazy transfer approach). Notes - This problem teaches the relationship between stacks and queues. - The expensive pop (lazy transfer) approach is generally preferred for performance. - Both implementations are correct; choice depends on operation frequency (more pushes vs. more pops). - Python lists implement both stack (append/pop) and queue operations natively, but this problem constrains to stack operations only.
- **Space Complexity**: - O(n) for storing n elements across both stacks. - At any moment, elements are either in s1 or s2, never duplicated. Alternative approach (expensive pop / amortized O(1)) **Lazy transfer approach (recommended for better amortized performance):** ```python class MyQueue:     def __init__(self):         self.s1 = []  # Input stack         self.s2 = []  # Output stack     def push(self, x: int) -> None:         self.s1.append(x)  # O(1) - just push to s1     def pop(self) -> int:         self._transfer_if_needed()         return self.s2.pop()     def peek(self) -> int:         self._transfer_if_needed()         return self.s2[-1]     def empty(self) -> bool:         return not self.s1 and not self.s2     def _transfer_if_needed(self):         if not self.s2:  # Only transfer when s2 is empty             while self.s1:                 self.s2.append(self.s1.pop()) ``` - `push(x)`: O(1) — simply append to s1. - `pop()`: Amortized O(1) — each element is moved at most once from s1 to s2. - `peek()`: Amortized O(1) — same as pop. - Space: O(n). Comparison of approaches | Operation | Expensive Push (current) | Expensive Pop (lazy) | |-----------|-------------------------|---------------------| | push() | O(n) | O(1) | | pop() | O(1) | Amortized O(1) | | peek() | O(1) | Amortized O(1) | | empty() | O(1) | O(1) | - **Expensive push**: Simple to understand, but push is slow. - **Expensive pop**: More efficient in practice; push is fast, pop/peek are amortized constant time. Edge cases - Empty queue → `empty()` returns True. - Single element → push, then pop returns that element. - Multiple pushes followed by multiple pops → FIFO order maintained. - Interleaved push and pop operations → works correctly. - Peek without pop → non-destructive, returns front element. Example testcases (from repository) - Initialize queue → empty() returns True - Push 10 → empty() returns False, peek() returns 10 - Push 20 → peek() returns 10 (first in) - Pop → returns 10, peek() returns 20 - Pop → returns 20, empty() returns True - Push 1, 2, 3 → pop returns 1, 2, 3 in order (FIFO verified) Step-by-step example (expensive push) - Initial: s1 = [], s2 = [] - Push 1:   - Transfer s1 to s2: s1 = [], s2 = []   - Push 1 to s1: s1 = [1], s2 = []   - Transfer s2 to s1: s1 = [1], s2 = [] - Push 2:   - Transfer s1 to s2: s1 = [], s2 = [1]   - Push 2 to s1: s1 = [2], s2 = [1]   - Transfer s2 to s1: s1 = [2, 1], s2 = [] - Push 3:   - Transfer s1 to s2: s1 = [], s2 = [1, 2]   - Push 3 to s1: s1 = [3], s2 = [1, 2]   - Transfer s2 to s1: s1 = [3, 2, 1], s2 = [] - Pop: s1.pop() → 1 (correct FIFO) - Pop: s1.pop() → 2 - Pop: s1.pop() → 3 Thought process / design choices - The current implementation uses expensive push for simplicity and clarity. - The lazy transfer approach is more efficient for real-world use (fewer element movements). - Both approaches correctly implement queue semantics using only stack operations. Common pitfalls - Forgetting to transfer elements back to s1 after push → incorrect ordering. - Using only one stack → cannot maintain FIFO order. - Not checking for empty stacks before pop/peek → index errors. - In lazy approach, forgetting to transfer before peek/pop → returns wrong element. Applications and use cases - Understanding data structure conversions and trade-offs. - Interview problem testing understanding of stacks and queues. - Demonstrating amortized analysis (lazy transfer approach). Notes - This problem teaches the relationship between stacks and queues. - The expensive pop (lazy transfer) approach is generally preferred for performance. - Both implementations are correct; choice depends on operation frequency (more pushes vs. more pops). - Python lists implement both stack (append/pop) and queue operations natively, but this problem constrains to stack operations only.

### Advantages

- Efficient stack solution
- Clear and maintainable code

### Disadvantages

- May require additional space
