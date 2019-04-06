# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root]]
        r = None
        while stack:
            levels = stack.pop()
            r = levels[0]
            tmp = []
            for l in levels:
                if l.left:
                    tmp.append(l.left)
                if l.right:
                    tmp.append(l.right)
            if tmp:
                stack.append(tmp)
        return r.val
