# Day of the Year

## Problem Summary

Given a date string in the format `YYYY-MM-DD`, return the day number of the year (1-366).

**Example**: `"2019-02-10"` → `41` (31 days in Jan + 10 days in Feb)

## Approach: String Manipulation (Implemented)

### Strategy

The solution uses string manipulation to solve the problem efficiently.

```python
def dayOfYear(self, date: str) -> int:
    month_dates = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_dates_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

    split_date = [int(i) for i in date.split("-")]
    tes = split_date[1] % 12
    if split_date[0] % 400 == 0 or (split_date[0] % 4 == 0 and split_date[0] % 100 != 0):
        return (sum(month_dates_leap[:tes - 1]) + split_date[2])
    else:
        return (sum(month_dates[:tes - 1]) + split_date[2])
```

### How It Works

The algorithm determines leap year status and sums days:

1. **Parse date**: Split string into year, month, day integers
2. **Leap year check**:
   - Divisible by 400, OR
   - Divisible by 4 AND NOT divisible by 100
3. **Sum previous months**: Use appropriate array (leap or regular)
4. **Add current day**: Add the day of current month

**Example** for `"2020-03-01"` (leap year):

```
Year: 2020 (divisible by 4, not by 100) → leap year
Month: 3 (March)
Day: 1

Sum of Jan-Feb in leap year: 31 + 29 = 60
Add current day: 60 + 1 = 61
```

### Why String Manipulation Works

- **Leap year rules**: Correctly implements Gregorian calendar rules
- **Precomputed days**: Arrays store days per month for quick lookup
- **Cumulative sum**: Adding previous months gives offset to current month

### Complexity Analysis

- **Time Complexity**: O(m) where m is the month number (at most 12). The sum operation is O(m) for slicing and summing previous months.
- **Space Complexity**: O(1) - uses fixed-size arrays regardless of input.

### Advantages

- Efficient string manipulation solution
- Clear and maintainable code

### Disadvantages

- May require additional space
