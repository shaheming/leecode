class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            if (target - num) in nums:
                if num == target - num:
                    try:
                        start = nums.index(num)
                        return [nums.index(num), nums.index(num, start+1)]
                    except:
                        pass
                else:
                    return [nums.index(num), nums.index(target - num)]


s = Solution()
print(s.twoSum([2, 5, 5, 11], 10))
