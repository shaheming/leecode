class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == '0': return 0
        self.my_way = {}
        self.decode(s)

        return self.my_way[s]

    def decode(self, s):
        if self.my_way.get(s, None): return self.my_way[s]
        if s[0] == '0': return 0
        if len(s) == 1:
            self.my_way[s] = 1
            return 1

        w = self.decode(s[1:])

        if int(s[:2]) <= 26:
            if len(s) == 2:
                w += 1
            else:
                w += self.decode(s[2:])

        self.my_way[s] = w
        return self.my_way[s]
# 这道题的思想是类似斐波拉西数列 r[i] = r[i-1] + r[i-2]
# 可以用搜索已经扫描过的子串来进行剪枝操作
