class Solution:
    def findClosest(self, hourses, stores):
        if len(hourses) == 0 or len(stores) == 0:
            return []
        stores = sorted(stores)
        print(stores)
        hourseDis = {}
        res = []
        for index, hourse in enumerate(hourses):
            if hourse in hourseDis:
                res.append(hourseDis[hourse])
                continue
            else:
                hourseDis[hourse] = self.find(hourse, stores)
                res.append(hourseDis[hourse])
        return res

    def find(self, hourse, stores):
        start, end = 0, len(stores) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if stores[mid] < hourse:
                start = mid
            else:
                end = mid
        print(stores[start], stores[end], hourse)
        if abs(stores[start] - hourse) <= abs(stores[end] - hourse):
            
            return stores[start]
        else:
            return stores[end]


hourses = [5, 10, 17]
stores = [1, 5, 3, 7, 13, 20, 11, 12,10,16]
s = Solution()
r = s.findClosest(hourses, stores)
print(r)
