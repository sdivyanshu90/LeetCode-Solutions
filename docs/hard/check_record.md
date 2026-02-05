# Check Record

## Problem Summary

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

- `'A'`: Absent.
- `'L'`: Late.
- `'P'`: Present.
  Any student is eligible for an attendance award if they meet <b>both</b> of the following criteria:

The student was absent (`'A'`) for <b>strictly</b> fewer than 2 days <b>total</b>.  
The student was <b>never</b> late (`'L'`) for 3 or more consecutive days.  
Given an integer `n`, return the <b>number</b> of possible attendance records of length `n` that make a student eligible for an attendance award. The answer may be very large, so return it <b>modulo</b> `10^9 + 7`.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/student-attendance-record-ii/description/)

## Approach: Algorithm (Implemented)

### Strategy

See the solution code for implementation details.

Implement the algorithm as shown in the solution class.

**Code Snippet**:

```python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp_curr_state = [[0] * 3 for _ in range(2)]
        dp_next_state = [[0] * 3 for _ in range(2)]
        dp_curr_state[0][0] = 1
        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    dp_next_state[total_absences][0] = (
                        dp_next_state[total_absences][0] +
                        dp_curr_state[total_absences][consecutive_lates]
                    ) % MOD
                    if total_absences < 1:
                        dp_next_state[total_absences + 1][0] = (
                            dp_next_state[total_absences + 1][0] +
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD
                    if consecutive_lates < 2:
                        dp_next_state[total_absences][consecutive_lates + 1] = (
                            dp_next_state[total_absences][consecutive_lates + 1] +
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD
            dp_curr_state = [row[:] for row in dp_next_state]
            dp_next_state = [[0] * 3 for _ in range(2)]
        count = sum(dp_curr_state[total_absences][consecutive_lates] \
                    for total_absences in range(2) \
                    for consecutive_lates in range(3)) % MOD
        return count
def test_check_record():
    s = Solution()
    n1 = 2
    print(s.checkRecord(n1)) # Expected output: 8
    n2 = 1
    print(s.checkRecord(n2)) # Expected output: 3
    n3 = 10101
    print(s.checkRecord(n3)) # Expected output: 183236316
    n4 = 0
    print(s.checkRecord(n4)) # Expected output: 1
    n5 = 5
    print(s.checkRecord(n5)) # Expected output: 94
test_check_record()
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
