from typing import List

class Solution:
    def constructDistancedSequence(self, target_number: int) -> List[int]:
        result_sequence = [0] * (target_number * 2 - 1)
        is_number_used = [False] * (target_number + 1)

        self.find_lexicographically_largest_sequence(
            0, result_sequence, is_number_used, target_number
        )

        return result_sequence

    def find_lexicographically_largest_sequence(
        self, current_index, result_sequence, is_number_used, target_number
    ):
        if current_index == len(result_sequence):
            return True

        if result_sequence[current_index] != 0:
            return self.find_lexicographically_largest_sequence(
                current_index + 1,
                result_sequence,
                is_number_used,
                target_number,
            )

        for number_to_place in range(target_number, 0, -1):
            if is_number_used[number_to_place]:
                continue

            is_number_used[number_to_place] = True
            result_sequence[current_index] = number_to_place

            if number_to_place == 1:
                if self.find_lexicographically_largest_sequence(
                    current_index + 1,
                    result_sequence,
                    is_number_used,
                    target_number,
                ):
                    return True
            elif (
                current_index + number_to_place < len(result_sequence)
                and result_sequence[current_index + number_to_place] == 0
            ):
                result_sequence[current_index + number_to_place] = (
                    number_to_place
                )

                if self.find_lexicographically_largest_sequence(
                    current_index + 1,
                    result_sequence,
                    is_number_used,
                    target_number,
                ):
                    return True

                result_sequence[current_index + number_to_place] = 0

            result_sequence[current_index] = 0
            is_number_used[number_to_place] = False

        return False

def test_construct_distanced_sequence():
    s = Solution()

    # Test Case 1
    target_number1 = 3
    print(s.constructDistancedSequence(target_number1)) # Expected Output: [3,1,2,3,2]

    # Test Case 2
    target_number2 = 5
    print(s.constructDistancedSequence(target_number2)) # Expected Output: [5,3,1,4,3,5,4,2]

    # Test Case 3
    target_number3 = 2
    print(s.constructDistancedSequence(target_number3)) # Expected Output: [2,1,2]

    # Test Case 4
    target_number4 = 4
    print(s.constructDistancedSequence(target_number4)) # Expected Output: [4,2,3,4,3,1,2]

    # Test Case 5
    target_number5 = 6
    print(s.constructDistancedSequence(target_number5)) # Expected Output: [6,4,2,5,3,6,5,4,3,1,2]

test_construct_distanced_sequence()