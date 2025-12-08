from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]

        def _swap(state, i, j):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            return "".join(state_list)

        target = "123450"
        start_state = "".join(str(num) for row in board for num in row)

        visited = set()
        queue = deque([start_state])
        visited.add(start_state)

        moves = 0

        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()

                if current_state == target:
                    return moves

                zero_pos = current_state.index("0")
                for new_pos in directions[zero_pos]:
                    next_state = _swap(current_state, zero_pos, new_pos)

                    if next_state in visited:
                        continue

                    visited.add(next_state)
                    queue.append(next_state)
            moves += 1

        return -1

def test_sliding_puzzle():
    solution = Solution()
    
    # Test case 1
    board = [[1, 2, 3], [4, 0, 5]]
    print(solution.slidingPuzzle(board)) # Expected: 1
    
    # Test case 2
    board = [[1, 2, 3], [5, 4, 0]]
    print(solution.slidingPuzzle(board)) # Expected: -1
    
    # Test case 3
    board = [[4, 1, 2], [5, 0, 3]]
    print(solution.slidingPuzzle(board)) # Expected: 5
    
    # Test case 4
    board = [[3, 2, 4], [1, 5, 0]]
    print(solution.slidingPuzzle(board)) # Expected: 14
    
    # Test case 5
    board = [[0, 1, 2], [3, 4, 5]]
    print(solution.slidingPuzzle(board)) # Expected: 0

    # Test case 6
    board = [[1, 0, 2], [3, 4, 5]]
    print(solution.slidingPuzzle(board)) # Expected: 1

    # Test case 7
    board = [[1, 2, 0], [3, 4, 5]]
    print(solution.slidingPuzzle(board)) # Expected: 2

    # Test case 8
    board = [[5, 4, 3], [2, 1, 0]]
    print(solution.slidingPuzzle(board)) # Expected: -1

    # Test case 9
    board = [[2, 3, 4], [1, 0, 5]]
    print(solution.slidingPuzzle(board)) # Expected: 6

    # Test case 10
    board = [[1, 2, 3], [0, 4, 5]]
    print(solution.slidingPuzzle(board)) # Expected: 2

test_sliding_puzzle()