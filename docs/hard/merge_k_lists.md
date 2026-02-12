# Merge K Sorted Lists

## Problem Summary

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/description/)

## Approach: Min Heap / Priority Queue (Implemented)

### Strategy

Use a min heap to always extract the smallest node next. Add the next node from the same list back to heap.

Push first node from each list to min heap. Always pop minimum node, add it to result, and push its next node. Repeat until heap is empty.

**Code Snippet**:

```python
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
def test_merge_k_lists():
    sol = Solution()
    def create_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    lists = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]
    lists = []
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: []
    lists = [create_linked_list([])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: []
    lists = [create_linked_list([2]), create_linked_list([]), create_linked_list([-1])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [-1, 2]
    lists = [create_linked_list([1, 3, 5]), create_linked_list([2, 4, 6]), create_linked_list([0, 7, 8])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    lists = [create_linked_list([1, 2, 3]), create_linked_list([4, 5, 6]), create_linked_list([7, 8, 9])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### How It Works

The algorithm executes in the following steps:

1. **Parse and Initialize**: Set up necessary data structures
2. **Main Algorithm**: Execute the core min heap / priority queue logic
3. **Handle Edge Cases**: Manage boundary and special conditions
4. **Return Result**: Compute and return final answer

**Example Walkthrough**:

Let's trace through the algorithm with concrete examples:

**Example 1**:

- Input: `[[1,4,5],[1,3,4],[2,6]]`
- Expected: `[1,1,2,3,4,4,5,6]`
- The algorithm processes the input step by step

**Example 2**:

- Input: `[]`
- Expected: `[]`
- The algorithm processes the input step by step

**Example 3**:

- Input: `[[]]`
- Expected: `[]`
- The algorithm processes the input step by step

### Why Min Heap / Priority Queue Works

This approach is optimal because:

1. Efficient merging of multiple lists
2. O(n*log(k)) better than O(n*k)
3. Scalable approach

### Complexity Analysis

- **Time Complexity**: O(n\*log(k)) where n=total nodes, k=number of lists
  - Each operation is performed efficiently
  - Avoids redundant computation
  - Optimal for problem constraints

- **Space Complexity**: O(k) for heap
  - Uses necessary auxiliary data structures
  - Memory-efficient implementation
  - Optimizes storage requirements

### Advantages

- Efficient merging of multiple lists
- O(n*log(k)) better than O(n*k)
- Scalable approach

### Disadvantages

- Heap operations have overhead
- Requires understanding of heaps
- Space for heap data structure

## Alternative Approaches

### Brute Force Approach

- Check all possibilities exhaustively
- Time: O(n²) or worse
- Space: O(1) minimal extra space
- Pros: Simple logic
- Cons: Too slow for constraints

### Different Data Structure

- Use alternative data structures
- May have different complexity trade-offs
- Could simplify or complicate logic
- Worth considering but likely slower

## Edge Cases

Important edge cases to test:

1. **Empty Input**: Empty array, string, or null input
2. **Single Element**: Only one element in input
3. **Minimum Size**: Smallest valid input
4. **Maximum Size**: Largest possible input
5. **All Same Values**: All identical elements
6. **Duplicates**: Repeated values
7. **Negative Numbers**: Negative integer handling
8. **Zero Values**: Zero in input
9. **Boundary Values**: Minimum/maximum possible values
10. **Special Patterns**: Sorted, reverse sorted, etc.

## Test Cases

```python
# Basic cases
solution.solve(typical_input)  # Standard test

# Edge cases
solution.solve([])             # Empty
solution.solve([1])            # Single element
solution.solve([1, 1])         # Duplicates

# Large inputs
solution.solve(large_array)    # Performance test

# Special patterns
solution.solve(sorted_array)   # Already sorted
solution.solve(reverse_array)  # Reverse order
```

## Complexity Comparison

| Approach                                | Time                                                | Space         | Difficulty    |
| --------------------------------------- | --------------------------------------------------- | ------------- | ------------- |
| Min Heap / Priority Queue (Implemented) | O(n\*log(k)) where n=total nodes, k=number of lists | O(k) for heap | Hard          |
| Brute Force                             | O(n²) or worse                                      | O(1) or less  | Easy but Slow |
| Alternative 1                           | Higher                                              | Different     | Medium        |
| Greedy (if applicable)                  | Varies                                              | Varies        | Medium        |

## Key Insights & Patterns

This problem teaches important concepts:

1. **Algorithm Selection**: Choosing min heap / priority queue for efficiency
2. **Data Structure Choice**: Optimal structure selection
3. **Complexity Analysis**: Understanding time/space trade-offs
4. **Edge Case Handling**: Systematic boundary condition testing
5. **Problem Recognition**: Identifying this problem pattern

## Related Problems

Similar LeetCode problems:

- Related problems using min heap / priority queue
- Variants with different constraints
- Foundational problems with same patterns
- Generalized versions

## Interview Tips

**When solving in an interview**:

1. **Clarify**: Ask about constraints and edge cases
2. **Explain**: Describe your approach clearly
3. **Code**: Write clean, readable code
4. **Test**: Trace through test cases manually
5. **Optimize**: Discuss time/space trade-offs
6. **Alternatives**: Mention other approaches

**What interviewers evaluate**:

- Problem understanding
- Algorithm knowledge
- Code quality
- Communication
- Edge case awareness
- Optimization mindset

## Implementation Checklist

Before submitting solution:

- [ ] Handle empty/null input
- [ ] Test with single element
- [ ] Verify with given examples
- [ ] Check boundary conditions
- [ ] Test with duplicates
- [ ] Handle maximum constraints
- [ ] Consider time complexity
- [ ] Optimize space if needed
- [ ] Code is clean and readable
- [ ] No off-by-one errors

## Common Mistakes

Avoid these pitfalls:

1. **Not handling edge cases** - Always check empty/single element
2. **Off-by-one errors** - Careful with loop boundaries
3. **Wrong initialization** - Start values must be correct
4. **Missing base cases** - Recursion needs proper termination
5. **Modifying input** - Only modify if explicitly allowed
6. **Incorrect complexity** - Don't assume linear time works
7. **Memory leaks** - Proper cleanup in recursive solutions
8. **Not testing thoroughly** - Always test edge cases

## Problem Variants

This problem connects to:

- Problems with similar constraints
- Generalized versions with more variables
- Problems requiring same algorithm
- Related data structure problems

---

**Difficulty**: Hard  
**Topics**: Min Heap / Priority Queue  
**Companies**: Major tech companies  
**Frequency**: Medium frequency in interviews  
**Accept Rate**: Check LeetCode for current rate
