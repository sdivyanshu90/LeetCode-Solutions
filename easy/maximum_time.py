class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        
        if time[0] == '?':
            time[0] = '2' if time[1] == '?' or time[1] < '4' else '1'
        
        if time[1] == '?':
            time[1] = '3' if time[0] == '2' else '9'
        
        if time[3] == '?':
            time[3] = '5'
        
        if time[4] == '?':
            time[4] = '9'
        
        return ''.join(time)

def test_maximum_time():
    solution = Solution()

    # Test case 1
    time = "2?:?0"
    print(solution.maximumTime(time))  # Expected output: "23:50"

    # Test case 2
    time = "0?:3?"
    print(solution.maximumTime(time))  # Expected output: "09:39"

    # Test case 3
    time = "1?:22"
    print(solution.maximumTime(time))  # Expected output: "19:22"

    # Test case 4
    time = "??:??"
    print(solution.maximumTime(time))  # Expected output: "23:59"

    # Test case 5
    time = "?0:?6"
    print(solution.maximumTime(time))  # Expected output: "20:56"

test_maximum_time()