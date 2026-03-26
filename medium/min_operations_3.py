class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0

        for i in range(n):
            answer[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left

            j = n - 1 - i
            answer[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right

        return answer

def test_min_operations():
    solution = Solution()

    # Test Case 1
    boxes1 = "110"
    print(solution.minOperations(boxes1)) # Expected Output: [1, 1, 3]

    # Test Case 2
    boxes2 = "001011"
    print(solution.minOperations(boxes2)) # Expected Output: [11, 8, 5, 4, 3, 4]

    # Test Case 3
    boxes3 = "0"
    print(solution.minOperations(boxes3)) # Expected Output: [0]

    # Test Case 4
    boxes4 = "1"
    print(solution.minOperations(boxes4)) # Expected Output: [0]

    # Test Case 5
    boxes5 = "101"
    print(solution.minOperations(boxes5)) # Expected Output: [1, 2, 1]

test_min_operations()