class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # a + b + c + d == target
        # (a + b + c) + d == target
        # four combanation and hash map
        res = []

        self.findNSum(3, nums, target, [], res)
        return res

    def findNSum(self, n, nums, target, path, res):
        if n < 2 and len(nums) >= 2:
            start, end = 0, len(nums) - 1

            while start < end:
                total = nums[start] + nums[end]
                if total == target:
                    res.append(path + [nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif total < target:
                    start += 1
                else:
                    end -= 1
        else:
            i = 0
            while i < len(nums) - n:
                self.findNSum(n-1, nums[i+1:], target -
                              nums[i], path+[nums[i]], res)
                i += 1
                while i < len(nums) - n and nums[i] == nums[i-1]:
                    i += 1


s = Solution()
print(s.fourSum([-5, -4, -2, -2, -2, -1, 0, 0, 1], -9))
