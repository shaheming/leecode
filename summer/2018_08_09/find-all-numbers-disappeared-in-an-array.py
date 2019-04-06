class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = [0 for _ in range(len(nums))]
        for n in nums:
            r[n - 1] += 1
        return [i + 1 for i in range(len(r)) if r[i] == 0]
