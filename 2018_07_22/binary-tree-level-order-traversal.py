# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路: 用队列
class Solution:

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        parents = []
        children = []
        parents.append(root)
        while len(parents) > 0 and len(children) == 0:
            r = []
            for p in parents:
                r.append(p.val)
                if p.left is not None:
                    children.append(p.left)
                if p.right is not None:
                    children.append(p.right)
            result.append(r)
            parents = children
            children = []
        return result

