# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        pathP, pathQ = [root], [root]
        self.findPath(root, pathP, p)
        self.findPath(root, pathQ, q)
        if p in pathQ:
            return p
        if q in pathP:
            return q
        # print([n.val for n in pathP],[n.val for n in pathQ])
        for node in pathQ[::-1]:
            if node in pathP:
                return node

    def findPath(self, root, path, target):
        if root == target:
            return True
        if root.left:
            path.append(root.left)
            r = self.findPath(root.left, path, target)
            if r:
                return True
            else:
                path.pop()
        if root.right:
            path.append(root.right)
            r = self.findPath(root.right, path, target)
            if r:
                return True
            else:
                path.pop()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # If p, q is under the root, then return low(p, q)
    # If only p is the descendant of root then return p
    # If only q is the descendant of root then return q
    # If neither p nor q is descendant of the root return None.
    # The keypoint there is bring the info of p, q from leave to root.
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left

        if right is not None:
            return right

        return None

