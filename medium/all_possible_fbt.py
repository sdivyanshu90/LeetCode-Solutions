from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        memo = [[] for _ in range(n + 1)]
        memo[1] = [TreeNode(0)]

        for i in range(3, n + 1, 2):
            for j in range(1, i, 2):
                left_subtrees = memo[j]
                right_subtrees = memo[i - j - 1]
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        memo[i].append(root)

        return memo[n]

def test_all_possible_fbt():
    solution = Solution()

    # Test case 1
    n1 = 7
    result1 = solution.allPossibleFBT(n1)
    print(f"Number of full binary trees with {n1} nodes: {len(result1)}")  # Expected output: 5

    # Test case 2
    n2 = 3
    result2 = solution.allPossibleFBT(n2)
    print(f"Number of full binary trees with {n2} nodes: {len(result2)}")  # Expected output: 1

    # Test case 3
    n3 = 5
    result3 = solution.allPossibleFBT(n3)
    print(f"Number of full binary trees with {n3} nodes: {len(result3)}")  # Expected output: 2

    # Test case 4
    n4 = 1
    result4 = solution.allPossibleFBT(n4)
    print(f"Number of full binary trees with {n4} nodes: {len(result4)}")  # Expected output: 1

    # Test case 5
    n5 = 9
    result5 = solution.allPossibleFBT(n5)
    print(f"Number of full binary trees with {n5} nodes: {len(result5)}")  # Expected output: 14

test_all_possible_fbt()