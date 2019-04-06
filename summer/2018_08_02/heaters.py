class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for h in sorted(houses):
            while h >= sum(heaters[i:i + 2]) / 2:
                i += 1
            r = max(r, abs(heaters[i] - h))
        return r
#思路是遍历问题？
#这道题是一道蛮有意思的题目，首先我们看题目中的例子，不管是houses还是heaters数组都是有序的，所以我们也需要给输入的这两个数组先排序，以免其为乱序。我们就拿第二个例子来分析，我们的目标是houses中的每一个数字都要被cover到，那么我们就遍历houses数组，对每一个数组的数字，我们在heaters中找能包含这个数字的左右范围，
# 然后看离左右两边谁近取谁的值，如果某个house位置比heaters中最小的数字还小，那么肯定要用最小的heater去cover，反之如果比最大的数字还大，就用最大的数字去cover。