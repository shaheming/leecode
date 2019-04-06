#通过位匹配的方式寻找区分
# xor ALL num IF DUC GET 0
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        mask = 1
        while (mask & xor == 0): mask = mask << 1
        a = b = 0
        for num in nums:
            if mask & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
