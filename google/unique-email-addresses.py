class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if len(emails) == 0:
            return 0
        emailSet = set()
        for email in emails:
            e = ""
            local, domain = email.split("@")
            e = "@" + domain
            local = "".join(local.split("+")[0].split("."))
            e = local + e 
            emailSet.add(e)
        return len(emailSet)
