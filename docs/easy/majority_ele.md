# Majority Element

## Problem Summary

Given an array `nums` of size `n`, return the **majority element**. The majority element is the element that appears **more than ⌊n/2⌋ times**. You may assume that the majority element always exists in the array.

**LeetCode Problem**: [169. Majority Element](https://leetcode.com/problems/majority-element/)

## Approach 1: Hash Map with Early Return (Implemented)

### Strategy

The implemented solution uses a **hash map with early termination**:

1. Use a hash map (defaultdict) to count occurrences of each element
2. As we count, check if current element's count exceeds n/2
3. Return immediately when we find the majority element (early exit optimization)

**Code**:

```python
def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    H = defaultdict(int)
    for i in range(n):
        H[nums[i]] += 1

        if H[nums[i]] > n / 2:
            return nums[i]
```

### How It Works

**Example**: `nums = [2, 2, 1, 1, 1, 2, 2]`

```
n = 7, threshold = 7/2 = 3.5

Index 0: nums[0]=2
  - H = {2: 1}
  - 1 > 3.5? No

Index 1: nums[1]=2
  - H = {2: 2}
  - 2 > 3.5? No

Index 2: nums[2]=1
  - H = {2: 2, 1: 1}
  - 1 > 3.5? No

Index 3: nums[3]=1
  - H = {2: 2, 1: 2}
  - 2 > 3.5? No

Index 4: nums[4]=1
  - H = {2: 2, 1: 3}
  - 3 > 3.5? No

Index 5: nums[5]=2
  - H = {2: 3, 1: 3}
  - 3 > 3.5? No

Index 6: nums[6]=2
  - H = {2: 4, 1: 3}
  - 4 > 3.5? Yes!
  - Return 2
```

### Complexity Analysis

- **Time Complexity**: O(n) - Single pass through array
  - Best case: O(n/2 + 1) when majority element is found early
  - Worst case: O(n) when majority element is at the end
- **Space Complexity**: O(n) - Hash map stores at most n elements

### Edge Cases Handled

- **Single element**: `[1]` → 1 (immediately found)
- **All same**: `[5,5,5,5]` → 5 (found after n/2+1 elements)
- **Bare majority**: `[1,2,1,3,1,1]` → 1 (exactly more than n/2)
- **Negative numbers**: `[-1,-1,2]` → -1 (works with any integer)
- **Large numbers**: Handles any integer values

## Approach 2: Sorting (Commented in Code)

Sort the array and return the middle element:

```python
def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n//2]
```

### How It Works

Since the majority element appears more than n/2 times, after sorting, it **must** occupy the middle position.

**Example**: `nums = [2, 2, 1, 1, 1, 2, 2]`

```
Sorted: [1, 1, 1, 2, 2, 2, 2]
         0  1  2  3  4  5  6
Middle index: 7//2 = 3
nums[3] = 2 ✓
```

**Why this works**:

- If majority element appears > n/2 times, it occupies > n/2 positions
- In a sorted array, these positions must include the middle index
- Example with n=7: Element appears ≥4 times, so it spans the middle

### Complexity

- **Time**: O(n log n) - Sorting dominates
- **Space**: O(1) or O(n) depending on sorting algorithm

### Advantages

- Simple and elegant
- No extra hash map needed
- Guaranteed to work due to mathematical property

### Disadvantages

- Slower than hash map approach
- Modifies the input array (unless you copy it)

## Approach 3: Boyer-Moore Voting Algorithm (Optimal)

The **most efficient** solution using constant space:

```python
def majorityElement(self, nums: List[int]) -> int:
    candidate = None
    count = 0

    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
```

### How It Works

The algorithm maintains a candidate and a count:

1. If count is 0, set current element as candidate
2. If current element equals candidate, increment count
3. If current element differs from candidate, decrement count
4. The surviving candidate is the majority element

**Example**: `nums = [2, 2, 1, 1, 1, 2, 2]`

```
num=2: count=0 → candidate=2, count=1
num=2: count=1 → candidate=2, count=2
num=1: count=2 → candidate=2, count=1 (different, decrement)
num=1: count=1 → candidate=2, count=0 (different, decrement)
num=1: count=0 → candidate=1, count=1 (new candidate)
num=2: count=1 → candidate=1, count=0 (different, decrement)
num=2: count=0 → candidate=2, count=1 (new candidate)

Final: candidate=2 ✓
```

### Why This Works

**Intuition**: Imagine a battle where each element fights against different elements:

- Same elements support the candidate (count++)
- Different elements oppose the candidate (count--)
- The majority element will survive because it appears more than all others combined

**Mathematical proof**:

- Majority element appears > n/2 times
- All other elements combined appear < n/2 times
- Even if all other elements "cancel out" the majority element, the majority still has votes left

### Complexity

- **Time**: O(n) - Single pass
- **Space**: O(1) - Only two variables

### This is the Optimal Solution!

- Best time complexity: O(n)
- Best space complexity: O(1)
- No sorting required
- No hash map required
- Elegant algorithm

## Approach 4: Randomization

Randomly pick elements until finding the majority:

```python
import random

def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    while True:
        candidate = random.choice(nums)
        count = sum(1 for num in nums if num == candidate)
        if count > n // 2:
            return candidate
```

### Expected Complexity

- **Time**: O(n) expected - Probability of picking majority > 1/2, so few iterations
- **Space**: O(1)

### Drawbacks

- Non-deterministic
- Not suitable for interviews
- Theoretically interesting but impractical

## Approach 5: Divide and Conquer

Recursively find majority in subarrays:

```python
def majorityElement(self, nums: List[int]) -> int:
    def majority_helper(lo, hi):
        # Base case
        if lo == hi:
            return nums[lo]

        # Recurse on left and right halves
        mid = (lo + hi) // 2
        left_maj = majority_helper(lo, mid)
        right_maj = majority_helper(mid + 1, hi)

        # If same, that's the majority
        if left_maj == right_maj:
            return left_maj

        # Count occurrences in range
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left_maj)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right_maj)

        return left_maj if left_count > right_count else right_maj

    return majority_helper(0, len(nums) - 1)
```

### Complexity

- **Time**: O(n log n) - Divide and conquer with linear merge
- **Space**: O(log n) - Recursion stack

### Not Recommended

- More complex
- Slower than hash map or Boyer-Moore
- Good for understanding divide and conquer, not for this problem

## Comparison of Approaches

| Approach               | Time          | Space    | Pros                      | Cons                   |
| ---------------------- | ------------- | -------- | ------------------------- | ---------------------- |
| Hash Map (Implemented) | O(n)          | O(n)     | Simple, early termination | Extra space            |
| Sorting                | O(n log n)    | O(1)\*   | Elegant, simple           | Slower, modifies input |
| Boyer-Moore            | O(n)          | O(1)     | Optimal, no extra space   | Less intuitive         |
| Randomization          | O(n) expected | O(1)     | Interesting               | Non-deterministic      |
| Divide & Conquer       | O(n log n)    | O(log n) | Educational               | Complex, slower        |

\*Depends on sorting implementation

## Edge Cases & Considerations

1. **Single Element**:

   - `[1]` → 1
   - Element is the majority by definition
   - All approaches handle correctly

2. **All Same Elements**:

   - `[7,7,7,7,7]` → 7
   - First element found immediately in hash map approach
   - Boyer-Moore never changes candidate

3. **Bare Majority (exactly > n/2)**:

   - `[1,2,1,3,1,1]` → 1 (4 out of 6)
   - Count is 4, threshold is 3 (6/2)
   - Still counts as majority

4. **Two Elements**:

   - `[1,1]` → 1
   - Works correctly

5. **Majority at End**:

   - `[1,2,3,3,3,3,3]` → 3
   - Hash map must scan entire array
   - Boyer-Moore still O(n)

6. **Negative Numbers**:

   - `[-1,-1,2]` → -1
   - All approaches handle negative values

7. **Large Numbers**:
   - Works with any integer in valid range

## Common Pitfalls

1. **Off-by-One in Threshold**:

   ```python
   # WRONG: >= instead of >
   if H[nums[i]] >= n / 2:
       return nums[i]

   # CORRECT: Must be GREATER than n/2
   if H[nums[i]] > n / 2:
       return nums[i]
   ```

2. **Integer Division vs Float Division**:

   ```python
   # Both work, but be consistent
   if count > n // 2:  # Integer comparison
   if count > n / 2:   # Float comparison (implemented version)
   ```

3. **Not Handling Empty Array**:

   - Problem guarantees non-empty array
   - But good practice to check

4. **Modifying Input in Sorting Approach**:

   ```python
   # WRONG: Modifies original array
   nums.sort()

   # BETTER: Copy if needed
   sorted_nums = sorted(nums)
   ```

5. **Forgetting Early Return in Hash Map**:

   ```python
   # Less efficient: counts everything then finds max
   for num in nums:
       H[num] += 1
   return max(H, key=H.get)

   # Better: early return (implemented)
   for num in nums:
       H[num] += 1
       if H[num] > n / 2:
           return num
   ```

## Optimization Notes

**Implemented approach (Hash Map)**:

- Good balance of simplicity and efficiency
- O(n) time is optimal
- Early termination is a nice optimization
- O(n) space is acceptable

**Best approach (Boyer-Moore)**:

- O(n) time, O(1) space
- Optimal in both dimensions
- Should be known for interviews

**Trade-offs**:

- Hash map: Easier to understand, uses space
- Boyer-Moore: Optimal, but requires understanding the algorithm
- Sorting: Simple but slower

For interviews, know both hash map and Boyer-Moore approaches.

## Visual Example: Boyer-Moore

```
nums = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7]

Step-by-step:
7: candidate=7, count=1
7: candidate=7, count=2  (same, increment)
5: candidate=7, count=1  (different, decrement)
7: candidate=7, count=2  (same, increment)
5: candidate=7, count=1  (different, decrement)
1: candidate=7, count=0  (different, decrement to 0)
5: candidate=5, count=1  (new candidate)
7: candidate=5, count=0  (different, decrement)
5: candidate=5, count=1  (new candidate)
5: candidate=5, count=2  (same, increment)
7: candidate=5, count=1  (different, decrement)
7: candidate=5, count=0  (different, decrement)
7: candidate=7, count=1  (new candidate)

Final: candidate=7

Count verification: 7 appears 7 times out of 13 (>6.5) ✓
```

## Test Cases

```python
# Basic cases
majorityElement([3,2,3])                      # 3
majorityElement([2,2,1,1,1,2,2])              # 2

# Edge cases
majorityElement([1])                          # 1 (single element)
majorityElement([1,1])                        # 1 (two elements)

# Bare majority
majorityElement([1,2,1,3,1,1])                # 1 (4 out of 6)
majorityElement([6,6,5,5,6])                  # 6 (3 out of 5)

# Negative numbers
majorityElement([-1,-1,2,3,-1])               # -1

# Zero
majorityElement([0,5,5,0,0])                  # 0

# All same
majorityElement([7,7,7,7,7])                  # 7

# Large numbers
majorityElement([1000000000,5,1000000000])    # 1000000000

# Majority at end
majorityElement([1,2,3,4,5,5,5,5,5])          # 5

# Long array
majorityElement([1,2,1,2,1,2,1,2,1])          # 1 (5 out of 9)
```

## Thought Process

The problem guarantees that a majority element exists (appears > n/2 times).

**Key observations**:

1. An element appearing > n/2 times appears in more than half the array
2. There can be at most one such element
3. We need to identify which element it is

**Approach considerations**:

**Naive O(n²)**: For each element, count its occurrences

- Too slow

**Hash map O(n) time, O(n) space**: Count frequencies

- Works well, implemented approach
- Early termination optimization is nice

**Sorting O(n log n)**: Middle element must be majority

- Clever mathematical insight
- Slower but elegant

**Boyer-Moore O(n) time, O(1) space**: Voting algorithm

- Optimal solution
- Requires understanding the algorithm
- Most impressive in interviews

The implemented hash map approach is a good practical solution with reasonable trade-offs. For optimal performance, Boyer-Moore is the gold standard.

## Related Problems

- [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) (appears > n/3 times)
- [1150. Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
