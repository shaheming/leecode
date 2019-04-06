class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        index = 0
        chDic = {}
        maxCount = 0
        for i in range(len(s)):
            if len(chDic) < 2:
                chDic[s[i]] = chDic.get(s[i], 0) + 1
            else:
                if s[i] in chDic:
                    chDic[s[i]] += 1
                else:
                    maxCount = max(maxCount, sum(chDic.values()))
                    index = i - 1
                    tmp = s[index]
                    while index > 0 and s[index - 1] == tmp:
                        index -= 1
                    chDic = {s[i-1]: i - index}
                    chDic[s[i]] = 1
        return max(maxCount, sum(chDic.values()))
