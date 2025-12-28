# Design HashMap

Problem summary

- Implement a HashMap from scratch without using built-in hash table libraries.
- Support put(key, value), get(key), and remove(key) operations.
- All keys and values are integers.

Current implementation (in repository)

- Implementation uses Python dictionary:
  - Uses built-in dict as underlying storage.
  - put() stores key-value pair in dictionary.
  - get() returns value if key exists, -1 otherwise using dict.get().
  - remove() deletes key if exists using conditional check and del.
- Example code:
  ```python
  def __init__(self):
      self.data = {}
  def put(self, key: int, value: int) -> None:
      self.data[key] = value
  def get(self, key: int) -> int:
      return self.data.get(key, -1)
  ```

Why this works

- Python dict provides hash table functionality.
- put() handles both insert and update operations.
- get() with default value -1 matches requirement for missing keys.
- remove() with existence check avoids KeyError.

Time complexity

- All operations (put, get, remove): O(1) average case.
- Worst case (hash collisions): O(n) but rare with good hash function.
- Overall time complexity: O(1) average.

Space complexity

- Dictionary stores up to n key-value pairs.
- Space complexity: O(n).

Thought process and trade-offs

- Using built-in dict: simple but defeats "design from scratch" intent.
- True implementation should use: array of buckets, hash function, collision handling (chaining or open addressing).
- For interview: mention this is simplified version; actual implementation would involve custom hash table structure.
- For production/practice: use built-in dict (shown here) for reliability and efficiency.
