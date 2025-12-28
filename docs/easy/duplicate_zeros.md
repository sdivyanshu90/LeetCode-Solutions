# Duplicate Zeros

Problem summary

- Given a fixed-length array, duplicate each zero, shifting remaining elements to the right.
- Modifications are in-place; elements beyond array length are discarded.
- Example: [1,0,2,3,0,4,5,0] -> [1,0,0,2,3,0,0,4].

Current implementation (in repository)

- Implementation creates new array then copies back:
  - Creates empty list new_arr.
  - Iterates through original array.
  - For zeros: extends with [0, 0].
  - For non-zeros: appends the value.
  - Copies first len(arr) elements back to original array.
- Example code:
  ```python
  new_arr = []
  for num in arr:
      if num == 0:
          new_arr.extend([0, 0])
      else:
          new_arr.append(num)
  for i in range(len(arr)):
      arr[i] = new_arr[i]
  ```

Why this works

- Building new array with duplicated zeros simulates the shifting behavior.
- Copying back first len(arr) elements ensures fixed-length constraint.
- Elements beyond original length are naturally discarded.
- In-place modification achieved by overwriting original array values.

Time complexity

- Let n = length of array.
- First pass building new_arr: O(n).
- Second pass copying back: O(n).
- Overall time complexity: O(n).

Space complexity

- new_arr can grow up to O(n) in worst case (all zeros doubles to 2n, but we only use first n).
- Space complexity: O(n).

Thought process and trade-offs

- Two-pass approach: simple to understand and implement.
- True in-place O(1) space solution exists: work backwards, calculate final positions, place elements from right to left. More complex but space-efficient.
- Current approach trades space for simplicity.
- For interview: this solution demonstrates understanding; mention O(1) space optimization if time permits.
- Trade-off: O(n) auxiliary space vs. code complexity.
