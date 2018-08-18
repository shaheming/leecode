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
        if len(set(s)) == 1 and set(s) == set(p):
            return [i for i in range(len(s) - len(p) + 1)]
        r = []
        ch_dict = self.get_ch_dict(p)
        p_len = len(p)
        s_len = len(s)
        i = 0
        while i < s_len - p_len + 1:
            for j in range(p_len):
                if j == p_len - 1 and ch_dict.get(s[i + j], 0) == 1:
                    r.append(i)
                    while i + p_len < s_len:
                        if s[i] != s[i + p_len]:
                            i += p_len - 2
                            break
                        i += 1
                        r.append(i)
                    ch_dict = self.get_ch_dict(p)
                    break
                if ch_dict.get(s[i + j], 0) < 1:
                    ch_dict = self.get_ch_dict(p)
                    break
                else:
                    ch_dict[s[i + j]] -= 1
            i += 1
        return r

    def get_ch_dict(self, p):
        ch_dict = {}
        for c in p:
            if ch_dict.get(c, None):
                ch_dict[c] += 1
            else:
                ch_dict[c] = 1
        return ch_dict

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
s = "acdcaeccde"
p = "c"
print(so.findAnagrams(s, p))
