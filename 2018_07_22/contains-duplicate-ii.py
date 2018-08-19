class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """


        position = {}
        for i in range(len(nums)):
            if nums[i] not in position:
                position[nums[i]]=[i]
            else:
                if i - position[nums[i]][-1] <= k:
                    return True
                else:
                    position[nums[i]].append(i)
        return False
