# Minimum Window Substring

## Problem Summary

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the <b>minimum window substring</b> of `s` such that every character in `t` <b>(including duplicates)</b> is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is <b>unique</b>.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/minimum-window-substring/description/)

## Approach: Sliding Window with Hash Map (Implemented)

### Strategy

Use sliding window with character frequency maps. Expand right pointer to include characters, contract left when valid window found.

Maintain frequency maps for pattern and window. Use two pointers. Expand right until window contains all characters. Then contract left to minimize window.

**Code Snippet**:

```python
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1
        required = len(dictT)
        l, r = 0, 0
        formed = 0
        windowCounts = defaultdict(int)
        ans = [-1, 0, 0]
        while r < len(s):
            c = s[r]
            windowCounts[c] += 1
            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1
            while l <= r and formed == required:
                c = s[l]
                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r
                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == -1 else s[ans[1]:ans[2] + 1]
def test_min_window():
    solution = Solution()
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(solution.minWindow(s1, t1))  # Expected output: "BANC"
    s2 = "a"
    t2 = "a"
    print(solution.minWindow(s2, t2))  # Expected output: "a"
    s3 = "a"
    t3 = "aa"
    print(solution.minWindow(s3, t3))  # Expected output: ""
    s4 = "ab"
    t4 = "A"
    print(solution.minWindow(s4, t4))  # Expected output: ""
    s5 = "aaflslflsldkalskaaa"
    t5 = "aaa"
    print(solution.minWindow(s5, t5))  # Expected output: "aaa"
    s6 = "aa"
    t6 = "aa"
    print(solution.minWindow(s6, t6))  # Expected output: "aa"
```

### How It Works

The algorithm executes in the following steps:

1. **Parse and Initialize**: Set up necessary data structures
2. **Main Algorithm**: Execute the core sliding window with hash map logic
3. **Handle Edge Cases**: Manage boundary and special conditions
4. **Return Result**: Compute and return final answer

**Example Walkthrough**:

Let's trace through the algorithm with concrete examples:

**Example 1**:

- Input: `'ADOBECODEBANC', 'ABC'`
- Expected: `'BANC'`
- The algorithm processes the input step by step

**Example 2**:

- Input: `'a', 'a'`
- Expected: `'a'`
- The algorithm processes the input step by step

**Example 3**:

- Input: `'a', 'aa'`
- Expected: `''`
- The algorithm processes the input step by step

### Why Sliding Window with Hash Map Works

This approach is optimal because:

1. Optimal time complexity
2. Constant space for character maps
3. Handles all edge cases

### Complexity Analysis

- **Time Complexity**: O(m + n) where m=len(s), n=len(t)
  - Each operation is performed efficiently
  - Avoids redundant computation
  - Optimal for problem constraints

- **Space Complexity**: O(1) - at most 26 lowercase letters in maps
  - Uses necessary auxiliary data structures
  - Memory-efficient implementation
  - Optimizes storage requirements

### Advantages

- Optimal time complexity
- Constant space for character maps
- Handles all edge cases

### Disadvantages

- Requires careful frequency tracking
- Window contraction logic can be complex
- Multiple conditions to check

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

| Approach                                   | Time                              | Space                                       | Difficulty    |
| ------------------------------------------ | --------------------------------- | ------------------------------------------- | ------------- |
| Sliding Window with Hash Map (Implemented) | O(m + n) where m=len(s), n=len(t) | O(1) - at most 26 lowercase letters in maps | Hard          |
| Brute Force                                | O(n²) or worse                    | O(1) or less                                | Easy but Slow |
| Alternative 1                              | Higher                            | Different                                   | Medium        |
| Greedy (if applicable)                     | Varies                            | Varies                                      | Medium        |

## Key Insights & Patterns

This problem teaches important concepts:

1. **Algorithm Selection**: Choosing sliding window with hash map for efficiency
2. **Data Structure Choice**: Optimal structure selection
3. **Complexity Analysis**: Understanding time/space trade-offs
4. **Edge Case Handling**: Systematic boundary condition testing
5. **Problem Recognition**: Identifying this problem pattern

## Related Problems

Similar LeetCode problems:

- Related problems using sliding window with hash map
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
**Topics**: Sliding Window with Hash Map  
**Companies**: Major tech companies  
**Frequency**: Medium frequency in interviews  
**Accept Rate**: Check LeetCode for current rate
