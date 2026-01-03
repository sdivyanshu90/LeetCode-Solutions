# Article Views (SQL/Pandas)

## Problem Summary

Given a DataFrame `views` with columns `author_id` and `viewer_id`, find all authors who viewed their own articles. Return their IDs sorted in ascending order.

## Current Implementation

The solution uses pandas filtering and deduplication:

```python
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    same_author_viewer = views[views['author_id'] == views['viewer_id']]
    result = same_author_viewer[['author_id']].drop_duplicates().sort_values(by='author_id')
    result.rename(columns={'author_id': 'id'}, inplace=True)
    return result
```

## How It Works

The algorithm performs sequential DataFrame operations:

1. **Filter self-views**: `views['author_id'] == views['viewer_id']` creates boolean mask for rows where author viewed their own article
2. **Select column**: Extract only `author_id` column
3. **Remove duplicates**: `drop_duplicates()` ensures each author appears once
4. **Sort**: `sort_values()` orders by author_id ascending
5. **Rename**: Change column name from `author_id` to `id` for output format

**SQL equivalent**:

```sql
SELECT DISTINCT author_id AS id
FROM views
WHERE author_id = viewer_id
ORDER BY id ASC
```

## Why This Works

- **Boolean indexing**: Efficiently filters rows matching condition
- **Chained operations**: Pandas supports fluent method chaining
- **Deduplication**: Handles authors who viewed their articles multiple times
- **Rename for output**: Matches expected schema

## Time Complexity

O(n log n) where n is the number of rows. The filtering is O(n), but sorting dominates at O(n log n).

## Space Complexity

O(k) where k is the number of unique self-viewing authors (result size).

## Trade-offs

- **Readable**: Clear step-by-step DataFrame transformations
- **Pandas idioms**: Uses standard DataFrame methods
- **Could optimize**: Combine operations for slight efficiency gain:
  ```python
  return (views[views['author_id'] == views['viewer_id']]
          [['author_id']].drop_duplicates()
          .sort_values(by='author_id')
          .rename(columns={'author_id': 'id'}))
  ```
- **SQL comparison**: For very large datasets, database query might be more efficient than in-memory pandas operations
