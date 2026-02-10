# First Missing Positive

## Problem Summary

Find the smallest positive integer that doesn't appear in the array.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/)

## Approach: In-place Array Manipulation (Implemented)

### Strategy

Place each positive integer i at position i-1 (if it fits). Then find first position where index+1 != value.

Iterate through array and swap elements to their correct positions. For each number n, place it at position n-1 if 0 < n <= len(nums). Then scan for the first missing positive.

**Code Snippet**:

```python
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
def test_first_missing_positive():
    s = Solution()
    print(s.firstMissingPositive([3,4,-1,1]))  # Expected output: 2
    print(s.firstMissingPositive([1,2,0]))  # Expected output: 3
    print(s.firstMissingPositive([-1,-2,-3]))  # Expected output: 1
    print(s.firstMissingPositive([]))  # Expected output: 1
    print(s.firstMissingPositive([1]))  # Expected output: 2
    print(s.firstMissingPositive([-1]))  # Expected output: 1
    print(s.firstMissingPositive([1,1,2,2]))  # Expected output: 3
    print(s.firstMissingPositive([7,8,9,11,12]))  # Expected output: 1
    print(s.firstMissingPositive([1,2,3,4,5]))  # Expected output: 6
    print(s.firstMissingPositive([2,3,7,6,8,-1,-10,15]))  # Expected output: 1
test_first_missing_positive()
```

### How It Works

The algorithm executes in the following steps:

1. **Parse and Initialize**: Set up necessary data structures
2. **Main Algorithm**: Execute the core in-place array manipulation logic
3. **Handle Edge Cases**: Manage boundary and special conditions  
4. **Return Result**: Compute and return final answer

**Example Walkthrough**:

Let's trace through the algorithm with concrete examples:

**Example 1**:  
- Input: `[3,4,-1,1]`  
- Expected: `2`  
- The algorithm processes the input step by step

**Example 2**:  
- Input: `[1,2,0]`  
- Expected: `3`  
- The algorithm processes the input step by step

**Example 3**:  
- Input: `[-1,-2,-3]`  
- Expected: `1`  
- The algorithm processes the input step by step

### Why In-place Array Manipulation Works

This approach is optimal because:

1. Optimal time and space complexity
2. In-place modification
3. No extra data structures needed

### Complexity Analysis

- **Time Complexity**: O(n) - single pass with constant work per element
  - Each operation is performed efficiently
  - Avoids redundant computation
  - Optimal for problem constraints

- **Space Complexity**: O(1) - modify array in-place
  - Uses necessary auxiliary data structures
  - Memory-efficient implementation
  - Optimizes storage requirements

### Advantages

- Optimal time and space complexity
- In-place modification
- No extra data structures needed

### Disadvantages

- Modifies input array
- Complex swap logic
- Requires careful index management

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
| In-place Array Manipulation (Implemented) | O(n) - single pass with constant work per element | O(1) - modify array in-place | Hard |
| Brute Force | O(n²) or worse | O(1) or less | Easy but Slow |
| Alternative 1 | Higher | Different | Medium |
| Greedy (if applicable) | Varies | Varies | Medium |

## Key Insights & Patterns

This problem teaches important concepts:

1. **Algorithm Selection**: Choosing in-place array manipulation for efficiency
2. **Data Structure Choice**: Optimal structure selection
3. **Complexity Analysis**: Understanding time/space trade-offs
4. **Edge Case Handling**: Systematic boundary condition testing
5. **Problem Recognition**: Identifying this problem pattern

## Related Problems

Similar LeetCode problems:
- Related problems using in-place array manipulation
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
**Topics**: In-place Array Manipulation  
**Companies**: Major tech companies  
**Frequency**: Medium frequency in interviews  
**Accept Rate**: Check LeetCode for current rate
