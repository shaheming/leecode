#看见一个用双栈的方法来实现不用每次排序的找最小。
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        try:
            return self.stack.pop()
        except:
            return None

    def top(self):
        """
        :rtype: int
        """
        try:
            return self.stack[-1]
        except:
            return

    def getMin(self):
        """
        :rtype: int
        """
        try:
            return min(self.stack)
        except:
            return


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
