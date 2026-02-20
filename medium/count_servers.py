from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0]) if num_rows > 0 else 0
        communicable_servers_count = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    can_communicate = False

                    for other_col in range(num_cols):
                        if other_col != col and grid[row][other_col] == 1:
                            can_communicate = True
                            break

                    if can_communicate:
                        communicable_servers_count += 1
                    else:
                        for other_row in range(num_rows):
                            if other_row != row and grid[other_row][col] == 1:
                                can_communicate = True
                                break

                        if can_communicate:
                            communicable_servers_count += 1

        return communicable_servers_count

def test_count_servers():
    solution = Solution()

    # Test case 1
    grid = [[1,0],[0,1]]
    print(solution.countServers(grid))  # Expected output: 0

    # Test case 2
    grid = [[1,0],[1,1]]
    print(solution.countServers(grid))  # Expected output: 3

    # Test case 3
    grid = [[1,1,0],[0,0,1],[1,0,1]]
    print(solution.countServers(grid))  # Expected output: 5

    # Test case 4
    grid = [[1,0,0],[0,1,0],[0,0,1]]
    print(solution.countServers(grid))  # Expected output: 0

    # Test case 5
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    print(solution.countServers(grid))  # Expected output: 9

test_count_servers()