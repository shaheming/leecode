# -*- coding: utf-8 -*-
class Solution:
    def binary_search(self, nums, target):
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums)-1

        while (start + 1 < end):
            mid = (start + end) // 2
            if nums[mid] < target: 
              #注意如果取等这个将取到最右边的数并且配合最后面进行对比的
              #赋值start or end 是取得第一个点或者最后一个点的关键
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left, right = 0, len(nums) - 1

        print(left, right)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[-1]:
                if nums[mid] < target or target <= nums[-1]:
                    left = mid
                elif nums[mid] > target:
                    right = mid
            else:
                if nums[mid] > target or target > nums[-1]:
                    right = mid
                elif nums[mid] < target:
                    left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

nums = [1, 1, 1, 2]
target = 1

nums = [1, 3, 5]
target = 5
s = Solution()
print(s.search(nums, target))
