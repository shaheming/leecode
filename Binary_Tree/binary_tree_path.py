# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#这道题在这里我没有很好我想用 conquer 的方法去做，结果就做成了 traverse 与 conquer 的结合体导致做的不太好。
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        return self.dfs(root, "%s" % root.val)

    def dfs(self, root, path):
        leftPaths = []
        rightPaths = []
        if root.left is None and root.right is None:
            return [path]
        if root.left:
            leftPaths = self.dfs(root.left, path + "->%s" % root.left.val)
        if root.right:
            rightPaths = self.dfs(root.right, path + "->%s" % root.right.val)
        return leftPaths + rightPaths




#这个是自底向上的方法
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.dfs(root)

    def dfs(self, root):
        paths = []
        if root is None:
            return paths
        if root.left is None and root.right is None:
            return ["%s" % root.val]

        leftPaths = self.dfs(root.left)
        for p in leftPaths:
            paths.append("%s" % root.val + "->" + p)
        rightPaths = self.dfs(root.right)
        for p in rightPaths:
            paths.append("%s" % root.val + "->" + p)
        return paths
