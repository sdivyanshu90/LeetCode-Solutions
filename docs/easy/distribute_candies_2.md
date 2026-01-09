# Distribute Candies to People

## Problem Summary

Distribute `candies` to `num_people` in rounds. In each round, give increasing amounts: 1 candy to first person, 2 to second, etc. Continue until candies run out. Return final candy counts.

**Example**: `candies=7, num_people=4` → `[1,2,3,1]`

- Round 1: give 1,2,3,1 (used 7, none left)

## Approach: Frequency Counting (Implemented)

### Strategy

The solution uses frequency counting to solve the problem efficiently.

```python
def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    res = [0] * num_people
    idx = 0
    i = 1

    while candies > 0:
        res[idx] += min(candies, i)
        idx = (idx + 1) % len(res)
        candies -= i
        i += 1
    return res
```

### How It Works

The algorithm simulates giving candies round by round:

1. **Initialize**: Array of zeros for each person, index pointer, candy counter starting at 1
2. **While candies remain**:
   - Give `min(candies, i)` to current person (handles running out mid-round)
   - Move to next person (wrapping with modulo)
   - Decrement remaining candies
   - Increment candy amount for next distribution
3. **Return** final distribution

**Example** for `candies=10, num_people=3`:

```
Initial: res=[0,0,0], candies=10, i=1

Turn 1: res[0]+=min(10,1)=1 → [1,0,0], candies=9, i=2
Turn 2: res[1]+=min(9,2)=2 → [1,2,0], candies=7, i=3
Turn 3: res[2]+=min(7,3)=3 → [1,2,3], candies=4, i=4
Turn 4: res[0]+=min(4,4)=4 → [5,2,3], candies=0, i=5
Result: [5,2,3]
```

### Why Frequency Counting Works

- **Simulation approach**: Directly models the distribution process
- **Modulo arithmetic**: `(idx + 1) % len(res)` handles circular wrapping
- **min() handles remainder**: When candies < i, gives remaining candies instead of full amount
- **Accumulation**: `+=` allows multiple rounds per person

### Complexity Analysis

- **Time Complexity**: O(√candies) because the sum 1+2+3+...+k = k(k+1)/2 = candies, so k ≈ √(2\*candies). The loop runs k times.
- **Space Complexity**: O(num_people) for the result array. O(1) auxiliary space.

### Advantages

- Efficient frequency counting solution
- Clear and maintainable code

### Disadvantages

- May require additional space
