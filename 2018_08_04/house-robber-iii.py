# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dp = [{}, {}]
        if root is None: return 0
        return max(self.dfs(root, True), self.dfs(root, False))

    def dfs(self, root, p):
        if root.left is None and root.right is None:
            if p:
                return 0
            else:
                return root.val

        l = r = l1 = r1 = 0

        if root.left:
            if root.left in self.dp[0]:
                l = self.dp[0][root.left]
            else:
                l = self.dfs(root.left, False)
                self.dp[0][root.left] = l
        if root.right:
            if root.right in self.dp[0]:
                r = self.dp[0][root.right]
            else:
                r = self.dfs(root.right, False)
                self.dp[0][root.right] = r
        if p:
            return l + r
        else:
            if root.left:
                if root.left in self.dp[1]:
                    l1 = self.dp[1][root.left]
                else:
                    l1 = self.dfs(root.left, True)
                    self.dp[1][root.left] = l1
            if root.right:
                if root.right in self.dp[1]:
                    r1 = self.dp[1][root.right]
                else:
                    r1 = self.dfs(root.right, True)
                    self.dp[1][root.right] = r
            return max(root.val + l1 + r1, l + r)
#dp 问题，用计划递归剪枝