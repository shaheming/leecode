class Solution:
    def findAncestor(self, d, array):
        if len(array) == 0:
            return []

        res = []

        for i in range(len(array)):
            ancestoryCount = 1
            p = array[i]
            while ancestoryCount < d:
                if p == -1:
                    break
                else:
                    p = array[p]
                ancestoryCount += 1
            res.append(p)
        return res


array = [-1, 0, 0, 1, 1,2,2,3,3,4,9]
d = 1
s = Solution()
r = s.findAncestor(d, array)
print(r)
