from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index_map = {"type" : 0, "color" : 1, "name" : 2}

        index = index_map[ruleKey]

        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count

def test_count_matches():
    solution = Solution()

    # Test case 1
    items1 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey1 = "color"
    ruleValue1 = "silver"
    print(solution.countMatches(items1, ruleKey1, ruleValue1))  # Expected output: 1

    # Test case 2
    items2 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey2 = "type"
    ruleValue2 = "phone"
    print(solution.countMatches(items2, ruleKey2, ruleValue2))  # Expected output: 2

    # Test case 3
    items3 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey3 = "name"
    ruleValue3 = "lenovo"
    print(solution.countMatches(items3, ruleKey3, ruleValue3))  # Expected output: 1

    # Test case 4
    items4 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey4 = "color"
    ruleValue4 = "blue"
    print(solution.countMatches(items4, ruleKey4, ruleValue4))  # Expected output: 1

    # Test case 5
    items5 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey5 = "name"
    ruleValue5 = "pixel"
    print(solution.countMatches(items5, ruleKey5, ruleValue5))  # Expected output: 1

test_count_matches()