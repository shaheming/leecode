class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        if n <= 9: return n
        base = 9
        while n - base * i > 0:
            n -= base * i
            base *= 10
            i += 1
        base //= 10
        num = (10 ** (i - 1)) - 1 + n // i
        p = n % i
        if p == 0:
            return int(str(num)[-1])
        else:
            return int(str(num + 1)[p - 1])


s = Solution()
print(s.findNthDigit(999999999))
print(s.findNthDigit(11))
