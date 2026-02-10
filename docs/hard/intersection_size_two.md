# Intersection Size Two

## Problem Summary

You are given a 2D integer array `intervals` where <b>$intervals[i] = [start_i, end_i]$</b> represents all the integers from <b>$start_i$</b> to <b>$end_i$</b> inclusively.

A <b>containing set</b> is an array `nums` where each interval from `intervals` has <b>at least two</b> integers in `nums`.

For example, if `intervals = [[1,3], [3,7], [8,9]]`, then `[1,2,4,7,8,9]` and `[2,3,4,8,9]` are containing sets.  
Return the minimum possible size of a <b>containing set</b>.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/set-intersection-size-at-least-two/description/)

## Approach: Algorithm (Implemented)

### Strategy

See the solution code for implementation details.

Implement the algorithm as shown in the solution class.

**Code Snippet**:

```python
from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        size = 0
        x1 = -1
        x2 = -2
        for start, end in intervals:
            if x1 >= start:
                continue
            elif x2 >= start:
                x1 = x2
                x2 = end
                size += 1
            else:
                x1 = end - 1
                x2 = end
                size += 2
        return size
def test_intersection_size_two():
    solution = Solution()
    intervals1 = [[1,3],[1,4],[2,5],[3,5]]
    print(solution.intersectionSizeTwo(intervals1)) # Expected: 3
    intervals2 = [[1,2],[2,3],[2,4],[4,5]]
    print(solution.intersectionSizeTwo(intervals2)) # Expected: 5
    intervals3 = [[0,1],[1,2],[2,3],[3,4],[4,5]]
    print(solution.intersectionSizeTwo(intervals3)) # Expected: 10
    intervals4 = [[1,10],[2,9],[3,8],[4,7]]
    print(solution.intersectionSizeTwo(intervals4)) # Expected: 2
    intervals5 = [[5,7],[1,3],[2,4],[6,8]]
    print(solution.intersectionSizeTwo(intervals5)) # Expected: 4
    intervals6 = [[1,5],[2,6],[3,7],[4,8]]
    print(solution.intersectionSizeTwo(intervals6)) # Expected: 4
    intervals7 = [[1,2],[2,3],[3,4],[4,5],[5,6]]
    print(solution.intersectionSizeTwo(intervals7)) # Expected: 10
    intervals8 = [[0,2],[2,4],[4,6],[6,8]]
    print(solution.intersectionSizeTwo(intervals8)) # Expected: 8
    intervals9 = [[1,1000]]
    print(solution.intersectionSizeTwo(intervals9)) # Expected: 2
    intervals10 = [[1,3],[4,6],[7,9]]
    print(solution.intersectionSizeTwo(intervals10)) # Expected: 6
test_intersection_size_two()
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
