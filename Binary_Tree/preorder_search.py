# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        if root is None:
            return r
        stack = [root]
        while stack:
            node = stack.pop()
            r.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return r

    
    def inorderTraversal(self, root):
        r = []
        if root is None:
            return r
        stack = []
        p = root
        while p is not None or stack:
            while p is not None:
                stack.append(p)
                p = p.left
            p = stack.pop()
            r.append(p.val)
            p = p.right
        return r




