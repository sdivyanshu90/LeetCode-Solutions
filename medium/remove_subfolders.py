from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]

        for i in range(1, len(folder)):
            last_folder = result[-1]
            last_folder += "/"
            if not folder[i].startswith(last_folder):
                result.append(folder[i])
        return result

def test_remove_subfolders():
    solution = Solution()

    # Test case 1
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    print(solution.removeSubfolders(folder))  # Expected output: ["/a","/c/d","/c/f"]

    # Test case 2
    folder = ["/a","/a/b/c","/a/b/d"]
    print(solution.removeSubfolders(folder))  # Expected output: ["/a"]

    # Test case 3
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    print(solution.removeSubfolders(folder))  # Expected output: ["/a/b/c","/a/b/ca","/a/b/d"]

    # Test case 4
    folder = ["/"]
    print(solution.removeSubfolders(folder))  # Expected output: ["/"]

    # Test case 5
    folder = ["/a/b","/a/b/c/d","/a/b/c"]
    print(solution.removeSubfolders(folder))  # Expected output: ["/a/b"]

test_remove_subfolders()