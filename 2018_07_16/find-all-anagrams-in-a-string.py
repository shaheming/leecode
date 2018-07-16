# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        if len(p) == len(s):
            if p == s:
                return [0]
            else:
                return []

        r = []
        ch_dict = {}
        for c in p:
            if ch_dict.get(c, None):
                ch_dict[c] += 1
            else:
                ch_dict[c] = 1

        print(ch_dict)
        p_len = len(p)
        s_len = len(s)
        i = 0
        while (i < len(s)):
            if p_len > s_len - i:
                return r
            else:
                if self.dfs(ch_dict, s[i:i + p_len]):
                    r.append(i)
                    while i + p_len < s_len and s[i] == s[i + p_len]:
                        i += 1
                        r.append(i)

                i += 1
        return r

    def dfs(self, ch_dict, s):
        if len(s) == 1 and ch_dict.get(s, 0) == 1:
            return True
        if len(ch_dict) == 1 and len(set(s)) == 1 and ch_dict.get(s[0], 0) == len(s):
            return True

        if s[0] not in ch_dict or ch_dict.get(s[0], 0) < 1:
            return False
        else:
            ch_dict[s[0]] -= 1
            r = self.dfs(ch_dict, s[1:])
            ch_dict[s[0]] += 1
            return r


so = Solution()
s = "aaaaaaaaa"
p = "aa"
print(so.findAnagrams(s, p))
