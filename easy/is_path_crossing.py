class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
        
        visited = {(0, 0)}
        x = 0
        y = 0

        for c in path:
            dx, dy = moves[c]
            x += dx
            y += dy
            
            if (x, y) in visited:
                return True

            visited.add((x, y))
        
        return False

def test_is_path_crossing():
    solution = Solution()

    # Test Case 1
    path1 = "NES"
    print(solution.isPathCrossing(path1))  # Expected output: False

    # Test Case 2
    path2 = "NESWW"
    print(solution.isPathCrossing(path2))  # Expected output: True

    # Test Case 3
    path3 = "NENESSWW"
    print(solution.isPathCrossing(path3))  # Expected output: True

    # Test Case 4
    path4 = "NNNN"
    print(solution.isPathCrossing(path4))  # Expected output: False

    # Test Case 5
    path5 = "NSNSNSNS"
    print(solution.isPathCrossing(path5))  # Expected output: True

test_is_path_crossing()