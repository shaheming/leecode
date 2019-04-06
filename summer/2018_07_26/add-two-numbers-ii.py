# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        stack1 = []
        stack2 = []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next

        up = 0

        for _ in range(max([len(stack1), len(stack2)]) + 1):
            if stack1:
                n1 = stack1.pop()
            else:
                n1 = 0
            if stack2:
                n2 = stack2.pop()
            else:
                n2 = 0
            tmp = n1 + n2 + up
            up = tmp // 10
            res.append(tmp % 10)

        if res[-1] == 0:
            res.pop()
        print(res)

        p = head = ListNode(res.pop())
        while res:
            p.next = ListNode(res.pop())
            p = p.next
        return head
