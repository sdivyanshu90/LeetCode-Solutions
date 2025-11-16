# Delete Duplicate Emails

Problem summary

- Given a pandas DataFrame `person` with at least columns `id` and `email`, remove duplicate rows that share the same `email`, keeping the row with the smallest `id`.
- The provided function mutates the input DataFrame in-place.

Approach implemented

- Sort the DataFrame by `id` in ascending order: person.sort_values(by='id', inplace=True)
- Drop duplicate emails keeping the first occurrence (which after the sort has the smallest id):
  person.drop_duplicates(subset='email', keep='first', inplace=True)
- This keeps one row per email (the row with the minimum id).

Behavior details / important notes

- In-place mutation: The function modifies the passed DataFrame object and returns None.
- Case-sensitivity: The operation treats email strings as-is. 'a@b.com' and 'A@b.com' are considered different unless normalized beforehand.
- Column requirements: The function expects `id` and `email` columns to exist. If missing, pandas will raise a KeyError.
- Index handling: Sorting and dropping preserve original rows but do not reset the index. Callers can reset the index afterwards if needed.

Time and space complexity

- Sorting: O(m log m) time and O(m) extra memory (where m = number of rows).
- drop_duplicates: O(m) time on average (hash-based) and O(m) auxiliary memory for tracking seen keys.
- Overall: O(m log m) time dominated by sort; O(m) extra space.

Edge cases and robustness

- Empty DataFrame: function returns immediately (no changes).
- Single row: unchanged.
- All rows share same email: after operation only the row with smallest id remains.
- Additional columns: preserved for the kept rows.
- If `id` values are not unique, sorting still places rows in some deterministic order (ties arbitrary unless further tie-breakers provided).
- If case-insensitive deduplication is required, normalize emails first, e.g., person['email_norm'] = person['email'].str.lower() and use that column for drop_duplicates.

Testing summary (as included in test function)

- Basic duplicate scenarios, no-duplicate scenarios, all-duplicates, empty DataFrame, single-row, multiple duplicate groups, already sorted ids, reverse-sorted ids, extra columns, and case-sensitivity checks. Expected outcomes verify that the smallest id per email is kept.

Recommended improvements / alternatives

- Return a new DataFrame instead of mutating in-place for safer functional behavior:
  df_out = person.sort_values('id').drop_duplicates('email', keep='first').reset_index(drop=True)
- If you need case-insensitive deduplication:
  person['email_lower'] = person['email'].str.lower()
  person.sort_values('id', inplace=True)
  person.drop_duplicates(subset='email_lower', keep='first', inplace=True)
  person.drop(columns='email_lower', inplace=True)
- If performance matters and the DataFrame is already sorted by `id`, skip the sort step.
