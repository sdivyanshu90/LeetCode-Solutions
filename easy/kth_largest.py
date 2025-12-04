from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        self.stream.insert(index, val)
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            if mid_element == val:
                return mid
            elif mid_element > val:
                right = mid - 1
            else:
                left = mid + 1
        return left


def test_kth_largest():
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    # Test Case 1
    print(kthLargest.add(3)) # Expected: 4

    # Test Case 2
    print(kthLargest.add(5)) # Expected: 5

    # Test Case 3
    print(kthLargest.add(10)) # Expected: 5

    # Test Case 4
    print(kthLargest.add(9)) # Expected: 8

    # Test Case 5
    print(kthLargest.add(4)) # Expected: 8

test_kth_largest()