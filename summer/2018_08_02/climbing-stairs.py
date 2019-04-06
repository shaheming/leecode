class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:return 0
        if n== 1: return 1
        if n == 2:return 2
        step1= 1
        step2 = 2
        r=0
        for _ in range(n-2):
            r = step1+step2
            step1=step2
            step2=r
        return r



