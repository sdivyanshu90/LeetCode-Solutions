# Last Stone Weight

Problem summary

- Given array of stone weights, repeatedly smash the two heaviest stones together.
- If weights equal, both destroyed. If different, new stone has weight = difference.
- Return weight of last remaining stone, or 0 if none remain.
- Example: [2,7,4,1,8,1] -> smash 8 and 7 (leave 1), continue... -> return 1.

Current implementation (in repository)

- Implementation uses max heap:
  - Converts weights to negative values (Python heapq is min-heap, negation makes it max-heap).
  - Heapifies the array.
  - While more than one stone: pop two heaviest, compare, push difference if not equal.
  - Returns last stone weight (negated back to positive), or 0 if empty.
- Example code:
  ```python
  stones = [-stone for stone in stones]
  heapq.heapify(stones)
  while len(stones) > 1:
      first = heapq.heappop(stones)
      second = heapq.heappop(stones)
      if first != second:
          heapq.heappush(stones, first - second)
  return -stones[0] if stones else 0
  ```

Why this works

- Max heap provides efficient access to heaviest stones.
- Negation trick: -x converts max-heap problem to min-heap problem for Python's heapq.
- Repeatedly removing and potentially adding stones simulates the smashing process.
- Stopping when <= 1 stone remains gives final answer.

Time complexity

- Let n = number of stones.
- Heapify: O(n).
- Each iteration: 2 pops + potential push = O(log n) each.
- Number of iterations: O(n) worst case (one stone removed per iteration).
- Overall time complexity: O(n log n).

Space complexity

- Heap array: O(n).
- Space complexity: O(n).

Thought process and trade-offs

- Heap approach: optimal for repeatedly finding maximum element.
- Alternative: sort after each operation - O(n² log n), much slower.
- Alternative: linear scan to find two max each time - O(n²), slower.
- Negation for max-heap: elegant workaround for Python's min-heap limitation.
- Current approach: optimal time complexity for this problem.
