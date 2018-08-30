class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3: return False
        n = (len(num) - 1) // 2
        for i in range(1, n + 1):
            num1 = num[:i]
            if num1[0] == '0' and len(num1) > 1:
                break
            for j in range(1, n + 1):
                num2 = num[i:i + j]
                num1 = num[:i]
                if num2[0] == '0' and len(num2) > 1:
                    break
                subStr = num[i + j:]
                while subStr and subStr.find(str(int(num2) + int(num1))) == 0:
                    tmp = num2
                    num2 = str(int(num2) + int(num1))
                    num1 = tmp
                    subStr = subStr[len(num2):]
                if len(subStr) == 0 and (i + j) < len(num):
                    return True
        return False
