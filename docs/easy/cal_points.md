# Baseball Game

## Problem Summary

- Given a list of string operations representing a baseball game, calculate the sum of all scores.
- Operations: integer (record score), '+' (sum of last two), 'D' (double last score), 'C' (remove last score).
- Example: ["5","2","C","D","+"] -> 5, 2, remove 2, 10 (double 5), 15 (5+10) -> sum = 30.

Current implementation (in repository)

- Implementation uses a stack to track scores:
  - Iterates through operations list.
  - For 'C': pops last score from stack.
  - For 'D': doubles the last score and pushes result.
  - For '+': sums last two scores and pushes result.
  - For integers: converts to int and pushes to stack.
  - Returns sum of all values in stack.
- Example code:
  ```python
  if i == 'C':
      stack.pop()
  elif i == 'D':
      stack.append(int(stack[-1])*2)
  elif i == '+':
      stack.append(stack[-2]+stack[-1])
  ```

Why this works

- Stack maintains current valid scores, allowing easy access to most recent values.
- 'C' operation removes last score by popping.
- 'D' and '+' need last one or two scores respectively, which stack provides efficiently.
- Final sum aggregates all valid scores remaining after all operations.

Time complexity

- Let n = number of operations.
- Each operation (push, pop, access last elements) is O(1).
- Processing all operations: O(n).
- Final sum: O(n) for summing stack elements.
- Overall time complexity: O(n).

Space complexity

- Stack stores up to n scores in worst case (all integer operations).
- Space complexity: O(n).

Thought process and trade-offs

- Stack approach: natural fit for operations that reference recent values.
- Direct indexing (stack[-1], stack[-2]) assumes valid input (problem guarantees this).
- Alternative: maintain running sum and adjust on 'C', but requires tracking removed values for potential future '+' operations - more complex.
- Current approach is clean and straightforward.

## Approach: Stack (Implemented)

### Strategy

The solution uses stack to solve the problem efficiently.

```python
  if i == 'C':
      stack.pop()
  elif i == 'D':
      stack.append(int(stack[-1])*2)
  elif i == '+':
      stack.append(stack[-2]+stack[-1])
  ```

### How It Works

- Direct indexing (stack[-1], stack[-2]) assumes valid input (problem guarantees this).
- Alternative: maintain running sum and adjust on 'C', but requires tracking removed values for potential future '+' operations - more complex.
- Current approach is clean and straightforward.

### Why Stack Works

- Stack maintains current valid scores, allowing easy access to most recent values.
- 'C' operation removes last score by popping.
- 'D' and '+' need last one or two scores respectively, which stack provides efficiently.
- Final sum aggregates all valid scores remaining after all operations.

Time complexity

- Let n = number of operations.
- Each operation (push, pop, access last elements) is O(1).
- Processing all operations: O(n).
- Final sum: O(n) for summing stack elements.
- Overall time complexity: O(n).

Space complexity

- Stack stores up to n scores in worst case (all integer operations).
- Space complexity: O(n).

Thought process and trade-offs

- Stack approach: natural fit for operations that reference recent values.
- Direct indexing (stack[-1], stack[-2]) assumes valid input (problem guarantees this).
- Alternative: maintain running sum and adjust on 'C', but requires tracking removed values for potential future '+' operations - more complex.
- Current approach is clean and straightforward.

### Complexity Analysis

- **Time Complexity**: - Let n = number of operations. - Each operation (push, pop, access last elements) is O(1). - Processing all operations: O(n). - Final sum: O(n) for summing stack elements. - Overall time complexity: O(n). Space complexity - Stack stores up to n scores in worst case (all integer operations). - Space complexity: O(n). Thought process and trade-offs - Stack approach: natural fit for operations that reference recent values. - Direct indexing (stack[-1], stack[-2]) assumes valid input (problem guarantees this). - Alternative: maintain running sum and adjust on 'C', but requires tracking removed values for potential future '+' operations - more complex. - Current approach is clean and straightforward.
- **Space Complexity**: - Stack stores up to n scores in worst case (all integer operations). - Space complexity: O(n). Thought process and trade-offs - Stack approach: natural fit for operations that reference recent values. - Direct indexing (stack[-1], stack[-2]) assumes valid input (problem guarantees this). - Alternative: maintain running sum and adjust on 'C', but requires tracking removed values for potential future '+' operations - more complex. - Current approach is clean and straightforward.

### Advantages

- Efficient stack solution
- Clear and maintainable code

### Disadvantages

- May require additional space
