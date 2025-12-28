# Min Cost Climbing Stairs

Problem summary

- Array cost where cost[i] is the cost of ith step on a staircase.
- Can start from step 0 or step 1, and climb 1 or 2 steps at a time.
- Find minimum cost to reach the top (beyond last step).
- Example: [10,15,20] -> start at 1 (cost 15), step to top -> 15.

Current implementation (in repository)

- Implementation uses dynamic programming with O(1) space:
  - Tracks minimum cost to reach previous two steps (dp1, dp2).
  - For each step, calculates cost = current step cost + min of previous two.
  - Updates dp1 and dp2 for next iteration (rolling variables).
  - Returns minimum of last two values (can reach top from either).
- Example code:
  ```python
  dp1 = cost[0]
  dp2 = cost[1]
  for i in range(2, len(cost)):
      dp0 = cost[i] + min(dp1, dp2)
      dp1 = dp2
      dp2 = dp0
  return min(dp2, dp1)
  ```

Why this works

- DP recurrence: cost to reach step i = cost[i] + min(cost to reach i-1, cost to reach i-2).
- Rolling variables avoid storing entire DP array.
- Starting with cost[0] and cost[1]: both can be starting positions (no cost to reach them initially).
- Final answer: min of reaching last two steps, as you can step beyond from either.

Time complexity

- Let n = length of cost array.
- Single pass through array: O(n).
- Overall time complexity: O(n).

Space complexity

- Only three variables (dp0, dp1, dp2).
- Space complexity: O(1).

Thought process and trade-offs

- Space-optimized DP: classic pattern for linear DP problems.
- Alternative: use array dp[i] for all steps - O(n) space, same time complexity.
- Current approach: optimal for both time and space.
- Key insight: only need previous two values, not entire history.
- Edge case: returning min(dp2, dp1) handles reaching top from either last step.
