import re
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def process_email(email):
            local_part, domain_part = email.split('@')
            local_part = re.sub(r'\+[^@]*', '', local_part)
            local_part = local_part.replace('.', '')
            return f"{local_part}@{domain_part}"

        res = set([process_email(email) for email in emails])
        return len(res)

def test_num_unique_emails():
    solution = Solution()

    # Test case 1
    emails1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(solution.numUniqueEmails(emails1))  # Expected output: 2

    # Test case 2
    emails2 = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    print(solution.numUniqueEmails(emails2))  # Expected output: 3

    # Test case 3
    emails3 = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
    print(solution.numUniqueEmails(emails3))  # Expected output: 2

    # Test case 4
    emails4 = ["test.email+alex@leetcode.com", "test.email+alex@leetcode.com"]
    print(solution.numUniqueEmails(emails4))  # Expected output: 1

    # Test case 5
    emails5 = []
    print(solution.numUniqueEmails(emails5))  # Expected output: 0

test_num_unique_emails()