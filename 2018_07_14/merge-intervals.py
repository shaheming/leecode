# Definition for an interval.
#https://leetcode.com/problems/merge-intervals/description/
# if len(intervals) == 0:
#     return []
# 错误没有考虑 等于 0 的边界情况
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e



class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda item: item.start)
        index = 0
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= result[index].end:
                result[index].end = max(result[index].end, interval.end)
            else:
                result.append(interval)
                index += 1
        return [[interval.start, interval.end] for interval in result]


s = Solution()
intervals = [[1,4],[4,5]]
r = s.merge([Interval(start, end) for start, end in intervals])
print(r)
