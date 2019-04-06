class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0

        while True:
            while p2 < len(nums) and nums[p2] == 0:
                p2 += 1
            if p2 >= len(nums):
                break
            else:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1

        for i in range(p1, len(nums)):
            nums[i] = 0
