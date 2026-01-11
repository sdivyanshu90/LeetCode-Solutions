# Find the Town Judge

## Problem Summary

- In a town of n people (labeled 1 to n), find the town judge if one exists.
- Judge: trusted by everyone (n-1 people), trusts nobody.
- Given trust array where trust[i] = [a, b] means person a trusts person b.
- Return the judge's label, or -1 if no judge exists.

Current implementation (in repository)

- Implementation uses trust score tracking:
  - Creates array to track "trust score" for each person.
  - For each trust relationship [a, b]: decrements score[a] (trusting someone), increments score[b] (being trusted).
  - Judge will have score = n-1 (trusted by all, trusts nobody).
  - Returns person with score == n-1, or -1 if none found.
- Example code:
  ```python
  people = [0] * (n + 1)
  for a, b in trust:
      people[a] -= 1
      people[b] += 1
  ```

Why this works

- Judge is trusted by n-1 people: +n-1 to score.
- Judge trusts nobody: no decrements to score.
- Non-judge either trusts someone (negative contribution) or isn't trusted by all.
- Score of exactly n-1 uniquely identifies the judge.
- Only one person can have this score (at most one judge).

Time complexity

- Let m = number of trust relationships.
- Initializing people array: O(n).
- Processing all trust relationships: O(m).
- Finding judge: O(n) to scan array.
- Overall time complexity: O(n + m).

Space complexity

- People array of size n+1: O(n).
- Space complexity: O(n).

Thought process and trade-offs

- Trust score approach: elegant single-pass solution.
- Alternative: track in-degree and out-degree separately - requires two arrays but same complexity.
- Alternative: build adjacency list for graph - more complex, same complexity.
- Current approach: simple and efficient.
- Edge case: n=1 with no trust relationships returns 1 (single person is vacuously the judge).

## Approach: Iterative (Implemented)

### Strategy

The solution uses iterative to solve the problem efficiently.

```python
  people = [0] * (n + 1)
  for a, b in trust:
      people[a] -= 1
      people[b] += 1
  ```

### How It Works

- Alternative: track in-degree and out-degree separately - requires two arrays but same complexity.
- Alternative: build adjacency list for graph - more complex, same complexity.
- Current approach: simple and efficient.
- Edge case: n=1 with no trust relationships returns 1 (single person is vacuously the judge).

### Why Iterative Works

- Judge is trusted by n-1 people: +n-1 to score.
- Judge trusts nobody: no decrements to score.
- Non-judge either trusts someone (negative contribution) or isn't trusted by all.
- Score of exactly n-1 uniquely identifies the judge.
- Only one person can have this score (at most one judge).

Time complexity

- Let m = number of trust relationships.
- Initializing people array: O(n).
- Processing all trust relationships: O(m).
- Finding judge: O(n) to scan array.
- Overall time complexity: O(n + m).

Space complexity

- People array of size n+1: O(n).
- Space complexity: O(n).

Thought process and trade-offs

- Trust score approach: elegant single-pass solution.
- Alternative: track in-degree and out-degree separately - requires two arrays but same complexity.
- Alternative: build adjacency list for graph - more complex, same complexity.
- Current approach: simple and efficient.
- Edge case: n=1 with no trust relationships returns 1 (single person is vacuously the judge).

### Complexity Analysis

- **Time Complexity**: - Let m = number of trust relationships. - Initializing people array: O(n). - Processing all trust relationships: O(m). - Finding judge: O(n) to scan array. - Overall time complexity: O(n + m). Space complexity - People array of size n+1: O(n). - Space complexity: O(n). Thought process and trade-offs - Trust score approach: elegant single-pass solution. - Alternative: track in-degree and out-degree separately - requires two arrays but same complexity. - Alternative: build adjacency list for graph - more complex, same complexity. - Current approach: simple and efficient. - Edge case: n=1 with no trust relationships returns 1 (single person is vacuously the judge).
- **Space Complexity**: - People array of size n+1: O(n). - Space complexity: O(n). Thought process and trade-offs - Trust score approach: elegant single-pass solution. - Alternative: track in-degree and out-degree separately - requires two arrays but same complexity. - Alternative: build adjacency list for graph - more complex, same complexity. - Current approach: simple and efficient. - Edge case: n=1 with no trust relationships returns 1 (single person is vacuously the judge).

### Advantages

- Efficient iterative solution
- Clear and maintainable code

### Disadvantages

- May require additional space
