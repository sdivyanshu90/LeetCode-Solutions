# Unique Email Addresses

Problem summary

- Given list of email addresses, count unique destinations.
- Local part (before @): ignore dots '.', ignore everything after '+'.
- Domain part (after @): unchanged.
- Example: "test.email+alex@leetcode.com" -> "testemail@leetcode.com".

Current implementation (in repository)

- Implementation uses regex and set:
  - Defines process_email function to normalize each email.
  - Splits on '@' to separate local and domain.
  - Uses regex to remove '+' and everything after.
  - Removes all dots from local part.
  - Combines normalized local with domain.
  - Stores all processed emails in set to get unique count.
- Example code:
  ```python
  def process_email(email):
      local_part, domain_part = email.split('@')
      local_part = re.sub(r'\+[^@]*', '', local_part)
      local_part = local_part.replace('.', '')
      return f"{local_part}@{domain_part}"
  res = set([process_email(email) for email in emails])
  return len(res)
  ```

Why this works

- Split on '@' separates local and domain for independent processing.
- Regex `\+[^@]*` matches '+' and everything after until '@' (or end).
- replace('.', '') removes all dots efficiently.
- Set deduplicates normalized emails automatically.
- Domain remains unchanged as per problem rules.

Time complexity

- Let n = number of emails, m = average email length.
- Processing each email: O(m) for regex and string operations.
- Total processing: O(n × m).
- Set operations: O(n) average.
- Overall time complexity: O(n × m).

Space complexity

- Set stores up to n unique emails: O(n × m).
- Space complexity: O(n × m).

Thought process and trade-offs

- Regex approach: concise handling of '+' rule.
- Alternative (commented in code): split on '+' without regex - simpler, same effect.
- Set for deduplication: standard pattern, efficient.
- Could optimize: early termination impossible since all emails must be checked.
- Current approach: clear and correct.
