# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[1]

    def dfs(self, root):
        if root is None:
            return 0, True

        if root.left is None and root.right is None:
            return 1, True

        leftHeight, leftIsBalance = self.dfs(root.left)

        rightHeight, rightIsBalance = self.dfs(root.right)

        return max(leftHeight, rightHeight) + 1, leftIsBalance and rightIsBalance and abs(leftHeight - rightHeight) <= 1



