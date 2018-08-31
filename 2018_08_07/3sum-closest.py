class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        total = nums[0] +nums[1] + nums[2]
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j < k:
                r = nums[i] +nums[j] + nums[k]
                if r == target:
                    return r
                if abs(target - r) < abs(target - total):
                    total = r
                if r < target:
                    j+=1
                elif r > target:
                    k-=1
        return total


# a, b , c, d, e, f, g, h
# 
# a,b,h
# 
# if target > abh
# 
# sum = a+b+g
# 
# if target > sum:
# 
# sum = a+b+f
# 
# if target < sum:
# 
# sum = a+c+f
# 
# if target < sum:
# 
# sum = a + d + f or sum = a+c+g
# 
# 但是因为题目中有说， input would have exactly one solution, 所以只可能有一种情况

s=Solution()
print(s.threeSumClosest([0,1,2],1))