from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = [[] for _ in range(n)]
        group_graph = [[] for _ in range(group_id)]

        for curr, prev_items in enumerate(beforeItems):
            for prev in prev_items:
                item_graph[prev].append(curr)

                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])

        def topo_sort(graph):
            visiting = set()
            finished = set()
            output = deque()

            def helper(node):
                visiting.add(node)

                for neighbor in graph[node]:
                    if neighbor not in finished:
                        if neighbor in visiting:
                            return False
                        valid = helper(neighbor)
                        if not valid:
                            return False

                visiting.remove(node)
                finished.add(node)
                output.appendleft(node)

                return True

            for node in range(len(graph)):
                if node not in finished:
                    valid = helper(node)
                    if not valid:
                        return []

            return list(output)

        item_order = topo_sort(item_graph)
        group_order = topo_sort(group_graph)

        if not item_order or not group_order:
            return []

        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        return [item for group_index in group_order for item in ordered_groups[group_index]]

def test_sort_items():
    solution = Solution()

    # Test Case 1
    n1 = 8
    m1 = 2
    group1 = [-1,-1,1,0,0,1,0,-1]
    beforeItems1 = [[],[6],[5],[6],[3,6],[],[],[]]
    print(solution.sortItems(n1, m1, group1, beforeItems1))  # Expected Output: [7, 0, 5, 2, 6, 3, 4, 1]

    # Test Case 2
    n2 = 8
    m2 = 2
    group2 = [-1,-1,1,0,0,1,0,-1]
    beforeItems2 = [[],[6],[5],[6],[3],[],[4],[]]
    print(solution.sortItems(n2, m2, group2, beforeItems2))  # Expected Output: []

    # Test Case 3
    n3 = 5
    m3 = 5
    group3 = [2,0,-1,3,0]
    beforeItems3 = [[],[0,3],[1,4],[],[]]
    print(solution.sortItems(n3, m3, group3, beforeItems3))  # Expected Output: [3, 0, 4, 1, 2]

    # Test Case 4
    n4 = 3
    m4 = 1
    group4 = [-1,0,0]
    beforeItems4 = [[],[0],[1]]
    print(solution.sortItems(n4, m4, group4, beforeItems4))  # Expected Output: [0, 1, 2]

    # Test Case 5
    n5 = 4
    m5 = 2
    group5 = [1,0,1,0]
    beforeItems5 = [[],[2,3],[3],[]]
    print(solution.sortItems(n5, m5, group5, beforeItems5))  # Expected Output: []

test_sort_items()