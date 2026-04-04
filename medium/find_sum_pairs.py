from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        _nums2, _cnt = self.nums2, self.cnt

        _cnt[_nums2[index]] -= 1
        _nums2[index] += val
        _cnt[_nums2[index]] += 1

    def count(self, tot: int) -> int:
        _nums1, _cnt = self.nums1, self.cnt

        ans = 0
        for num in _nums1:
            if (rest := tot - num) in _cnt:
                ans += _cnt[rest]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

def test_find_sum_pairs():
    # Test case 1
    nums1_1 = [1, 1, 2, 2, 2]
    nums2_1 = [1, 4, 5, 2, 5]
    obj1 = FindSumPairs(nums1_1, nums2_1)
    print(obj1.count(7))  # Expected output: 6
    obj1.add(3, 2)
    print(obj1.count(7))  # Expected output: 6

    # Test case 2
    nums1_2 = [1, 2, 3]
    nums2_2 = [4, 5, 6]
    obj2 = FindSumPairs(nums1_2, nums2_2)
    print(obj2.count(7))  # Expected output: 3
    obj2.add(0, 1)
    print(obj2.count(7))  # Expected output: 3
    obj2.add(1, 1)
    print(obj2.count(7))  # Expected output: 3
    obj2.add(2, 1)
    print(obj2.count(7))  # Expected output: 2

    # Test case 3
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    obj3 = FindSumPairs(nums1_3, nums2_3)
    print(obj3.count(8))  # Expected output: 2
    obj3.add(0, 1)
    print(obj3.count(8))  # Expected output: 3
    obj3.add(1, 1)
    print(obj3.count(8))  # Expected output: 3
    obj3.add(2, 1)
    print(obj3.count(8))  # Expected output: 3

    # Test case 4
    nums1_4 = [1, 2, 3]
    nums2_4 = [4, 5, 6]
    obj4 = FindSumPairs(nums1_4, nums2_4)
    print(obj4.count(9))  # Expected output: 1
    obj4.add(0, 1)
    print(obj4.count(9))  # Expected output: 1
    obj4.add(1, 1)
    print(obj4.count(9))  # Expected output: 2
    obj4.add(2, 1)
    print(obj4.count(9))  # Expected output: 2

    # Test case 5
    nums1_5 = [1, 2, 3]
    nums2_5 = [4, 5, 6]
    obj5 = FindSumPairs(nums1_5, nums2_5)
    print(obj5.count(10))  # Expected output: 0
    obj5.add(0, 1)
    print(obj5.count(10))  # Expected output: 0
    obj5.add(1, 1)
    print(obj5.count(10))  # Expected output: 0
    obj5.add(2, 1)
    print(obj5.count(10))  # Expected output: 1

test_find_sum_pairs()