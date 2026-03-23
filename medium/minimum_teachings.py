class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        lang_sets = [set(l) for l in languages]

        problematic = set()
        for u, v in friendships:
            u -= 1; v -= 1
            if lang_sets[u].isdisjoint(lang_sets[v]):
                problematic.add(u)
                problematic.add(v)

        freq = defaultdict(int)
        for user in problematic:
            for lang in lang_sets[user]:
                freq[lang] += 1

        if not problematic:
            return 0

        return len(problematic) - max(freq.values(), default=0)

def test_minimum_teachings():
    solution = Solution()

    # Test case 1
    n = 2
    languages = [[1], [2], [1, 2]]
    friendships = [[1, 2], [1, 3], [2, 3]]
    print(solution.minimumTeachings(n, languages, friendships))  # Expected output: 1

    # Test case 2
    n = 3
    languages = [[2], [1, 3], [1, 2], [3]]
    friendships = [[1, 4], [4, 2], [1, 3], [2, 3]]
    print(solution.minimumTeachings(n, languages, friendships))  # Expected output: 2

    # Test case 3
    n = 5
    languages = [[1], [2], [3], [4], [5]]
    friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(solution.minimumTeachings(n, languages, friendships))  # Expected output: 4

    # Test case 4
    n = 4
    languages = [[1, 2], [2, 3], [3, 4], [1, 4]]
    friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]
    print(solution.minimumTeachings(n, languages, friendships))  # Expected output: 0

    # Test case 5
    n = 3
    languages = [[1], [2], [3]]
    friendships = [[1, 2], [2, 3], [1, 3]]
    print(solution.minimumTeachings(n, languages, friendships))  # Expected output: 2

test_minimum_teachings()