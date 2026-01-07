# Actors and Directors Who Cooperated At Least Three Times

## Problem Summary

- Given a DataFrame `actor_director` with actor-director pairs, find all pairs that have cooperated at least three times.
- Each row represents one cooperation between an actor and a director.
- Return a DataFrame with columns `actor_id` and `director_id` for pairs with at least 3 cooperations.

Current implementation (in repository)

- Implementation uses pandas groupby and filtering:
  - Groups by both `actor_id` and `director_id` columns.
  - Counts the size of each group using `.size()` to get cooperation count.
  - Filters groups where cooperation count >= 3.
  - Returns only the `actor_id` and `director_id` columns.
- Example code:
  ```python
  counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
  result = counts[counts['cooperation_count'] >= 3][['actor_id', 'director_id']]
  ```

Why this works

- `groupby(['actor_id', 'director_id'])` groups rows by unique actor-director pairs.
- `.size()` counts the number of rows in each group, representing cooperation count.
- Boolean filtering `counts['cooperation_count'] >= 3` selects only qualifying pairs.
- Column selection `[['actor_id', 'director_id']]` ensures the result has the required format.

Time complexity

- Let n = number of rows in the DataFrame.
- Groupby operation costs O(n) for scanning all rows and creating groups.
- Size calculation is O(n) as it counts all rows.
- Filtering is O(k) where k is the number of unique pairs.
- Overall time complexity: O(n).

Space complexity

- The groupby operation creates intermediate data structures storing unique pairs and their counts: O(k) where k is the number of unique actor-director pairs.
- Result DataFrame stores only qualifying pairs: O(m) where m <= k.
- Overall space complexity: O(k).

Thought process and trade-offs

- Pandas approach: simple, readable, and leverages built-in optimizations for grouping and aggregation.
- Alternative SQL-style approach would be similar in complexity.
- For very large datasets, this approach is efficient as it requires only one pass through the data.
- Trade-off: pandas dependency required, but typical for DataFrame manipulation problems.

## Approach: Iterative (Implemented)

### Strategy

The solution uses iterative to solve the problem efficiently.

```python
  counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
  result = counts[counts['cooperation_count'] >= 3][['actor_id', 'director_id']]
  ```

### How It Works

- Alternative SQL-style approach would be similar in complexity.
- For very large datasets, this approach is efficient as it requires only one pass through the data.
- Trade-off: pandas dependency required, but typical for DataFrame manipulation problems.

### Why Iterative Works

- `groupby(['actor_id', 'director_id'])` groups rows by unique actor-director pairs.
- `.size()` counts the number of rows in each group, representing cooperation count.
- Boolean filtering `counts['cooperation_count'] >= 3` selects only qualifying pairs.
- Column selection `[['actor_id', 'director_id']]` ensures the result has the required format.

Time complexity

- Let n = number of rows in the DataFrame.
- Groupby operation costs O(n) for scanning all rows and creating groups.
- Size calculation is O(n) as it counts all rows.
- Filtering is O(k) where k is the number of unique pairs.
- Overall time complexity: O(n).

Space complexity

- The groupby operation creates intermediate data structures storing unique pairs and their counts: O(k) where k is the number of unique actor-director pairs.
- Result DataFrame stores only qualifying pairs: O(m) where m <= k.
- Overall space complexity: O(k).

Thought process and trade-offs

- Pandas approach: simple, readable, and leverages built-in optimizations for grouping and aggregation.
- Alternative SQL-style approach would be similar in complexity.
- For very large datasets, this approach is efficient as it requires only one pass through the data.
- Trade-off: pandas dependency required, but typical for DataFrame manipulation problems.

### Complexity Analysis

- **Time Complexity**: - Let n = number of rows in the DataFrame. - Groupby operation costs O(n) for scanning all rows and creating groups. - Size calculation is O(n) as it counts all rows. - Filtering is O(k) where k is the number of unique pairs. - Overall time complexity: O(n). Space complexity - The groupby operation creates intermediate data structures storing unique pairs and their counts: O(k) where k is the number of unique actor-director pairs. - Result DataFrame stores only qualifying pairs: O(m) where m <= k. - Overall space complexity: O(k). Thought process and trade-offs - Pandas approach: simple, readable, and leverages built-in optimizations for grouping and aggregation. - Alternative SQL-style approach would be similar in complexity. - For very large datasets, this approach is efficient as it requires only one pass through the data. - Trade-off: pandas dependency required, but typical for DataFrame manipulation problems.
- **Space Complexity**: - The groupby operation creates intermediate data structures storing unique pairs and their counts: O(k) where k is the number of unique actor-director pairs. - Result DataFrame stores only qualifying pairs: O(m) where m <= k. - Overall space complexity: O(k). Thought process and trade-offs - Pandas approach: simple, readable, and leverages built-in optimizations for grouping and aggregation. - Alternative SQL-style approach would be similar in complexity. - For very large datasets, this approach is efficient as it requires only one pass through the data. - Trade-off: pandas dependency required, but typical for DataFrame manipulation problems.

### Advantages

- Efficient iterative solution
- Clear and maintainable code

### Disadvantages

- May require additional space
