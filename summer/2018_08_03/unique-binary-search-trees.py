class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:return 0
        nums = [0 for _ in range(n+1)]
        nums[0]=1
        nums[1]=1
        for i in range(2,n+1):
            for k in range(0,i):
                nums[i] += nums[i-k-1]*nums[k]
        return nums[n]


#注意转移方程
#SUM[I]*[I-K-1]