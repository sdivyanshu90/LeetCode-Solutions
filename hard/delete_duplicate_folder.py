from collections import Counter
from typing import List

class Trie:
    serial: str = ""
    children: dict

    def __init__(self):
        self.children = dict()


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        freq = Counter()

        def construct(node: Trie) -> None:
            if not node.children:
                return

            v = list()
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")

            v.sort()
            node.serial = "".join(v)
            freq[node.serial] += 1

        construct(root)

        ans = list()
        path = list()

        def operate(node: Trie) -> None:
            if freq[node.serial] > 1:
                return
            if path:
                ans.append(path[:])

            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans

def test_delete_duplicate_folder():
    solution = Solution()

    # Test Case 1
    paths1 = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
    print(solution.deleteDuplicateFolder(paths1))  # Expected output: [['d'], ['d', 'a']]

    # Test Case 2
    paths2 = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"]]
    print(solution.deleteDuplicateFolder(paths2))  # Expected output: [['a'], ['a', 'b'], ['a', 'b', 'x'], ['a', 'b', 'x', 'y'], ['c'], ['c', 'b'], ['d'], ['w']]

    # Test Case 3
    paths3 = [["a", "b"], ["c", "d"], ["c"], ["a"]]
    print(solution.deleteDuplicateFolder(paths3))  # Expected output: [['a'], ['a', 'b'], ['c'], ['c', 'd']]

    # Test Case 4
    paths4 = [["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"]]
    print(solution.deleteDuplicateFolder(paths4))  # Expected output: [['a'], ['a', 'x'], ['a', 'x', 'y'], ['a', 'z']]

    # Test Case 5
    paths5 = [["a"], ["b"], ["c"], ["d"]]
    print(solution.deleteDuplicateFolder(paths5))  # Expected output: [['a'], ['b'], ['c'], ['d']]

test_delete_duplicate_folder()