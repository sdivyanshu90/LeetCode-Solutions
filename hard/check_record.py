class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp_curr_state = [[0] * 3 for _ in range(2)]
        dp_next_state = [[0] * 3 for _ in range(2)]
        dp_curr_state[0][0] = 1

        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    dp_next_state[total_absences][0] = (
                        dp_next_state[total_absences][0] + 
                        dp_curr_state[total_absences][consecutive_lates]
                    ) % MOD
                    if total_absences < 1:
                        dp_next_state[total_absences + 1][0] = (
                            dp_next_state[total_absences + 1][0] + 
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD
                    if consecutive_lates < 2:
                        dp_next_state[total_absences][consecutive_lates + 1] = (
                            dp_next_state[total_absences][consecutive_lates + 1] + 
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD

            dp_curr_state = [row[:] for row in dp_next_state]
            dp_next_state = [[0] * 3 for _ in range(2)]

        count = sum(dp_curr_state[total_absences][consecutive_lates] \
                    for total_absences in range(2) \
                    for consecutive_lates in range(3)) % MOD
        return count

def test_check_record():
    s = Solution()

    # Test case 1
    n1 = 2
    print(s.checkRecord(n1)) # Expected output: 8

    # Test case 2
    n2 = 1
    print(s.checkRecord(n2)) # Expected output: 3

    # Test case 3
    n3 = 10101
    print(s.checkRecord(n3)) # Expected output: 183236316

    # Test case 4
    n4 = 0
    print(s.checkRecord(n4)) # Expected output: 1

    # Test case 5
    n5 = 5
    print(s.checkRecord(n5)) # Expected output: 94

test_check_record()