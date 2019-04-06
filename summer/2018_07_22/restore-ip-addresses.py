#这道题的思路是回溯法+分类讨论
#主要排除 0XX, > 255 的情况 注意容易忽视 X.0.X.X
class Solution:
    def get_sub(self, s, r, n):
        if s == '': return

        if n == 4:
            if int(s) > 255 or s[0] == '0' and len(s) > 1:
                return
            else:
                r.append(s)
                self.result.append(".".join(r))
                r.pop()

        for i in range(1, 4):
            print(r)
            if int(s[:i]) > 255 or (i > 1 and s[0] == '0'):
                pass
            else:
                r.append(s[:i])
                self.get_sub(s[i:], r, n + 1)
                r.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        self.result = []
        self.get_sub(s, [], 1)
        return self.result
