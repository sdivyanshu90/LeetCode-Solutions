from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_sizes = []
        last_occurrence = [0] * 26
        first_occurrence = [-1] * 26
        partition_start, partition_end = 0, 0

        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        for i, char in enumerate(s):
            index = ord(char) - ord("a")

            if first_occurrence[index] == -1:
                first_occurrence[index] = i

            if partition_end < first_occurrence[index]:
                partition_sizes.append(partition_end - partition_start + 1)
                partition_start = i
                partition_end = i

            partition_end = max(partition_end, last_occurrence[index])

        if partition_end - partition_start + 1 > 0:
            partition_sizes.append(partition_end - partition_start + 1)

        return partition_sizes

# Approach 2
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         last_pos = defaultdict(int)

#         for i, ch in enumerate(s):
#             last_pos[ch] = i 

#         start = 0
#         end = 0
#         res = []

#         for i, ch in enumerate(s):
#             end = max(end, last_pos[ch])

#             if i == end:
#                 res.append(end - start + 1)
#                 start = i + 1

#         return res

def test_partition_labels():
    solution = Solution()
    
    # Test case 1
    s1 = "ababcbacadefegdehijhklij"
    print(solution.partitionLabels(s1)) # Expected: [9,7,8]
    
    # Test case 2
    s2 = "eccbbbbdec"
    print(solution.partitionLabels(s2)) # Expected: [10]
    
    # Test case 3
    s3 = "caedbdedda"
    print(solution.partitionLabels(s3)) # Expected: [1,9]
    
    # Test case 4
    s4 = "abc"
    print(solution.partitionLabels(s4)) # Expected: [1,1,1]

    # Test case 5
    s5 = "aabbcc"
    print(solution.partitionLabels(s5)) # Expected: [2,2,2]

    # Test case 6
    s6 = "abacdc"
    print(solution.partitionLabels(s6)) # Expected: [3,3]

    # Test case 7
    s7 = "zxyzyx"
    print(solution.partitionLabels(s7)) # Expected: [6]

    # Test case 8
    s8 = "a"
    print(solution.partitionLabels(s8)) # Expected: [1]

    # Test case 9
    s9 = "ababcbacadefegdehijhklijxyzxyz"
    print(solution.partitionLabels(s9)) # Expected: [9,7,8,6]

    # Test case 10
    s10 = "abcdedcba"
    print(solution.partitionLabels(s10)) # Expected: [9]

test_partition_labels()