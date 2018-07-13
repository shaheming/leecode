# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 如果父节点加上兄弟 < O
# 1. root > 0
# 1.1 left+root 2 left + right 3. left+right+root(left>0 and right > 0)
# 2. root < 0
# 1. left 2. right 如果 root < -MAX 子节点，需要考虑子节点是否大于 global max 如果是替换 3 left+right+root
# 注意质量是求 path
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.global_max = float("-inf")
        self.find_max(root)
        print(self.global_max)
        return self.global_max

    def find_max(self, root):
        if root is None:
            return 0
        left_val = self.find_max(root.left)
        right_val = self.find_max(root.right)
        root_val = root.val
        self.global_max = max(root_val + left_val + right_val, self.global_max)
        return max(0, root.val + max(left_val, right_val))
