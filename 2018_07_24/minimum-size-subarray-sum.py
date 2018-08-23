class Solution:
#双指针的 O(N) 用于子序列查找
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = total = 0
        r = float('inf')
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                r = min([r, right - left + 1])
                total -= nums[left]
                left += 1
        if r > len(nums):
            return 0
        else:
            return r
#累积和
    def minSubArrayLen2(self, s, nums):
        r = float('inf')
        for index, num in enumerate(nums[1:], 1):
            nums[index] = nums[index - 1] + num
        left = 0
        for right, num in enumerate(nums):
            if num >= s:
                left = self.find_left(left, right, nums, s, num)
                r = min(r, right - left + 1)
        return r

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left
