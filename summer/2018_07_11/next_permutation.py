# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         # find longest non-increasing suffix
#         right = len(nums)-1
#         while nums[right] <= nums[right-1] and right-1 >=0:
#             right -= 1
#         if right == 0:
#             return self.reverse(nums,0,len(nums)-1)
#         # find pivot
#         pivot = right-1
#         successor = 0
#         # find rightmost succesor
#         for i in range(len(nums)-1,pivot,-1):
#             if nums[i] > nums[pivot]:
#                 successor = i
#                 break
#         # swap pivot and successor
#         nums[pivot],nums[successor] = nums[successor],nums[pivot]
#         # reverse suffix
#         self.reverse(nums,pivot+1,len(nums)-1)
#


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        is_change = False
        try:
            for i in range(len(nums) - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                    if nums[i] > nums[j]:
                        tmp = nums[i]

                        is_change = True
                        for k in range(i, j-1,-1):
                            nums[k] = nums[k-1]
                        nums[j] = tmp
                        raise ()
        except Exception as e:
            print(e)

        if not is_change:
            self.reverse(nums, 0, len(nums)-1 )
        print(nums)


    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


s = Solution()
print(s.nextPermutation([3,2,1]))
