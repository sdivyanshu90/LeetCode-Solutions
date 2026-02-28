from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        for i in range(1, n + 1):
            if i in target:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")
            if i == target[-1]:
                break
        return stack

def test_build_array():
    solution = Solution()

    # Test case 1
    target1 = [1, 3]
    n1 = 3
    print(solution.buildArray(target1, n1))  # Expected output: ["Push", "Push", "Pop", "Push"]

    # Test case 2
    target2 = [1, 2, 3]
    n2 = 3
    print(solution.buildArray(target2, n2))  # Expected output: ["Push", "Push", "Push"]

    # Test case 3
    target3 = [1, 2]
    n3 = 4
    print(solution.buildArray(target3, n3))  # Expected output: ["Push", "Push"]

    # Test case 4
    target4 = [2, 3, 4]
    n4 = 4
    print(solution.buildArray(target4, n4))  # Expected output: ["Push", "Pop", "Push", "Push", "Push"]

    # Test case 5
    target5 = [1, 4]
    n5 = 4
    print(solution.buildArray(target5, n5))  # Expected output: ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']

test_build_array()