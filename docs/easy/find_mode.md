# Find Mode in Binary Search Tree

## Problem Summary

- Given the root of a binary search tree (BST), find all values that appear most frequently in the tree.
- Return a list of all modal values (values with maximum frequency).
- Example: tree with values [1, 2, 2] → [2] (2 appears most often).

Approach (DFS with frequency counter)

- Use depth-first search (DFS) to traverse the entire tree.
- Maintain a frequency counter (defaultdict) that counts occurrences of each node value.
- After traversing the tree:
  - Find the maximum frequency using `max(counter.values())`.
  - Collect all values whose frequency equals the maximum frequency.
- Return the list of modal values.

Why this works (thought process)

- DFS guarantees we visit every node in the tree exactly once.
- A frequency counter tallies all occurrences; we then identify the maximum count.
- All values with the maximum count are modes by definition.
- This approach is straightforward and works for any tree structure.

Time and space complexity

- Time: O(n) — visit each node once in DFS; O(n) to find max frequency; O(k) to collect results (k = number of distinct values). Overall O(n).
- Space: O(h) for the DFS recursion stack (h = height of tree). In the worst case h = n (skewed tree), so worst-case O(n).
  - Plus O(k) for the frequency counter, where k = number of distinct node values (at most n).

Edge cases and robustness

- Empty tree (None) → DFS returns immediately; counter is empty; `max()` on empty sequence raises ValueError. Handle by checking if root is None first.
- Single node → frequency 1; that node's value is the mode.
- All nodes have the same value → that value is the only mode.
- All nodes have different values (all frequencies = 1) → all nodes are modes.
- Tree with negative values → handled naturally; counter works with any integer keys.

Example testcases (from repository)

- Tree [1, null, 2, 2] → [2]
- Tree [1] → [1]
- Tree [1, 1, 2, null, null, 2] → [1, 2]
- Tree [9, 7, 8, 5, 6, 3, 4] (all distinct) → [9, 7, 5, 6, 8, 3, 4]

Alternative approaches

- In-order traversal + one-pass counting: exploit BST property for linear time in-order scan. More space-efficient if in-order is already implemented.
- Using Counter from collections: `Counter(all_node_values)` after collecting all values. Slightly cleaner but requires collecting all values first.
- Without extra space (if in-place allowed): use Morris traversal (threaded tree). Very complex; not practical here.

Thought process / design choices

- Chose defaultdict for clean frequency counting without explicit initialization.
- DFS is intuitive and works for any tree (not relying on BST ordering).
- The two-step approach (count → find max → collect) is clear and easy to debug.
- If the problem requires in-order traversal specifically (BST property), adapt by using in-order DFS and tracking running counts.

Common pitfalls

- Assuming the tree is always non-empty; handle None root.
- Forgetting to return all modes (only returning the first one found).
- Using a regular dict and checking membership repeatedly instead of defaultdict.
- Not handling the case where multiple values have the same maximum frequency.

Improvements / notes

- If the tree is guaranteed to be a valid BST, you can use in-order traversal and track running frequency more efficiently (O(1) extra space with Morris traversal).
- For very large trees with memory constraints, in-order traversal with a single pass is preferable.
- The current solution prioritizes clarity and works for all binary trees, not just BSTs.

## Approach: Binary Search (Implemented)

### Strategy

The solution uses binary search to solve the problem efficiently.

### How It Works

Problem summary

- Given the root of a binary search tree (BST), find all values that appear most frequently in the tree.
- Return a list of all modal values (values with maximum frequency).
- Example: tree with values [1, 2, 2] → [2] (2 appears most often).

Approach (DFS with frequency counter)

- Use depth-first search (DFS) to traverse the entire tree.
- Maintain a frequency counter (defaultdict) that counts occurrences of each node value.
- After traversing the tree:
  - Find the maximum frequency using `max(counter.values())`.
  - Collect all values whose frequency equals the maximum frequency.
- Return the list of modal values.

Why this works (thought process)

- DFS guarantees we visit every node in the tree exactly once.
- A frequency counter tallies all occurrences; we then identify the maximum count.
- All values with the maximum count are modes by definition.
- This approach is straightforward and works for any tree structure.

Time and space complexity

- Time: O(n) — visit each node once in DFS; O(n) to find max frequency; O(k) to collect results (k = number of distinct values). Overall O(n).
- Space: O(h) for the DFS recursion stack (h = height of tree). In the worst case h = n (skewed tree), so worst-case O(n).
  - Plus O(k) for the frequency counter, where k = number of distinct node values (at most n).

Edge cases and robustness

- Empty tree (None) → DFS returns immediately; counter is empty; `max()` on empty sequence raises ValueError. Handle by checking if root is None first.
- Single node → frequency 1; that node's value is the mode.
- All nodes have the same value → that value is the only mode.
- All nodes have different values (all frequencies = 1) → all nodes are modes.
- Tree with negative values → handled naturally; counter works with any integer keys.

Example testcases (from repository)

- Tree [1, null, 2, 2] → [2]
- Tree [1] → [1]
- Tree [1, 1, 2, null, null, 2] → [1, 2]
- Tree [9, 7, 8, 5, 6, 3, 4] (all distinct) → [9, 7, 5, 6, 8, 3, 4]

Alternative approaches

- In-order traversal + one-pass counting: exploit BST property for linear time in-order scan. More space-efficient if in-order is already implemented.
- Using Counter from collections: `Counter(all_node_values)` after collecting all values. Slightly cleaner but requires collecting all values first.
- Without extra space (if in-place allowed): use Morris traversal (threaded tree). Very complex; not practical here.

Thought process / design choices

