# 最暴力的方法是 排列组合  all unique triplets
import json
import time


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_set = set()
        nums_dict = {}
        length = len(nums)
        tow_sum_dict = {}
        start_time = time.time()
        for i in range(length):
            num = nums[i]
            nums_dict[num] = nums_dict.get(num, 0) + 1
            for j in range(i + 1, length):
                num2 = nums[j]
                pair = tuple(sorted([num, num2]))
                pair_sum = sum(pair)
                pairs = tow_sum_dict.get(pair_sum, set())
                pairs.add(tuple(pair))
                tow_sum_dict[pair_sum] = pairs
        print(time.time() - start_time)
        start_time = time.time()
        for k, v in tow_sum_dict.items():
            if -k in nums_dict:
                for pair in v:
                    if nums_dict[-k] - sum([1 for i in pair if -k == i]) - 1 >= 0:
                        result_set.add(tuple(sorted(list(pair) + [-k])))
        print(time.time() - start_time)
        return [list(i) for i in result_set]

    def threeSums2(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                l , r = i + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == -nums[i]:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1; r -= 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                        while l < r and nums[r] == nums[r+1]: r -= 1
                    elif nums[l] + nums[r] < -nums[i]:
                        while l < r:
                            l += 1
                            if nums[l] > nums[l-1]: break
                    else:
                        while l < r:
                            r -= 1
                            if nums[r] < nums[r+1]: break
        return res

with open("3sum.json", "r") as f:
    nums = json.loads(f.read())
s = Solution()

print(s.threeSum(nums))
