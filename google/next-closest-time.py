class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        t = time[:2] + time[3:]
        digits = set(t)
        times = self.getCombinations(list(digits))

        minDistance = float('inf')
        minPostion = 0

        for index, time in enumerate(times):
            diff = self.sub(t, time)
            if diff < minDistance:
                minDistance = diff
                minPostion = index

        outTime = times[minPostion][:2] + ":" + times[minPostion][2:]
        return outTime

    def sub(self, t1, t2):

        time1 = int(t1[:2]) * 60 + int(t1[2:])
        time2 = int(t2[:2]) * 60 + int(t2[2:])
        if time1 >= time2:
            return time2 - time1 + 24 * 60
        else:
            return time2 - time1

    def getCombinations(self, digits):
        res = []
        for d1 in digits:
            if int(d1) > 2:
                continue
            for d2 in digits:
                if int(d1) == 2 and int(d2) > 3:
                    continue
                for d3 in digits:
                    if int(d3) > 5:
                        continue
                    for d4 in digits:
                        res.append(d1+d2+d3+d4)
        return res
