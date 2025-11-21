class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26  
        max_count = 0

        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            max_count = max(max_count, freq[ord(task) - ord('A')])

        time = (max_count - 1) * (n + 1)
        for f in freq:
            if f == max_count:
                time += 1

        return max(len(tasks), time)

def test_least_interval():
    s = Solution()

    # Test case 1
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(s.leastInterval(tasks, n))  # Expected output: 8

    # Test case 2
    tasks = ["A","A","A","B","B","B"]
    n = 0
    print(s.leastInterval(tasks, n))  # Expected output: 6

    # Test case 3
    tasks = ["A","A","A","A","B","B","C","C"]
    n = 2
    print(s.leastInterval(tasks, n))  # Expected output: 10

    # Test case 4
    tasks = ["A"]
    n = 2
    print(s.leastInterval(tasks, n))  # Expected output: 1

    # Test case 5
    tasks = ["A","B","C","D","E","F"]
    n = 2
    print(s.leastInterval(tasks, n))  # Expected output: 6

test_least_interval()