- Chose defaultdict for clean frequency counting without explicit initialization.
- DFS is intuitive and works for any tree (not relying on BST ordering).
- The two-step approach (count → find max → collect) is clear and easy to debug.
- If the problem requires in-order traversal specifically (BST property), adapt by using in-order DFS and tracking running counts.

Common pitfalls

- Assuming the tree is always non-empty; handle None root.
- Forgetting to return all modes (only returning the first one found).
- Using a regular dict and checking membership repeatedly instead of defaultdict.
- Not handling the case where multiple values have the same maximum frequency.

Improvements / notes

- If the tree is guaranteed to be a valid BST, you can use in-order traversal and track running frequency more efficiently (O(1) extra space with Morris traversal).
- For very large trees with memory constraints, in-order traversal with a single pass is preferable.
- The current solution prioritizes clarity and works for all binary trees, not just BSTs.

### Why Binary Search Works

- DFS guarantees we visit every node in the tree exactly once.
- A frequency counter tallies all occurrences; we then identify the maximum count.
- All values with the maximum count are modes by definition.
- This approach is straightforward and works for any tree structure.

Time and space complexity

- Time: O(n) — visit each node once in DFS; O(n) to find max frequency; O(k) to collect results (k = number of distinct values). Overall O(n).
- Space: O(h) for the DFS recursion stack (h = height of tree). In the worst case h = n (skewed tree), so worst-case O(n).
  - Plus O(k) for the frequency counter, where k = number of distinct node values (at most n).

Edge cases and robustness

- Empty tree (None) → DFS returns immediately; counter is empty; `max()` on empty sequence raises ValueError. Handle by checking if root is None first.
- Single node → frequency 1; that node's value is the mode.
- All nodes have the same value → that value is the only mode.
- All nodes have different values (all frequencies = 1) → all nodes are modes.
- Tree with negative values → handled naturally; counter works with any integer keys.

Example testcases (from repository)

- Tree [1, null, 2, 2] → [2]
- Tree [1] → [1]
- Tree [1, 1, 2, null, null, 2] → [1, 2]
- Tree [9, 7, 8, 5, 6, 3, 4] (all distinct) → [9, 7, 5, 6, 8, 3, 4]

Alternative approaches

- In-order traversal + one-pass counting: exploit BST property for linear time in-order scan. More space-efficient if in-order is already implemented.
- Using Counter from collections: `Counter(all_node_values)` after collecting all values. Slightly cleaner but requires collecting all values first.
- Without extra space (if in-place allowed): use Morris traversal (threaded tree). Very complex; not practical here.

Thought process / design choices

- Chose defaultdict for clean frequency counting without explicit initialization.
- DFS is intuitive and works for any tree (not relying on BST ordering).
- The two-step approach (count → find max → collect) is clear and easy to debug.
- If the problem requires in-order traversal specifically (BST property), adapt by using in-order DFS and tracking running counts.

Common pitfalls

- Assuming the tree is always non-empty; handle None root.
- Forgetting to return all modes (only returning the first one found).
- Using a regular dict and checking membership repeatedly instead of defaultdict.
- Not handling the case where multiple values have the same maximum frequency.

Improvements / notes

- If the tree is guaranteed to be a valid BST, you can use in-order traversal and track running frequency more efficiently (O(1) extra space with Morris traversal).
- For very large trees with memory constraints, in-order traversal with a single pass is preferable.
- The current solution prioritizes clarity and works for all binary trees, not just BSTs.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: - Time: O(n) — visit each node once in DFS; O(n) to find max frequency; O(k) to collect results (k = number of distinct values). Overall O(n). - Space: O(h) for the DFS recursion stack (h = height of tree). In the worst case h = n (skewed tree), so worst-case O(n).   - Plus O(k) for the frequency counter, where k = number of distinct node values (at most n). Edge cases and robustness - Empty tree (None) → DFS returns immediately; counter is empty; `max()` on empty sequence raises ValueError. Handle by checking if root is None first. - Single node → frequency 1; that node's value is the mode. - All nodes have the same value → that value is the only mode. - All nodes have different values (all frequencies = 1) → all nodes are modes. - Tree with negative values → handled naturally; counter works with any integer keys. Example testcases (from repository) - Tree [1, null, 2, 2] → [2] - Tree [1] → [1] - Tree [1, 1, 2, null, null, 2] → [1, 2] - Tree [9, 7, 8, 5, 6, 3, 4] (all distinct) → [9, 7, 5, 6, 8, 3, 4] Alternative approaches - In-order traversal + one-pass counting: exploit BST property for linear time in-order scan. More space-efficient if in-order is already implemented. - Using Counter from collections: `Counter(all_node_values)` after collecting all values. Slightly cleaner but requires collecting all values first. - Without extra space (if in-place allowed): use Morris traversal (threaded tree). Very complex; not practical here. Thought process / design choices - Chose defaultdict for clean frequency counting without explicit initialization. - DFS is intuitive and works for any tree (not relying on BST ordering). - The two-step approach (count → find max → collect) is clear and easy to debug. - If the problem requires in-order traversal specifically (BST property), adapt by using in-order DFS and tracking running counts. Common pitfalls - Assuming the tree is always non-empty; handle None root. - Forgetting to return all modes (only returning the first one found). - Using a regular dict and checking membership repeatedly instead of defaultdict. - Not handling the case where multiple values have the same maximum frequency. Improvements / notes - If the tree is guaranteed to be a valid BST, you can use in-order traversal and track running frequency more efficiently (O(1) extra space with Morris traversal). - For very large trees with memory constraints, in-order traversal with a single pass is preferable. - The current solution prioritizes clarity and works for all binary trees, not just BSTs.

### Advantages

- Efficient binary search solution
- Clear and maintainable code

### Disadvantages

- May require additional space
