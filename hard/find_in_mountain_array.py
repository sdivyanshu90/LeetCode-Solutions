# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        left, right = 1, length - 2
        while left != right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left
        left, right = 0, peak
        while left != right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        
        if mountainArr.get(left) == target:
            return left
        
        left, right = peak + 1, length - 1
        while left != right:
            mid = (left + right) // 2
            if mountainArr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
            
        if mountainArr.get(left) == target:
            return left
        
        return -1

def test_find_in_mountain_array():
    solution = Solution()

    # Test case 1
    class MountainArray1:
        def __init__(self):
            self.arr = [1, 2, 3, 4, 5, 3, 1]
        def get(self, index: int) -> int:
            return self.arr[index]
        def length(self) -> int:
            return len(self.arr)
    
    mountainArr1 = MountainArray1()
    target1 = 3
    print(solution.findInMountainArray(target1, mountainArr1))  # Expected output: 2

    # Test case 2
    class MountainArray2:
        def __init__(self):
            self.arr = [0, 1, 2, 4, 2, 1]
        def get(self, index: int) -> int:
            return self.arr[index]
        def length(self) -> int:
            return len(self.arr)
    
    mountainArr2 = MountainArray2()
    target2 = 3
    print(solution.findInMountainArray(target2, mountainArr2))  # Expected output: -1

    # Test case 3
    class MountainArray3:
        def __init__(self):
            self.arr = [0, 5, 3, 1]
        def get(self, index: int) -> int:
            return self.arr[index]
        def length(self) -> int:
            return len(self.arr)
    
    mountainArr3 = MountainArray3()
    target3 = 1
    print(solution.findInMountainArray(target3, mountainArr3))  # Expected output: 3

test_find_in_mountain_array()