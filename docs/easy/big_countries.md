# Big Countries

Problem summary

- Given a DataFrame `world` with country information including area and population.
- Find countries that have area >= 3,000,000 km² OR population >= 25,000,000.
- Return columns: name, population, and area.

Current implementation (in repository)

- Implementation uses pandas boolean filtering:
  - Uses `.loc[]` with a compound condition combining area and population criteria.
  - Applies OR logic using `|` operator between the two conditions.
  - Selects only the required columns: name, population, and area.
- Example code:
  ```python
  filtered_countries = world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
  return filtered_countries[['name','population','area']]
  ```

Why this works

- Boolean indexing in pandas evaluates the condition for each row.
- OR operator `|` returns True if either condition is met.
- `.loc[]` filters rows where the condition is True.
- Column selection `[['name','population','area']]` returns only specified columns.

Time complexity

- Let n = number of rows in the DataFrame.
- Evaluating boolean conditions: O(n) for checking each row.
- Filtering rows: O(n) for selecting matching rows.
- Column selection: O(n) for copying selected columns.
- Overall time complexity: O(n).

Space complexity

- Result DataFrame contains m rows where m <= n (filtered subset).
- Each row has 3 columns (name, population, area).
- Space complexity: O(m).

Thought process and trade-offs

- Pandas vectorized operations: efficient and readable for DataFrame manipulation.
- Single-pass filtering: evaluates both conditions simultaneously.
- Alternative SQL approach: `SELECT name, population, area FROM world WHERE area >= 3000000 OR population >= 25000000`.
- Trade-off: pandas dependency required, but standard for data manipulation in Python.
- Could optimize by short-circuit evaluation if one condition is much more selective, but pandas handles this efficiently.
