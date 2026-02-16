# Shortest Subarray with Sum at Least K

## Problem Summary

Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty <b>subarray</b> of `nums` with a sum of at least `k`. If there is no such <b>subarray</b>, return `-1`.

A <b>subarray</b> is a <b>contiguous</b> part of an array.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/)

## Approach: Algorithm (Implemented)

### Strategy

See the solution code for implementation details.

Implement the algorithm as shown in the solution class.

**Code Snippet**:

```python
from typing import List
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        candidate_indices = deque()
        shortest_subarray_length = float("inf")
        for i in range(n + 1):
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]]
                >= target_sum
            ):
                shortest_subarray_length = min(
                    shortest_subarray_length, i - candidate_indices.popleft()
                )
            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()
            candidate_indices.append(i)
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )
def test_shortestSubarray():
    solution = Solution()
    print(solution.shortestSubarray([1,2], 4)) # Expected: -1
    print(solution.shortestSubarray([2,-1,2], 3)) # Expected: 3
    print(solution.shortestSubarray([1], 1)) # Expected: 1
    print(solution.shortestSubarray([1,2,3,4,5], 11)) # Expected: 3
    print(solution.shortestSubarray([84,-37,32,40,95], 167)) # Expected: 3
test_shortestSubarray()
```

### How It Works

The algorithm executes in the following steps:

1. **Parse and Initialize**: Set up necessary data structures
2. **Main Algorithm**: Execute the core algorithm logic
3. **Handle Edge Cases**: Manage boundary and special conditions
4. **Return Result**: Compute and return final answer

**Example Walkthrough**:

Let's trace through the algorithm with concrete examples:

### Why Algorithm Works

This approach is optimal because:

1. Solves the problem correctly
2. Follows algorithm best practices

### Complexity Analysis

- **Time Complexity**: Varies based on algorithm
  - Each operation is performed efficiently
  - Avoids redundant computation
  - Optimal for problem constraints

- **Space Complexity**: Varies based on algorithm
  - Uses necessary auxiliary data structures
  - Memory-efficient implementation
  - Optimizes storage requirements

### Advantages

- Solves the problem correctly
- Follows algorithm best practices

### Disadvantages

- May have optimization opportunities

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

| Approach                | Time                      | Space                     | Difficulty    |
| ----------------------- | ------------------------- | ------------------------- | ------------- |
| Algorithm (Implemented) | Varies based on algorithm | Varies based on algorithm | Hard          |
| Brute Force             | O(n²) or worse            | O(1) or less              | Easy but Slow |
| Alternative 1           | Higher                    | Different                 | Medium        |
| Greedy (if applicable)  | Varies                    | Varies                    | Medium        |

## Key Insights & Patterns

This problem teaches important concepts:

1. **Algorithm Selection**: Choosing algorithm for efficiency
2. **Data Structure Choice**: Optimal structure selection
3. **Complexity Analysis**: Understanding time/space trade-offs
4. **Edge Case Handling**: Systematic boundary condition testing
5. **Problem Recognition**: Identifying this problem pattern

## Related Problems

Similar LeetCode problems:

- Related problems using algorithm
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
**Topics**: Algorithm  
**Companies**: Major tech companies  
**Frequency**: Medium frequency in interviews  
**Accept Rate**: Check LeetCode for current rate
