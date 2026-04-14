class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        list1 = [False] * n
        list1[source] = True
        q = deque([source])
        while q:
            current = q.popleft()
            if current == destination:
                return True
            for next in graph[current]:
                if not list1[next]:
                    list1[next] = True
                    q.append(next)
        return False

def test_valid_path():
    solution = Solution()

    # Test case 1
    n1 = 3
    edges1 = [[0, 1], [1, 2], [2, 0]]
    source1 = 0
    destination1 = 2
    print(solution.validPath(n1, edges1, source1, destination1))  # Expected output: True

    # Test case 2
    n2 = 6
    edges2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source2 = 0
    destination2 = 5
    print(solution.validPath(n2, edges2, source2, destination2))  # Expected output: False

    # Test case 3
    n3 = 1
    edges3 = []
    source3 = 0
    destination3 = 0
    print(solution.validPath(n3, edges3, source3, destination3))  # Expected output: True

    # Test case 4
    n4 = 5
    edges4 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    source4 = 0
    destination4 = 4
    print(solution.validPath(n4, edges4, source4, destination4))  # Expected output: True

    # Test case 5
    n5 = 5
    edges5 = [[0, 1], [1, 2], [2, 3]]
    source5 = 0
    destination5 = 4
    print(solution.validPath(n5, edges5, source5, destination5))  # Expected output: False

test_valid_path()