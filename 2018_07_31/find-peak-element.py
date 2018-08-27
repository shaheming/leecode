class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.bs(nums, 0, len(nums) - 1)

    def bs(self, nums, l, h):
        if l == h: return l
        mid = (l + h) // 2
        if nums[mid] > nums[mid + 1]:
            return self.bs(nums, l, mid)
        else:
            return self.bs(nums, mid + 1, h)

# 等价问题,用二分查找法
# 那为什么可以用二分查找法呢?
# 这是因为如何 mid <= 右边 说明 peak 在右边 else peak 在 左边

