# Candy Distribution

## Problem Summary

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/candy/)

## Approach: Greedy with Two-Pass (Implemented)

### Strategy

Two passes: left-to-right ensures ascending requirement, right-to-left ensures descending requirement.

First pass: if rating increases, increment candy. Second pass: if rating increases going right, ensure candy increases. Final pass: verify all conditions.

**Code Snippet**:

```python
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)
def test_candy():
    solution = Solution()
    print(solution.candy([1, 0, 2])) # Expected output: 5
    print(solution.candy([1, 2, 2])) # Expected output: 4
    print(solution.candy([1, 3, 4, 5, 2])) # Expected output: 11
    print(solution.candy([1, 2, 3, 4, 5])) # Expected output: 15
    print(solution.candy([5, 4, 3, 2, 1])) # Expected output: 15
    print(solution.candy([1, 2, 3, 2, 1])) # Expected output: 9
    print(solution.candy([1])) # Expected output: 1
    print(solution.candy([1, 2])) # Expected output: 3
    print(solution.candy([2, 1])) # Expected output: 3
    print(solution.candy([1, 0, 2, 1])) # Expected output: 6
test_candy()
```

### How It Works

The algorithm executes in the following steps:

1. **Parse and Initialize**: Set up necessary data structures
2. **Main Algorithm**: Execute the core greedy with two-pass logic
3. **Handle Edge Cases**: Manage boundary and special conditions
4. **Return Result**: Compute and return final answer

**Example Walkthrough**:

Let's trace through the algorithm with concrete examples:

**Example 1**:

- Input: `[1,0,2]`
- Expected: `5`
- The algorithm processes the input step by step

**Example 2**:

- Input: `[1,2,2]`
- Expected: `4`
- The algorithm processes the input step by step

**Example 3**:

- Input: `[1,3,4,5,2]`
- Expected: `11`
- The algorithm processes the input step by step

### Why Greedy with Two-Pass Works

This approach is optimal because:

1. Minimal candy distribution
2. Greedy approach works perfectly
3. Clear two-pass strategy

### Complexity Analysis

- **Time Complexity**: O(n) - two passes through array
  - Each operation is performed efficiently
  - Avoids redundant computation
  - Optimal for problem constraints

- **Space Complexity**: O(n) for candy array
  - Uses necessary auxiliary data structures
  - Memory-efficient implementation
  - Optimizes storage requirements

### Advantages

- Minimal candy distribution
- Greedy approach works perfectly
- Clear two-pass strategy

### Disadvantages

- Requires two passes
- Need to manage state carefully
- Extra space for tracking candies

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

| Approach                           | Time                            | Space                | Difficulty    |
| ---------------------------------- | ------------------------------- | -------------------- | ------------- |
| Greedy with Two-Pass (Implemented) | O(n) - two passes through array | O(n) for candy array | Hard          |
| Brute Force                        | O(n²) or worse                  | O(1) or less         | Easy but Slow |
| Alternative 1                      | Higher                          | Different            | Medium        |
| Greedy (if applicable)             | Varies                          | Varies               | Medium        |

## Key Insights & Patterns

This problem teaches important concepts:

1. **Algorithm Selection**: Choosing greedy with two-pass for efficiency
2. **Data Structure Choice**: Optimal structure selection
3. **Complexity Analysis**: Understanding time/space trade-offs
4. **Edge Case Handling**: Systematic boundary condition testing
5. **Problem Recognition**: Identifying this problem pattern

## Related Problems

Similar LeetCode problems:

- Related problems using greedy with two-pass
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
**Topics**: Greedy with Two-Pass  
**Companies**: Major tech companies  
**Frequency**: Medium frequency in interviews  
**Accept Rate**: Check LeetCode for current rate
