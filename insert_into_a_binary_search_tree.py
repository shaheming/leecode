# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这道题的思路是通过 Binary search tree, you will find a leave that you can put the
# node on the left or on the right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    #这是一种非递归的写法，二叉搜索树有个一性质·
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        start = None
        p = root
        while (p is not None):
            start = p
            if p.val < val:
                p = p.right
            else:
                p = p.left

        if val < start.val:
            start.left = TreeNode(val)
        else:
            start.right = TreeNode(val)
        return root
