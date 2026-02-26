from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if not rating:
            return 0
            
        max_val = max(rating)
        left_tree = [0] * (max_val + 1)
        right_tree = [0] * (max_val + 1)
        
        def update(tree: List[int], index: int, val: int):
            while index < len(tree):
                tree[index] += val
                index += index & (-index)
                
        def query(tree: List[int], index: int) -> int:
            total_sum = 0
            while index > 0:
                total_sum += tree[index]
                index -= index & (-index)
            return total_sum
            
        for r in rating:
            update(right_tree, r, 1)
            
        teams = 0
        
        for r in rating:
            update(right_tree, r, -1)
            less_left = query(left_tree, r - 1)
            greater_left = query(left_tree, max_val) - query(left_tree, r)
            less_right = query(right_tree, r - 1)
            greater_right = query(right_tree, max_val) - query(right_tree, r)
            teams += (less_left * greater_right) + (greater_left * less_right)
            update(left_tree, r, 1)     
                   
        return teams

def test_num_teams():
    solution = Solution()

    # Test case 1
    rating1 = [2, 5, 3, 4, 1]
    print(solution.numTeams(rating1))  # Expected output: 3

    # Test case 2
    rating2 = [2, 1, 3]
    print(solution.numTeams(rating2))  # Expected output: 0

    # Test case 3
    rating3 = [1, 2, 3, 4]
    print(solution.numTeams(rating3))  # Expected output: 4

    # Test case 4
    rating4 = [4, 3, 2, 1]
    print(solution.numTeams(rating4))  # Expected output: 4

    # Test case 5
    rating5 = [1, 3, 2, 4]
    print(solution.numTeams(rating5))  # Expected output: 2

test_num_teams()