import re

class Solution:
    def interpret(self, command: str) -> str:
        return re.sub(r'\(\)|\(al\)', lambda m: 'o' if m.group(0) == '()' else 'al', command)

def test_interpret():
    solution = Solution()

    # Test case 1
    command = "G()(al)"
    print(solution.interpret(command))  # Expected output: "Goal"

    # Test case 2
    command = "G()()()()(al)"
    print(solution.interpret(command))  # Expected output: "Gooooal"

    # Test case 3
    command = "(al)G(al)()()G"
    print(solution.interpret(command))  # Expected output: "alGalooG"

    # Test case 4
    command = "G()()()()"
    print(solution.interpret(command))  # Expected output: "Goooo"

    # Test case 5
    command = "(al)(al)(al)"
    print(solution.interpret(command))  # Expected output: "alalal"

test_interpret()