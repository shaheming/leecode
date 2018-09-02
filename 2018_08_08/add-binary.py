class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if int(a) + int(b) == 0:
            return '0'
        result = [None] * (len(a) + len(b))
        a = (len(result) - len(a)) * "0" + a
        b = (len(result) - len(b)) * "0" + b
        up = 0
        for i in range(len(result) - 1, -1, -1):
            result[i] = str((int(a[i]) + int(b[i]) + up) % 2)
            up = (int(a[i]) + int(b[i]) + up) // 2

        index = 0

        while result[index] == "0" and index < len(result):
            index += 1
        return "".join(result[index:])
# 字符串的加法注意处理 0 的情况
