from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]

        index = 0
        while index < len(formula):
            if formula[index] == "(":
                stack.append(defaultdict(int))
                index += 1
            elif formula[index] == ")":
                curr_map = stack.pop()
                index += 1
                multiplier = ""
                while index < len(formula) and formula[index].isdigit():
                    multiplier += formula[index]
                    index += 1
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier

                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]
            else:
                curr_atom = formula[index]
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                curr_count = ""
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                if curr_count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(curr_count)
        final_map = dict(sorted(stack[0].items()))
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans

def test_count_of_atoms():
    solution = Solution()

    # Test Case 1
    formula = "H2O"
    print(solution.countOfAtoms(formula))  # Expected: "H2O"

    # Test Case 2
    formula = "Mg(OH)2"
    print(solution.countOfAtoms(formula))  # Expected: "H2MgO2"

    # Test Case 3
    formula = "K4(ON(SO3)2)2"
    print(solution.countOfAtoms(formula))  # Expected: "K4N2O14S4"

    # Test Case 4: Single atom
    formula = "C"
    print(solution.countOfAtoms(formula))  # Expected: "C"

    # Test Case 5: Atom with count
    formula = "C6H12O6"
    print(solution.countOfAtoms(formula))  # Expected: "C6H12O6"

    # Test Case 6: Nested parentheses
    formula = "((H)2(O)1)3"
    print(solution.countOfAtoms(formula))  # Expected: "H6O3"

    # Test Case 7: No parentheses, multiple atoms
    formula = "NaClH2O"
    print(solution.countOfAtoms(formula))  # Expected: "ClH2NaO"

    # Test Case 8: Complex nested structure
    formula = "Fe(C5H5)2"
    print(solution.countOfAtoms(formula))  # Expected: "C10H10Fe"

    # Test Case 9: Large counts
    formula = "C100H200O100"
    print(solution.countOfAtoms(formula))  # Expected: "C100H200O100"

    # Test Case 10: Multiple nested parentheses with counts
    formula = "Al2(SO4)3(H2O)6"
    print(solution.countOfAtoms(formula))  # Expected: "Al2H12O18S3"

test_count_of_atoms()