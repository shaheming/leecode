#分两步走，第一步奖外面的总串的头保存用迭代 1 的方式进行迭代，然后在将其链接子啊仪器
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

        counter = 1
        preHead = ListNode(0)
        preHead.next = head
        pp = preHead
        while counter < m:
            pp = head
            head = head.next
            counter += 1

        p = head
        while counter < n:
            tmp = head.next
            head.next = tmp.next
            tmp.next = p
            p = tmp
            counter += 1
        pp.next = p
        return preHead.next
