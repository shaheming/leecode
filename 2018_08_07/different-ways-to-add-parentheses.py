class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.dp = {}
        return self.sub(input)

    def sub(self, input):
        op_p = []
        r = []
        for i, e in enumerate(input):
            if e in ["*", "+", "-"]:
                op_p.append(i)
        if len(op_p) == 1:
            return [self.helper(input[:op_p[0]], input[op_p[0] + 1:], input[op_p[0]])]
        if len(op_p) == 0:
            return [int(input)]

        for i in op_p:
            if input[:i] in self.dp:
                A = self.dp[input[:i]]
            else:
                A = self.sub(input[:i])
                self.dp[input[:i]] = A
            if input[i + 1:] in self.dp:
                B = self.dp[input[i + 1:]]
            else:
                B = self.sub(input[i + 1:])
                self.dp[input[i + 1:]] = B
            for a in A:
                for b in B:
                    r.append(self.helper(a, b, input[i]))
        return r

    def helper(self, num1, num2, op):
        if op == "*":
            return int(num1) * int(num2)
        elif op == "-":
            return int(num1) - int(num2)
        elif op == "+":
            return int(num1) + int(num2)
