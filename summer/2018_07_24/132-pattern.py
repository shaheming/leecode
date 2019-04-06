class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        s3 = -float('inf')
        for n in nums[::-1]:
            if s3 > n:
                return True
            while len(stack) > 0 and n > stack[-1]:
                s3 = stack.pop()
            stack.append(n)
        return False