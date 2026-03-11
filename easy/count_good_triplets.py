class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        
        return count

def test_count_good_triplets():
    solution = Solution()

    # Test case 1
    arr1 = [3, 0, 1, 1, 9, 7]
    a1, b1, c1 = 7, 2, 3
    print(solution.countGoodTriplets(arr1, a1, b1, c1))  # Expected output: 4

    # Test case 2
    arr2 = [1, 1, 2, 2, 3]
    a2, b2, c2 = 0, 0, 1
    print(solution.countGoodTriplets(arr2, a2, b2, c2))  # Expected output: 0

    # Test case 3
    arr3 = [1, 2, 3, 4, 5]
    a3, b3, c3 = 1, 1, 1
    print(solution.countGoodTriplets(arr3, a3, b3, c3))  # Expected output: 3 (triplets are (1, 2, 3), (2, 3, 4), (3, 4, 5))

    # Test case 4
    arr4 = [1, 1, 1]
    a4, b4, c4 = 0, 0, 0
    print(solution.countGoodTriplets(arr4, a4, b4, c4))  # Expected output: 1 (triplet is (1, 1, 1))

    # Test case 5
    arr5 = [1, 2, 3]
    a5, b5, c5 = 2, 2, 2
    print(solution.countGoodTriplets(arr5, a5, b5, c5))  # Expected output: 1 (triplet is (1, 2, 3))


test_count_good_triplets()