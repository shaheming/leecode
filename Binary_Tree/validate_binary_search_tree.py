# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这道题的思路是当返回值太多的时候，通过传入尝试的方式来进行判断。
# 或者是用中序遍历一次然后看生成的数组是否是一个递增的序列
# 这是遍历和递归的方法相结合


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, None, None)

    def dfs(self, root, minVal, maxVal):
        if root is None:
            return True
        if (minVal is not None and root.val <= minVal) or (maxVal is not None and root.val >= maxVal):
            return False
        return self.dfs(root.left, minVal, root.val) and self.dfs(root.right, root.val, maxVal)

    def isValidBST(self, root):
        if root is None:
            return True
        stack, res = [], []
        p = root
        while p is not None or stack:
            while p is not None:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right

        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False
        return True



