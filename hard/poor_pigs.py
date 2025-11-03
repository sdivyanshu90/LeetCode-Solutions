class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        pigs = 0
        while (states ** pigs) < buckets:
            pigs += 1
        return pigs

def test_poor_pigs():
    s = Solution()

    # Test case 1
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60
    print(s.poorPigs(buckets, minutesToDie, minutesToTest))  # Expected output: 5

    # Test case 2
    buckets = 4
    minutesToDie = 15
    minutesToTest = 15
    print(s.poorPigs(buckets, minutesToDie, minutesToTest))  # Expected output: 2

    # Test case 3
    buckets = 4
    minutesToDie = 15
    minutesToTest = 30
    print(s.poorPigs(buckets, minutesToDie, minutesToTest))  # Expected output: 2

    # Test case 4
    buckets = 25
    minutesToDie = 15
    minutesToTest = 60
    print(s.poorPigs(buckets, minutesToDie, minutesToTest))  # Expected output: 2

    # Test case 5
    buckets = 1
    minutesToDie = 15
    minutesToTest = 15
    print(s.poorPigs(buckets, minutesToDie, minutesToTest))  # Expected output: 0

test_poor_pigs()