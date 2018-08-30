class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = index = 0

        while True:
            while index < len(nums) and nums[index] == val:
                index += 1

            if index >= len(nums):
                break

            nums[p] = nums[index]
            index += 1
            p += 1

        return p