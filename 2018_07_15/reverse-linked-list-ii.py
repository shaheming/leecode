# https://leetcode.com/problems/reverse-linked-list-ii/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        tmpHead = ListNode(0)
        tmpNode = ListNode(0)
        tmpPre = ListNode(0)
        fakeHead = ListNode(0)
        fakeHead.next = head
        tmpNode.next = fakeHead

        # find m - 1
        for _ in range(m - 1):
            tmpNode.next = tmpNode.next.next

        # 头
        tmpHead = tmpNode.next
        tmpEnd = None
        pointer = tmpNode.next.next
        for _ in range(m, n + 1):
            print("pointer:", pointer.val)
            if tmpEnd is None:
                tmpEnd = pointer
            tmp = tmpPre.next
            tmpPre.next = pointer
            tmpHead.next = pointer.next
            pointer = pointer.next
            tmpPre.next.next = tmp

        tmpEnd.next = pointer
        tmpHead.next = tmpPre.next

        return fakeHead.next


def print_list(listNode):
    r = [listNode.val]
    pointer = listNode.next
    while pointer is not None:
        r.append(pointer.val)
        pointer = pointer.next
    print(r)


data = [1, 2, 3, 4, 5]
head = ListNode(data[0])
pointer = head
for i in data[1:]:
    pointer.next = ListNode(i)
    pointer = pointer.next

print_list(head)
s = Solution()
print_list(s.reverseBetween(head, 1, 4))
