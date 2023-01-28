from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output: set[str] = set()
        for email in emails:
            local , domain = email.split('@')
            local = local.split('+')[0]
            #local = ''.join(x for x in local if not x in remove)
            local = local.replace('.','')
            email = local + "@" + domain
            output.add(email)
        return len(output)
            
