from typing import List

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        if n == 1: 
            return [0]
        ans = [0] * n
        st = [n - 1]
        for i in range(n - 2, -1, -1):
            while st and t[i] >= t[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans

def test_daily_temperatures():
    solution = Solution()
    
    # Test case 1
    t1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures(t1)) #Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Test case 2
    t2 = [30, 40, 50, 60]
    print(solution.dailyTemperatures(t2)) #Expected: [1, 1, 1, 0]
    
    # Test case 3
    t3 = [30, 60, 90]
    print(solution.dailyTemperatures(t3)) #Expected: [1, 1, 0]
    
    # Test case 4
    t4 = [90, 80, 70, 60]
    print(solution.dailyTemperatures(t4)) #Expected: [0, 0, 0, 0]
    
    # Test case 5
    t5 = [70]
    print(solution.dailyTemperatures(t5)) #Expected: [0]
    
    # Test case 6
    t6 = [70, 70, 70, 70]
    print(solution.dailyTemperatures(t6)) #Expected: [0, 0, 0, 0]

    # Test case 7
    t7 = [55, 56, 57, 58, 59, 60]
    print(solution.dailyTemperatures(t7)) #Expected: [1, 1, 1, 1, 1, 0]

    # Test case 8
    t8 = [60, 59, 58, 57, 56, 55]
    print(solution.dailyTemperatures(t8)) #Expected: [0, 0, 0, 0, 0, 0]

    # Test case 9
    t9 = [70, 75, 72, 76, 73, 78]
    print(solution.dailyTemperatures(t9)) #Expected: [1, 2, 1, 2, 1, 0]

    # Test case 10
    t10 = [80, 81, 79, 82, 78, 83]
    print(solution.dailyTemperatures(t10)) #Expected: [1, 2, 1, 2, 1, 0]

test_daily_temperatures()