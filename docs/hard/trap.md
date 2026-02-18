# Trapping Rain Water

## Problem Summary

Given an elevation map, calculate how much water can be trapped after raining.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/)

## Approach: Two Pointers (Implemented)

### Strategy

Water at position i = min(leftMax[i], rightMax[i]) - height[i]. Use two pointers from ends moving toward center.

Maintain leftMax and rightMax. Move the pointer with smaller height and accumulate trapped water. This works because the water level at current position is determined by the minimum of max heights on both sides.

**Code Snippet**:

```python
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        leftMax = rightMax = trap_water = 0
        left = 0
        right = n - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    trap_water += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    trap_water += rightMax - height[right]
                right -= 1
        return trap_water
def test_trap():
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected output: 6
    print(solution.trap([]))  # Expected output: 0
    print(solution.trap([4]))  # Expected output: 0
    print(solution.trap([4,2]))  # Expected output: 0
    print(solution.trap([4,2,3]))  # Expected output: 1
    print(solution.trap([3,3,3,3]))  # Expected output: 0
    print(solution.trap([1,2,3,4,5]))  # Expected output: 0
    print(solution.trap([5,4,3,2,1]))  # Expected output: 0
    print(solution.trap([0,2,0,4,0,3,0,5,0,1]))  # Expected output: 12
    print(solution.trap([5,2,1,2,1,5]))  # Expected output: 14
test_trap()
```

### How It Works

The algorithm executes in the following steps:

1. **Parse and Initialize**: Set up necessary data structures
2. **Main Algorithm**: Execute the core two pointers logic
3. **Handle Edge Cases**: Manage boundary and special conditions  
4. **Return Result**: Compute and return final answer

**Example Walkthrough**:

Let's trace through the algorithm with concrete examples:

**Example 1**:  
- Input: `[0,1,0,2,1,0,1,3,2,1,2,1]`  
- Expected: `6`  
- The algorithm processes the input step by step

**Example 2**:  
- Input: `[4,2,3]`  
- Expected: `1`  
- The algorithm processes the input step by step

**Example 3**:  
- Input: `[5,4,3,2,1]`  
- Expected: `0`  
- The algorithm processes the input step by step

### Why Two Pointers Works

This approach is optimal because:

1. Optimal time complexity O(n)
2. Constant space usage
3. Single pass algorithm

### Complexity Analysis

- **Time Complexity**: O(n) - single pass with two pointers
  - Each operation is performed efficiently
  - Avoids redundant computation
  - Optimal for problem constraints

- **Space Complexity**: O(1) - only using pointer variables
  - Uses necessary auxiliary data structures
  - Memory-efficient implementation
  - Optimizes storage requirements

### Advantages

- Optimal time complexity O(n)
- Constant space usage
- Single pass algorithm
- Elegant solution

### Disadvantages

- Logic requires careful understanding
- Index management can be tricky
- Not immediately intuitive

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

| Approach | Time | Space | Difficulty |
|----------|------|-------|-----------|
| Two Pointers (Implemented) | O(n) - single pass with two pointers | O(1) - only using pointer variables | Hard |
| Brute Force | O(n²) or worse | O(1) or less | Easy but Slow |
| Alternative 1 | Higher | Different | Medium |
| Greedy (if applicable) | Varies | Varies | Medium |

## Key Insights & Patterns

This problem teaches important concepts:

1. **Algorithm Selection**: Choosing two pointers for efficiency
2. **Data Structure Choice**: Optimal structure selection
3. **Complexity Analysis**: Understanding time/space trade-offs
4. **Edge Case Handling**: Systematic boundary condition testing
5. **Problem Recognition**: Identifying this problem pattern

## Related Problems

Similar LeetCode problems:
- Related problems using two pointers
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
**Topics**: Two Pointers  
**Companies**: Major tech companies  
**Frequency**: Medium frequency in interviews  
**Accept Rate**: Check LeetCode for current rate
