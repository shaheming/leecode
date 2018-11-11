class Solution:
    def findClosest(self, hourses, stores):
        if len(hourses) == 0 or len(stores) == 0:
            return []
        sorted(hourses)
        sorted(stores)
        res = []
        for index, hourse in enumerate(hourses):
            if index != 0 and hourse == hourses[index - 1]:
                res.append(res[index - 1])
                continue
            else:
                res.append(self.find(hourse, stores))
        return res

    def find(self, hourse, stores):
        start, end = 0, len(stores) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if stores[mid] < hourse:
                start = mid
            else:
                end = mid
        if abs(stores[start] - hourse) < abs(stores[end] - hourse):
            return stores[start]
        else:
            return stores[end]


hourses = [2,4,3, 6, 12, 18]
stores = [5,5,5,5,5, 8, 9, 20]
s = Solution()
r = s.findClosest(hourses, stores)
print(r)
