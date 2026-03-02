class Solution:
    def isPrerequisite(
        self, adjList: dict, visited: List[bool], src: int, target: int
    ) -> bool:
        visited[src] = True

        if src == target:
            return True

        for adj in adjList.get(src, []):
            if not visited[adj]:
                if self.isPrerequisite(adjList, visited, adj, target):
                    return True
        return False

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])

        result = []

        for query in queries:
            visited = [False] * numCourses
            result.append(
                self.isPrerequisite(adjList, visited, query[0], query[1])
            )

        return result

def test_check_if_prerequisite():
    solution = Solution()

    # Test case 1
    numCourses = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1], [1, 0]]
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [False, True]

    # Test case 2
    numCourses = 2
    prerequisites = []
    queries = [[1, 0], [0, 1]]
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [False, False]

    # Test case 3
    numCourses = 3
    prerequisites = [[1, 2], [1, 0], [2, 0]]
    queries = [[1, 0], [1, 2]]
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [True, True]

    # Test case 4
    numCourses = 3
    prerequisites = [[0, 1], [1, 2]]
    queries = [[0, 2], [2, 0]]
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [True, False]

    # Test case 5
    numCourses = 5
    prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]]
    queries = [[0, 4], [1, 3], [2, 4], [3, 0]]
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))  # Expected output: [True, True, True, False]

test_check_if_prerequisite()