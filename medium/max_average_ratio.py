class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            heapq.heappush(max_heap, (-gain, passes, total_students))

        for _ in range(extraStudents):
            current_gain, passes, total_students = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )

        total_pass_ratio = 0
        while max_heap:
            _, passes, total_students = heapq.heappop(max_heap)
            total_pass_ratio += passes / total_students
        return total_pass_ratio / len(classes)

def test_max_average_ratio():
    solution = Solution()

    # Test case 1
    classes1 = [[1, 2], [3, 5], [2, 2]]
    extraStudents1 = 2
    print(solution.maxAverageRatio(classes1, extraStudents1))  # Expected output: 0.78333

    # Test case 2
    classes2 = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents2 = 4
    print(solution.maxAverageRatio(classes2, extraStudents2))  # Expected output: 0.53485

    # Test case 3
    classes3 = [[1, 3], [2, 5], [3, 7]]
    extraStudents3 = 10
    print(solution.maxAverageRatio(classes3, extraStudents3))  # Expected output: 0.78333

    # Test case 4
    classes4 = [[5, 10], [10, 20], [15, 30]]
    extraStudents4 = 5
    print(solution.maxAverageRatio(classes4, extraStudents4))  # Expected output: 0.66667

    # Test case 5
    classes5 = [[0, 1], [0, 2], [0, 3]]
    extraStudents5 = 6
    print(solution.maxAverageRatio(classes5, extraStudents5))  # Expected output: 0.83333

test_max_average_ratio()