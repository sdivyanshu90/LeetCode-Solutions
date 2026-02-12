# Maximum Score Words Formed by Letters

## Problem Summary

Given a list of `words`, a list of `single letters` (might be repeating), and a list of `scores` for every character.

Return the maximum score of any valid set of words formed by using the given letters (`words[i]` cannot be used two or more times).

It is not necessary to use all characters in `letters` and each letter can only be used once. Score of letters `'a'`, `'b'`, `'c'`, ... ,`'z'` is given by `score[0]`, `score[1]`, ... , `score[25]` respectively.

**LeetCode Problem**: [View on LeetCode](https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/)

## Approach: Algorithm (Implemented)

### Strategy

See the solution code for implementation details.

Implement the algorithm as shown in the solution class.

**Code Snippet**:

```python
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        self.max_score = 0
        freq = [0 for i in range(26)]
        subset_letters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1
        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            else:
                return True
        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                self.max_score = max(self.max_score, total_score)
                return
            check(w - 1, words, score, subset_letters, total_score)
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]
            if is_valid_word(subset_letters):
                check(w - 1, words, score, subset_letters, total_score)
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]
        check(W - 1, words, score, subset_letters, 0)
        return self.max_score
def test_max_score_words():
    solution = Solution()
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 19
    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 24
    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 0
    words = ["a","b","c"]
    letters = ["a","b","c"]
    score = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
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
