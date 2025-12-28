# Kth Largest Element in a Stream

Problem summary

- Design a class that finds the kth largest element in a stream.
- Constructor takes k and initial array of integers.
- add(val) method adds a value to the stream and returns the kth largest element.
- Example: k=3, nums=[4,5,8,2], add(3) returns 4 (kth largest among [2,3,4,5,8]).

Current implementation (in repository)

- Implementation maintains sorted list:
  - Stores k value and maintains sorted stream list.
  - add() method uses binary search to find insertion position.
  - Inserts new value at correct position to maintain sorted order.
  - Returns kth largest element (stream[-k]).
- Example code:
  ```python
  def add(self, val: int) -> int:
      index = self.getIndex(val)
      self.stream.insert(index, val)
      return self.stream[-self.k]
  ```

Why this works

- Maintaining sorted list allows O(1) access to kth largest element.
- Binary search finds correct insertion position in O(log n).
- Inserting at position keeps list sorted.
- Negative indexing stream[-k] gives kth largest (k from end).

Time complexity

- Let n = current number of elements in stream.
- Binary search: O(log n).
- Insertion: O(n) due to array shift.
- Per add() call: O(n).
- Constructor: O(n log n) for initial sort.

Space complexity

- Storing all stream elements: O(n).
- Space complexity: O(n).

Thought process and trade-offs

- Sorted list approach: simple but not optimal for large streams.
- Alternative: use min-heap of size k - O(log k) per add, O(k) space, more efficient for large streams.
- Min-heap keeps k largest elements; heap top is kth largest.
- Current approach: easier to understand but less efficient.
- For small k or small stream size, difference is negligible.
- For production: heap-based solution is preferred.
