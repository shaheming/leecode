class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_set = {}

        for c in s:
            if c in ch_set:
                ch_set[c]+=1
            else:
                ch_set[c]=1


        for i in range(len(s)):
            if ch_set[s[i]] == 1:
                return i

        return -1