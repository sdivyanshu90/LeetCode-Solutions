class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            
            for i in range(n):
                if i not in children:
                    return i
                
            return -1
        
        root = find_root()
        if root == -1:
            return False
        
        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    
                    stack.append(child)
                    seen.add(child)
        
        return len(seen) == n

def test_validateBinaryTreeNodes():
    solution = Solution()

    # Test case 1
    n1 = 4
    leftChild1 = [1, -1, 3, -1]
    rightChild1 = [2, -1, -1, -1]
    print(solution.validateBinaryTreeNodes(n1, leftChild1, rightChild1)) # Expected output: True

    # Test case 2
    n2 = 4
    leftChild2 = [1, -1, 3, -1]
    rightChild2 = [2, -1, -1, 0]
    print(solution.validateBinaryTreeNodes(n2, leftChild2, rightChild2)) # Expected output: False

    # Test case 3
    n3 = 2
    leftChild3 = [1, 0]
    rightChild3 = [-1, -1]
    print(solution.validateBinaryTreeNodes(n3, leftChild3, rightChild3)) # Expected output: False

    # Test case 4
    n4 = 6
    leftChild4 = [1, -1, -1, -1, -1, -1]
    rightChild4 = [2, -1, -1, -1, -1, -1]
    print(solution.validateBinaryTreeNodes(n4, leftChild4, rightChild4)) # Expected output: False

    # Test case 5
    n5 = 5
    leftChild5 = [4,-1,-1,-1,-1]
    rightChild5 = [-1,-1,-1,-1,-1]
    print(solution.validateBinaryTreeNodes(n5, leftChild5, rightChild5)) # Expected output: False

test_validateBinaryTreeNodes()