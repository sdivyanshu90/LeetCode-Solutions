# Best Time to Buy and Sell Stock

## Problem Summary

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**LeetCode Problem**: [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Approach 1: One Pass with Min Tracking (Implemented)

### Strategy

The implemented solution uses a **single-pass greedy approach**:

1. Track the minimum price seen so far
2. For each price, calculate the potential profit if we sold at that price
3. Update the maximum profit if current profit is higher
4. Update the minimum price if current price is lower
5. Return the maximum profit found

**Code**:

```python
def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit
```

### How It Works

**Example**: `prices = [7, 1, 5, 3, 6, 4]`

```
Day 0: price=7
  - min_price = 7
  - max_profit = 0

Day 1: price=1
  - profit = 1 - 7 = -6
  - max_profit = max(0, -6) = 0
  - min_price = min(7, 1) = 1

Day 2: price=5
  - profit = 5 - 1 = 4
  - max_profit = max(0, 4) = 4
  - min_price = min(1, 5) = 1

Day 3: price=3
  - profit = 3 - 1 = 2
  - max_profit = max(4, 2) = 4
  - min_price = min(1, 3) = 1

Day 4: price=6
  - profit = 6 - 1 = 5
  - max_profit = max(4, 5) = 5
  - min_price = min(1, 6) = 1

Day 5: price=4
  - profit = 4 - 1 = 3
  - max_profit = max(5, 3) = 5
  - min_price = min(1, 4) = 1

Result: 5 (buy at 1, sell at 6)
```

### Key Insight

At each day, we have two choices:

1. **Buy**: Check if this is the lowest price so far
2. **Sell**: Check if selling at current price (having bought at lowest price so far) gives maximum profit

We don't need to track when we buy or sell - just track the minimum price and maximum profit.

### Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(1) - Only two variables

### Edge Cases Handled

- **Single price**: `[5]` → 0 (cannot sell on same day)
- **Decreasing prices**: `[7,6,4,3,1]` → 0 (no profitable transaction)
- **Increasing prices**: `[1,2,3,4,5]` → 4 (buy first, sell last)
- **Best day at end**: Works correctly
- **Best day in middle**: Works correctly

## Approach 2: Brute Force (Not Recommended)

Check all possible buy-sell pairs:

```python
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit
```

### Complexity

- **Time**: O(n²) - Nested loops
- **Space**: O(1)

### Why Not Use This

- Much slower than O(n) solution
- Inefficient for large arrays
- No advantage over single-pass approach

## Approach 3: Kadane's Algorithm Variant

Treat as maximum subarray problem:

```python
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
```

### How It Works

- Convert prices to daily profit differences
- Find maximum sum of consecutive differences
- This is essentially Kadane's algorithm applied to stock prices

### Complexity

- **Time**: O(n)
- **Space**: O(1)

### Relation to Maximum Subarray

The problem can be reformulated as:

- Daily changes: `[prices[i+1] - prices[i] for i in range(n-1)]`
- Find maximum sum of consecutive changes
- This gives the best buy-sell window

## Approach 4: Dynamic Programming

Explicit DP formulation:

```python
def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    # dp[i] = max profit we can get by day i
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i-1], prices[i] - min_price)

    return dp[n-1]
```

### Space Optimization

Since we only need previous DP value, we can optimize to O(1) space:

```python
# This reduces to the implemented solution
```

### Complexity

- **Time**: O(n)
- **Space**: O(n) for array, but can be optimized to O(1)

## Comparison of Approaches

| Approach              | Time  | Space  | Pros                               | Cons                     |
| --------------------- | ----- | ------ | ---------------------------------- | ------------------------ |
| One Pass Min Tracking | O(n)  | O(1)   | Optimal, simple, clear             | None                     |
| Brute Force           | O(n²) | O(1)   | Easy to understand                 | Too slow                 |
| Kadane's Variant      | O(n)  | O(1)   | Elegant connection to max subarray | Less direct              |
| Dynamic Programming   | O(n)  | O(1)\* | Formal approach                    | More complex than needed |

\*Can be optimized from O(n)

## Mathematical Insight

### Why One Pass Works

The key observation is:

- To maximize profit, we want: `max(prices[j] - prices[i])` where `j > i`
- This is equivalent to: `max(prices[j]) - min(prices[i])` for `i < j`
- We can track `min_price` as we go and compute `price - min_price` at each step

**Proof of correctness**:

- At day `i`, `min_price` is the minimum of `prices[0...i]`
- `price - min_price` is the best profit if we sell on day `i`
- By checking this for all days, we find the overall maximum profit

### Connection to Maximum Subarray

If we compute daily differences: `diff[i] = prices[i+1] - prices[i]`

Then: `profit = prices[sell] - prices[buy] = sum(diff[buy:sell])`

Finding max profit = finding maximum sum subarray in `diff`, which is Kadane's algorithm.

## Edge Cases & Considerations

1. **Single Price**:

   - `[5]` → 0
   - Cannot buy and sell on same day
   - Loop starts from index 1, so no iterations if only 1 element

2. **Strictly Decreasing**:

   - `[7, 6, 4, 3, 1]` → 0
   - All profits are negative
   - `max_profit` stays 0 (initialized value)

3. **Strictly Increasing**:

   - `[1, 2, 3, 4, 5]` → 4
   - Best: buy first, sell last
   - `min_price` stays at 1, max profit is 5-1=4

4. **V-Shaped**:

   - `[9, 1, 5, 3, 6, 4]` → 5
   - Minimum in middle, maximum after
   - Correctly identifies buy at 1, sell at 6

5. **Peak in Middle**:

   - `[2, 4, 1, 5, 3]` → 4
   - Multiple local maxima
   - Correctly finds buy at 1, sell at 5

6. **All Same Prices**:

   - `[3, 3, 3, 3]` → 0
   - No profit possible
   - Works correctly

7. **Two Prices**:
   - `[3, 5]` → 2 (profit = 5-3)
   - `[5, 3]` → 0 (no profit)
   - Both handled correctly

## Common Pitfalls

1. **Not Initializing max_profit to 0**:

   ```python
   # WRONG: Might return negative profit
   max_profit = float('-inf')

   # CORRECT: Profit can't be negative (we can choose not to trade)
   max_profit = 0
   ```

2. **Updating min_price Before Calculating Profit**:

   ```python
   # WRONG: Might buy and sell on same day
   min_price = min(min_price, price)
   profit = price - min_price

   # CORRECT: Calculate profit first, then update min
   profit = price - min_price
   max_profit = max(max_profit, profit)
   min_price = min(min_price, price)
   ```

3. **Allowing Same Day Buy/Sell**:

   - Must buy before selling
   - Starting loop from `prices[1:]` ensures this

4. **Not Handling Empty Array**:

   ```python
   # Implemented solution assumes non-empty array
   # If needed, add check:
   if not prices:
       return 0
   ```

5. **Trying to Track Buy/Sell Days**:
   - Problem only asks for maximum profit, not when to trade
   - Don't complicate by tracking indices unnecessarily

## Optimization Notes

The implemented solution is **optimal**:

- O(n) time - must examine each price at least once
- O(1) space - only two variables
- Single pass - no backtracking needed
- Early intuition and simple logic

No further optimization possible for this problem.

## Why This Approach is Elegant

The solution is a perfect example of **greedy algorithm**:

1. **Local decision**: At each step, update min price and max profit
2. **Global optimum**: These local decisions lead to the global maximum profit
3. **Simplicity**: Only two variables and one loop

The key insight is that we don't need to know when we bought or sold - just the minimum price seen so far and the maximum profit achievable.

## Visual Example

```
Prices: [7, 1, 5, 3, 6, 4]

Graph:
7 ●
6 │                 ●
5 │         ●
4 │                     ●
3 │             ●
2 │
1 │     ●
0 └─────────────────────
  0  1  2  3  4  5  Day

Strategy:
- Buy at lowest point (1 on day 1)
- Sell at highest point after that (6 on day 4)
- Profit: 6 - 1 = 5

Algorithm tracks:
- min_price moves: 7 → 1 → 1 → 1 → 1 → 1
- max_profit moves: 0 → 0 → 4 → 4 → 5 → 5
```

## Test Cases

```python
# Example from problem
maxProfit([7,1,5,3,6,4])          # 5 (buy at 1, sell at 6)

# No profit possible
maxProfit([7,6,4,3,1])            # 0 (prices only decrease)

# Single day
maxProfit([5])                    # 0 (can't trade on same day)

# Increasing prices
maxProfit([1,2,3,4,5])            # 4 (buy at 1, sell at 5)

# Two prices - profit
maxProfit([1,2])                  # 1 (buy at 1, sell at 2)

# Two prices - no profit
maxProfit([2,1])                  # 0 (price decreases)

# V-shaped
maxProfit([9,1,5,3,6,4])          # 5 (buy at 1, sell at 6)

# Multiple peaks
maxProfit([2,4,1,5,3])            # 4 (buy at 1, sell at 5)

# All same
maxProfit([3,3,3,3])              # 0 (no change in price)

# Large numbers
maxProfit([10000,1,10000])        # 9999 (buy at 1, sell at 10000)

# Best at very end
maxProfit([3,2,6,5,0,3,10])       # 10 (buy at 0, sell at 10)
```

## Thought Process

The problem asks for maximum profit from a single buy-sell transaction.

**Observations**:

1. Must buy before selling (no short selling)
2. Want to maximize: `prices[sell_day] - prices[buy_day]`
3. This is: `max_price_after_day_i - min_price_before_day_i`

**Naive approach**: Try all buy-sell pairs → O(n²)

**Optimization insight**:

- For each day, the best buy price is the **minimum price seen so far**
- Calculate potential profit: `current_price - min_price_so_far`
- Track the maximum profit across all days

**Key realization**:

- We don't need to track when we buy/sell
- Just track minimum price and maximum profit
- Single pass is sufficient

This leads to the elegant O(n) solution with O(1) space.

## Related Problems

- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Multiple transactions)
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (At most 2 transactions)
- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) (At most k transactions)
- [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Related algorithm)
