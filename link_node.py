class Node:
    def __init__(self, v=None, next_node=None):
        self.value = v
        self.next_node = next_node


class Solution:

    def check(self, s):
        head = Node()
        tail = head
        cur = tail
        for ch in s:
            if ch == "[":
                cur = head
                continue
            elif ch == "]":
                cur = tail
                continue
            node = Node(ch, cur.next_node)
            cur.next_node = node
            if cur == tail:
                tail = node
            cur = node
        l = []
        c = head.next_node
        while c:
            l.append(c.value)
            c = c.next_node
        return "".join(l)


s = "This_is_a_[Beiju]_text"
s = "[[]][][]Happy_Birthday_to_Tsinghua_University"
s1 = Solution()
print(s1.check(s))
