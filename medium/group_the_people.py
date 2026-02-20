from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        max_size = max(groupSizes)  # Find the maximum group size
        groups = [[] for _ in range(max_size + 1)]  # Initialize a list of empty lists
        result = []  # Initialize the final result list
        
        # Iterate through the groupSizes list
        for i, size in enumerate(groupSizes):
            groups[size].append(i)  # Add person 'i' to the group of size 'size'
            
            # If the group size matches the number of people in the group, add it to the result
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []  # Reset the group
        
        return result

def test_group_the_people():
    solution = Solution()

    # Test case 1
    groupSizes = [3,3,3,3,3,1,3]
    print(solution.groupThePeople(groupSizes))  # Expected output: [[5], [0, 1, 2], [3, 4, 6]]

    # Test case 2
    groupSizes = [2,1,3,3,3,2]
    print(solution.groupThePeople(groupSizes))  # Expected output: [[1], [0, 5], [2, 3, 4]]

    # Test case 3
    groupSizes = [1]
    print(solution.groupThePeople(groupSizes))  # Expected output: [[0]]

    # Test case 4
    groupSizes = [2,2]
    print(solution.groupThePeople(groupSizes))  # Expected output: [[0, 1]]

    # Test case 5
    groupSizes = [3,3,3]
    print(solution.groupThePeople(groupSizes))  # Expected output: [[0, 1, 2]]

test_group_the_people()