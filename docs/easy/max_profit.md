# Best Time to Buy and Sell Stock

## Problem Summary

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**LeetCode Problem**: [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**LeetCode Problem**: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Approach: Dynamic Programming (Implemented)

### Strategy

The solution uses dynamic programming to solve the problem efficiently.

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

### Why Dynamic Programming Works

The dynamic programming approach is effective for this problem.

### Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Advantages

- Efficient dynamic programming solution
- Clear and maintainable code

### Disadvantages

- May require additional space
