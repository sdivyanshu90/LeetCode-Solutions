class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr_hash = defaultdict(int)
        target_hash = defaultdict(int)

        for i, j in zip(arr, target):
            arr_hash[i] += 1
            target_hash[j] += 1

        return arr_hash == target_hash

def test_can_be_equal():
    solution = Solution()

    # Test case 1
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(solution.canBeEqual(target, arr))  # Expected output: True

    # Test case 2
    target = [7]
    arr = [7]
    print(solution.canBeEqual(target, arr))  # Expected output: True

    # Test case 3
    target = [1, 12]
    arr = [12, 1]
    print(solution.canBeEqual(target, arr))  # Expected output: True

    # Test case 4
    target = [3, 7, 9]
    arr = [3, 7, 11]
    print(solution.canBeEqual(target, arr))  # Expected output: False

    # Test case 5
    target = [1, 2, 3]
    arr = [1, 2, 2]
    print(solution.canBeEqual(target, arr))  # Expected output: False

test_can_be_equal()