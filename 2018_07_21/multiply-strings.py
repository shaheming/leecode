class Solution:
    def mul(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        r = ""
        n2 = int(num2)
        for i in range(1, len(num1) + 1):
            tmp = str(int(num1[-i]) * n2)
            if r == "":
                r = tmp
            else:
                if tmp != '0':
                    r = self.add(tmp + "0" * (i - 1), r)
        return r

    def add(self, num1, num2):
        length = max([len(num1), len(num2)])
        r = ['0'] * (length + 1)
        len1 = len(num1)
        len2 = len(num2)
        up = 0
        for i in range(1, length + 2):
            if i <= len1:
                n1 = int(num1[-i])
            else:
                n1 = 0
            if i <= len2:
                n2 = int(num2[-i])
            else:
                n2 = 0
            r[-i] = str((up + n1 + n2) % 10)
            up = (up + n1 + n2) // 10
        if r[0] == '0':
            return "".join(r[1:])
        else:
            return "".join(r)

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = max(num1, num2)
        n2 = min(num1, num2)
        r = ""
        for i in range(1, len(n2) + 1):
            tmp = self.mul(n1, n2[-i])
            if r == "":
                r = tmp
            else:
                if tmp != '0':
                    r = self.add(tmp + "0" * (i - 1), r)
        return r

    # 思路用一个数字来存储结果
    # 需要注意的是进位问
    # 两个数相乘最大的结果的长度 = len(num1) + len(num2)
    def multiply2(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        product = [0] * (len(num1) + len(num2))
        position = len(product) - 1
        for n1 in num1[::-1]:
            tmposition = position
            for n2 in num2[::-1]:
                product[tmposition] += int(n1) * int(n2)
                product[tmposition - 1] += product[tmposition] // 10
                product[tmposition] %= 10
                tmposition -= 1
            position -= 1
        if product[0] == 0:
            product = product[1:]
        return "".join([str(p) for p in product])


s = Solution()
print(s.multiply2("123", "456"))
print(s.multiply("123", "456"))
