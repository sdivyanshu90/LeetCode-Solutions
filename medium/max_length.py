from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cur = []
        res = []
        def dfs(i):
            if i == len(arr):
                temp = "".join(cur)
                if len(set(temp))== len(temp):
                    res.append(len(temp))
                return
            cur.append(arr[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return max(res)

def test_max_length():
    solution = Solution()

    # Test case 1
    arr = ["un","iq","ue"]
    print(solution.maxLength(arr))  # Expected output: 4

    # Test case 2
    arr = ["cha","r","act","ers"]
    print(solution.maxLength(arr))  # Expected output: 6

    # Test case 3
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    print(solution.maxLength(arr))  # Expected output: 26

    # Test case 4
    arr = ["aa","bb"]
    print(solution.maxLength(arr))  # Expected output: 0

    # Test case 5
    arr = ["ab","cd","ef","gh"]
    print(solution.maxLength(arr))  # Expected output: 8

test_max_length()