# sum[i]−sum[j]=k
# 这里的思想是通过将sum值作为参考
# 这里最巧妙的用法是 upto two indices is the same, the sum of the elements lying in between those indices is zero.
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        length = len(nums)
        array = {}
        for i in range(len(nums) - 1, -1, -1):
            for index in range(length - i):
                sum = array.get(index, 0)
                array[index] = nums[i] + sum
                if array[index] == k:
                    counter += 1
        return counter

    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = sum = 0
        map = {}
        map[0] = 1#这个也非常重要是用来处理结尾=k的情况
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in map:
                count += map[sum - k]
            map[sum] = map.get(sum, 0) + 1
        return count
