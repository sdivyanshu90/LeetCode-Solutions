# Number of Atoms

## Problem Summary

Given a string `formula` representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than `1`. If the count is `1`, no digits will follow.

For example, `"H2O"` and `"H2O2"` are possible, but `"H1O2"` is impossible.  
Two formulas are concatenated together to produce another formula.

For example, `"H2O2He3Mg4"` is also a formula.  
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, `"(H2O2)"` and `"(H2O2)3"` are formulas.  
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than `1`), followed by the second name (in sorted order), followed by its count (if that count is more than `1`), and so on.

The test cases are generated so that all the values in the output fit in a <b>32-bit</b> integer.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/number-of-atoms/description/)

## Approach: Algorithm (Implemented)

### Strategy

See the solution code for implementation details.

Implement the algorithm as shown in the solution class.

**Code Snippet**:

```python
from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        index = 0
        while index < len(formula):
            if formula[index] == "(":
                stack.append(defaultdict(int))
                index += 1
            elif formula[index] == ")":
                curr_map = stack.pop()
                index += 1
                multiplier = ""
                while index < len(formula) and formula[index].isdigit():
                    multiplier += formula[index]
                    index += 1
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier
                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]
            else:
                curr_atom = formula[index]
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1
                curr_count = ""
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1
                if curr_count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(curr_count)
        final_map = dict(sorted(stack[0].items()))
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        return ans
def test_count_of_atoms():
    solution = Solution()
    formula = "H2O"
    print(solution.countOfAtoms(formula))  # Expected: "H2O"
    formula = "Mg(OH)2"
    print(solution.countOfAtoms(formula))  # Expected: "H2MgO2"
    formula = "K4(ON(SO3)2)2"
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
