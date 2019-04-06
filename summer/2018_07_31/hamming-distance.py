class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        p = total // 2
        dp = [False for _ in range(total + 1)]
        dp[0] = True
        for n in nums:
            for i in range(total, -1, -1): #注意这里是倒叙加，要不然会出现重复相加
                if dp[i]: dp[i + n] = True
            if dp[p]:
                return True
        return False


nums = [2, 7, 9, 12]
s = Solution()
s.canPartition(nums)
