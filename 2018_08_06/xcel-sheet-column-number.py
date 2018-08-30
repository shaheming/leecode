# convert hexdecimal to decimal
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i in s:
            r = ord(i) - ord('A') + 1 + r * 26
        return r
