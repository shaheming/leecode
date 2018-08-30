class Solution:

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        self.dp = [[0 for _ in range(n)] for _ in range(n)]
        return self.getScore(nums, 0, n - 1) >= 0

    def getScore(self, nums, l, r):
        if l == r:
            return nums[l]
        if self.dp[l][r] > 0:
            return self.dp[l][r]
        self.dp[l][r] = max(nums[l] - self.getScore(nums, l + 1, r), nums[r] - self.getScore(nums, l, r - 1))
        return self.dp[l][r]
