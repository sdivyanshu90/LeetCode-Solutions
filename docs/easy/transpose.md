# Transpose Matrix

## Problem Summary

Given a 2D integer array `matrix`, return the transpose of the matrix. The transpose swaps rows and columns: element at position `matrix[i][j]` becomes `matrix[j][i]`.

**Example**: `[[1,2,3],[4,5,6]]` → `[[1,4],[2,5],[3,6]]`

## Current Implementation

The solution iterates through columns and builds new rows from them:

```python
def transpose(self, matrix):
    res = []

    for col in range(len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        res.append(temp)
    return res
```

## How It Works

The algorithm constructs the transpose by converting columns to rows:

1. **Outer loop**: Iterate through each column index
2. **Inner loop**: For each column, iterate through rows to collect values
3. **Build new row**: Collect all `matrix[row][col]` values (forming a column from original)
4. **Add to result**: This becomes a row in the transposed matrix

**Example** for `[[1,2,3],[4,5,6]]`:

```
Original: 2 rows × 3 columns
Row 0: [1, 2, 3]
Row 1: [4, 5, 6]

Transpose: 3 rows × 2 columns
col=0: collect [matrix[0][0], matrix[1][0]] = [1, 4]
col=1: collect [matrix[0][1], matrix[1][1]] = [2, 5]
col=2: collect [matrix[0][2], matrix[1][2]] = [3, 6]

Result: [[1,4],[2,5],[3,6]]
```

## Why This Works

- **Definition of transpose**: Element (i,j) becomes (j,i)
- **Column-to-row mapping**: Each original column becomes a row in result
- **Nested loop pattern**: Naturally captures the 2D iteration needed

## Time Complexity

O(m \* n) where m is number of rows and n is number of columns. Must visit every element exactly once.

## Space Complexity

O(m \* n) for the result matrix. Uses O(1) auxiliary space beyond the output.

## Trade-offs

- **Clear logic**: Explicit nested loops make the transformation obvious
- **Readable**: Easy to trace and verify correctness
- **Standard approach**: Common pattern for matrix operations
- **Pythonic alternative**: Could use list comprehension or zip:

  ```python
  # Using list comprehension
  return [[matrix[row][col] for row in range(len(matrix))]
          for col in range(len(matrix[0]))]

  # Using zip (most Pythonic)
  return list(map(list, zip(*matrix)))
  ```

  The `zip(*matrix)` unpacks rows and zips them into columns - very concise!
