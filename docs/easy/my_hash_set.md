# Design HashSet

Problem summary

- Implement a HashSet from scratch without using built-in hash table libraries.
- Support add(key), remove(key), and contains(key) operations.
- All keys are integers.

Current implementation (in repository)

- Implementation uses array of buckets with chaining:
  - Creates array of 1000 buckets (lists).
  - Hash function: key % bucket_size.
  - add(): computes hash, appends to bucket if not present.
  - remove(): computes hash, removes from bucket if present.
  - contains(): computes hash, checks if key in bucket.
- Example code:
  ```python
  def __init__(self):
      self.bucket_size = 1000
      self.hash_set = [[] for _ in range(self.bucket_size)]
  def _hash_function(self, key):
      return key % self.bucket_size
  def add(self, key: int) -> None:
      hash_key = self._hash_function(key)
      if key not in self.hash_set[hash_key]:
          self.hash_set[hash_key].append(key)
  ```

Why this works

- Hash function distributes keys across buckets.
- Chaining handles collisions: bucket stores list of keys that hash to same value.
- Modulo operation provides uniform distribution for random keys.
- Checking membership before add avoids duplicates.

Time complexity

- Average case: O(1) if keys distributed well, few collisions.
- Worst case: O(n) if all keys hash to same bucket (becomes linear search).
- Overall time complexity: O(n/bucket_size) = O(1) average with good distribution.

Space complexity

- Array of 1000 buckets: O(bucket_size) = O(1000) = O(1) fixed.
- Total stored keys: O(n).
- Overall space complexity: O(n).

Thought process and trade-offs

- Custom implementation: demonstrates understanding of hash table internals.
- Chaining: simple collision resolution, unbounded growth per bucket.
- Bucket size 1000: reasonable for moderate key ranges, could be dynamic.
- Alternative: open addressing (linear probing, quadratic probing) - more complex.
- For interview: this shows proper hash set implementation principles.
