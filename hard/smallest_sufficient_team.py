from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        res = [0] * 17        
        n = len(req_skills)
        
        for i, i_skills in enumerate(people):
            people[i] = set(i_skills)
        
        for i, i_skills in enumerate(people):
            for j, j_skills in enumerate(people):
                if i != j and j_skills.issubset(i_skills):
                    people[j] = set()

        def dfs(idx, has, path):
            nonlocal res

            if idx == n:
                res = path

            elif req_skills[idx] in has:
                dfs(idx+1, has, path)

            else:
                if len(path) + 1 < len(res):
                    for i, p in enumerate(people):
                        if req_skills[idx] in p:
                            common = p & has
                            has |= p
                            dfs(idx+1, has, path+[i])
                            has -= p
                            has |= common

        dfs(0, set(), [])
        return res

def test_smallest_sufficient_team():
    solution = Solution()

    # Test case 1
    req_skills = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    print(solution.smallestSufficientTeam(req_skills, people))  # Expected output: [0,2]

    # Test case 2
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    print(solution.smallestSufficientTeam(req_skills, people))  # Expected output: [1,2]

    # Test case 3
    req_skills = ["a","b","c"]
    people = [["a"],["b"],["c"],["a","b"],["b","c"]]
    print(solution.smallestSufficientTeam(req_skills, people))  # Expected output: [0,1,2]

    # Test case 4
    req_skills = ["skill1","skill2"]
    people = [["skill1"],["skill2"],["skill1","skill2"]]
    print(solution.smallestSufficientTeam(req_skills, people))  # Expected output: [2]

    # Test case 5
    req_skills = ["x","y","z"]
    people = [["x","y"],["y","z"],["x","z"]]
    print(solution.smallestSufficientTeam(req_skills, people))  # Expected output: [0,1] or [0,2] or [1,2]

test_smallest_sufficient_team()