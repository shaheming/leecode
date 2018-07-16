# https://leetcode.com/problems/power-of-three/description/
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0 or n % 3 != 0:
            return False


        tmp = n
        while tmp > 1 and tmp % 3 == 0:
            tmp = tmp // 3
            if tmp == 1:
                return True

        return False

s=Solution()
print(s.isPowerOfThree(1))