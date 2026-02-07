# Find In Mountain Array

## Problem Summary

You may recall that an array `arr` is a mountain array if and only if:

- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:  
   - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`  
   - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`  
  Given a mountain array `mountainArr`, return the minimum `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

- `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).
- `MountainArray.length()` returns the length of the array.  
  Submissions making more than `100` calls to `MountainArray.get` will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/find-in-mountain-array/description/)

## Approach: Algorithm (Implemented)

### Strategy

See the solution code for implementation details.

Implement the algorithm as shown in the solution class.

**Code Snippet**:

```python
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        left, right = 1, length - 2
        while left != right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        left, right = 0, peak
        while left != right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        if mountainArr.get(left) == target:
            return left
        left, right = peak + 1, length - 1
        while left != right:
            mid = (left + right) // 2
            if mountainArr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        if mountainArr.get(left) == target:
            return left
        return -1
def test_find_in_mountain_array():
    solution = Solution()
    class MountainArray1:
        def __init__(self):
            self.arr = [1, 2, 3, 4, 5, 3, 1]
        def get(self, index: int) -> int:
            return self.arr[index]
        def length(self) -> int:
            return len(self.arr)
    mountainArr1 = MountainArray1()
    target1 = 3
    print(solution.findInMountainArray(target1, mountainArr1))  # Expected output: 2
    class MountainArray2:
        def __init__(self):
            self.arr = [0, 1, 2, 4, 2, 1]
        def get(self, index: int) -> int:
            return self.arr[index]
        def length(self) -> int:
            return len(self.arr)
    mountainArr2 = MountainArray2()
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
