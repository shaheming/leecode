# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val :
            p,q = q,p
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = root
        while parent.left or parent.right:
            if p.val == parent.val or q.val == parent.val or (p.val < parent.val and q.val > parent.val):
                return parent
            if q.val < parent.val:
                parent = parent.left
            if p.val > parent.val:
                parent = parent.right

