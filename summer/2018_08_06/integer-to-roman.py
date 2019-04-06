class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map = {1: "I",
               5: "V",
               10: "X",
               50: "L",
               100: "C",
               500: "D",
               1000: "M",
               4: "IV",
               9: "IX",
               40: "XL",
               90: "XC",
               400: "CD",
               900: "CM"}

        divces = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        r = ""
        for d in divces:
            if num >= d:
                n = num // d
                remain = num % d
                r += map[d] * n
                num = remain
        return r

s=Solution()
print(s.intToRoman(1994))
