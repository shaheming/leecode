class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        map = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
               20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
               100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"}
        divs = [1000000000, 1000000, 1000, 1]
        result = ""
        for div in divs:
            if num >= div:
                quotient = num // div
                remaind = num % div
                quotient_1 = quotient // 100
                remaind_1 = quotient % 100
                tmp = ""
                if quotient_1 != 0:
                    tmp = tmp + map[quotient_1] + " " + map[100] + " "
                if remaind_1 > 0:
                    if remaind_1 < 20:
                        tmp = tmp + map[remaind_1] + " "
                    else:
                        quotient_1 = remaind_1 // 10
                        remaind_1 = remaind_1 % 10
                        tmp = tmp + map[quotient_1 * 10] + " "
                        if remaind_1 != 0:
                            tmp = tmp + map[remaind_1] + " "
                result = result + tmp
                if div != 1:
                    result = result + map[div] + " "
                num = remaind

        return result[:-1] if result[-1] == " " else result
s=Solution()
print(s.numberToWords(100001))