class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s

def test_check_record():
    s = Solution()

    # Test case 1
    record1 = "PPALLP"
    print(s.checkRecord(record1)) # Expected output: True

    # Test case 2
    record2 = "PPALLL"
    print(s.checkRecord(record2)) # Expected output: False

    # Test case 3
    record3 = "A"
    print(s.checkRecord(record3)) # Expected output: True

    # Test case 4
    record4 = "LALL"
    print(s.checkRecord(record4)) # Expected output: True

    # Test case 5
    record5 = "AA"
    print(s.checkRecord(record5)) # Expected output: False

test_check_record()