import collections


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        index = len(nums) - 1
        queue = collections.deque([[]])
        while index >= 0:
            for _ in range(len(queue)):
                p = queue.popleft()
                queue.append(p)
                queue.append(p+[nums[index]])
            index -= 1

        return list(queue)

# This use dfs
# class Solution:
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """

#         res = []
#         self.dfs(nums, [], 0, res)
#         return res


#     def dfs(self, nums, path, index, res):
#         res.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, path+[nums[i]], i+1, res)

