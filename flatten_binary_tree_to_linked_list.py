# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        stack = [root]
        res = []
        while stack:
            p = stack.pop()
            res.append(p)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)

        root = res[0]
        p = root
        for node in res[1:]:
            p.right = node
            p.left = None
            p = node
        p.right = None
        p.left = None
    #在前序遍历的过程中就将树的结构都改变了
    def flatten2(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        stack = [root]
        tmp_root = None
        while stack:
            p = stack.pop()
            if tmp_root is None:
                tmp_root = p
            else:
                tmp_root.left = None
                tmp_root.right = p
                tmp_root = p
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
