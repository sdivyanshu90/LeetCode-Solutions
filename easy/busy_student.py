from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(endTime)):
            if endTime[i] >= queryTime and startTime[i] <= queryTime:
                count += 1
        return count

def test_busy_student():
    solution = Solution()

    # Test case 1
    startTime1 = [1,2,3]
    endTime1 = [3,2,7]
    queryTime1 = 4
    print(solution.busyStudent(startTime1, endTime1, queryTime1))  # Expected output: 1

    # Test case 2
    startTime2 = [4]
    endTime2 = [4]
    queryTime2 = 4
    print(solution.busyStudent(startTime2, endTime2, queryTime2))  # Expected output: 1

    # Test case 3
    startTime3 = [4]
    endTime3 = [4]
    queryTime3 = 5
    print(solution.busyStudent(startTime3, endTime3, queryTime3))  # Expected output: 0

    # Test case 4
    startTime4 = [1,1,1]
    endTime4 = [3,3,3]
    queryTime4 = 2
    print(solution.busyStudent(startTime4, endTime4, queryTime4))  # Expected output: 3

    # Test case 5
    startTime5 = [1,2,3]
    endTime5 = [3,2,7]
    queryTime5 = 1
    print(solution.busyStudent(startTime5, endTime5, queryTime5))  # Expected output: 1

test_busy_student()