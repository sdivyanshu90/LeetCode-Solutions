from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    a, b = nums[i], nums[j]
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]

                    if dfs(next_nums + [a + b]):
                        return True
                    if dfs(next_nums + [a - b]):
                        return True
                    if dfs(next_nums + [a * b]):
                        return True
                    if abs(b) > EPS and dfs(next_nums + [a / b]):
                        return True

            return False

        return dfs([float(x) for x in cards])

def test_judge_point_24():
    solution = Solution()

    # Test Case 1
    cards1 = [4, 1, 8, 7]
    print(solution.judgePoint24(cards1))  # Expected: True

    # Test Case 2
    cards2 = [1, 2, 1, 2]
    print(solution.judgePoint24(cards2))  # Expected: False

    # Test Case 3
    cards3 = [3, 3, 8, 8]
    print(solution.judgePoint24(cards3))  # Expected: True

    # Test Case 4
    cards4 = [1, 5, 9, 1]
    print(solution.judgePoint24(cards4))  # Expected: False

    # Test Case 5
    cards5 = [2, 2, 6, 6]
    print(solution.judgePoint24(cards5))  # Expected: True

test_judge_point_24()