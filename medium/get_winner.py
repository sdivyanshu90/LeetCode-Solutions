class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        queue = deque(arr[1:])
        curr = arr[0]
        winstreak = 0

        while queue:
            opponent = queue.popleft()
            if curr > opponent:
                queue.append(opponent)
                winstreak += 1
            else:
                queue.append(curr)
                curr = opponent
                winstreak = 1
            
            if winstreak == k or curr == max_element:
                return curr

def test_get_winner():
    solution = Solution()

    # Test case 1
    arr1 = [2, 1, 3, 5, 4]
    k1 = 2
    print(solution.getWinner(arr1, k1))  # Expected output: 5

    # Test case 2
    arr2 = [3, 2, 1]
    k2 = 10
    print(solution.getWinner(arr2, k2))  # Expected output: 3

    # Test case 3
    arr3 = [1, 9, 8, 2, 3]
    k3 = 3
    print(solution.getWinner(arr3, k3))  # Expected output: 9

    # Test case 4
    arr4 = [5, 4, 3, 2, 1]
    k4 = 1
    print(solution.getWinner(arr4, k4))  # Expected output: 5

    # Test case 5
    arr5 = [1, 2, 3, 4, 5]
    k5 = 5
    print(solution.getWinner(arr5, k5))  # Expected output: 5

test_get_winner()