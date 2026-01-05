# Distance Between Bus Stops

## Problem Summary

A bus travels in a circular route with `n` stops. Given an array `distance` where `distance[i]` is the distance from stop `i` to stop `(i+1) % n`, and two stops `start` and `destination`, return the shortest distance between them.

**Example**: `distance=[1,2,3,4]`, `start=0`, `destination=2` → `3` (clockwise: 1+2=3, counterclockwise: 4+3=7, min=3)

## Current Implementation

The solution calculates both clockwise and counterclockwise distances:

```python
def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    if start > destination:
        start, destination = destination, start

    clockwise_distance = 0
    anticlockwise_distance = 0
    total_distance = sum(distance)

    for i in range(start, destination):
        clockwise_distance += distance[i]

    anticlockwise_distance = total_distance - clockwise_distance

    return min(clockwise_distance, anticlockwise_distance)
```

## How It Works

The algorithm computes both possible paths:

1. **Normalize**: Ensure `start < destination` by swapping if needed
2. **Calculate total**: Sum all distances in the circle
3. **Clockwise distance**: Sum from `start` to `destination` (forward)
4. **Counterclockwise**: `total - clockwise` (going the other way around)
5. **Return minimum** of the two distances

**Example** for `distance=[1,2,3,4]`, `start=0`, `destination=3`:

```
Total: 1+2+3+4 = 10
Clockwise (0→1→2→3): 1+2+3 = 6
Counterclockwise (0→3 going backwards): 10-6 = 4
Result: min(6, 4) = 4
```

## Why This Works

- **Circular property**: Only two paths exist between any two points on a circle
- **Complementary distances**: The two paths together equal the full circle
- **Normalization**: Swapping ensures consistent direction calculation
- **Simple subtraction**: Total minus one path gives the other path

## Time Complexity

O(n) where n is the number of stops. Computing total is O(n), and the loop for clockwise distance is O(destination - start) ≤ O(n).

## Space Complexity

O(1) - only uses a few variables for accumulation.

## Trade-offs

- **Clear logic**: Easy to understand two-path comparison
- **Efficient**: Single pass to compute total, partial sum for clockwise
- **Alternative**: Could calculate both paths explicitly without using complement:
  ```python
  clockwise = sum(distance[i % n] for i in range(start, destination))
  counter = sum(distance[i % n] for i in range(destination, start + n))
  return min(clockwise, counter)
  ```
  But current approach is more efficient (avoids second loop).
