class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.tmp_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        # self.tmp_stack.append(None)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.stack) > 0:
            self.tmp_stack.append(self.stack.pop())
        r = self.tmp_stack.pop()
        while len(self.tmp_stack) > 0:
            self.stack.append(self.tmp_stack.pop())
        return r

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.stack) > 0:
            self.tmp_stack.append(self.stack.pop())
        r = self.tmp_stack[-1]
        while len(self.tmp_stack) > 0:
            self.stack.append(self.tmp_stack.pop())
        return r

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0