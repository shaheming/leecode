# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        r= self.bfs(1,n)
        print(r)
        return r


    def bfs(self,min,max):
        result = []
        if min > max:
            return result
        for rt in range(min,max+1):
            lefts = self.bfs(min,rt-1)
            rights = self.bfs(rt+1,max)
            if len(lefts) == 0 and len(rights) == 0:
                root= TreeNode(rt)
                result.append(root)
            elif len(lefts) == 0:
                for right in rights:
                    root = TreeNode(rt)
                    root.right = right
                    result.append(root)
            elif len(rights)==0:
                for left in lefts:
                    root = TreeNode(rt)
                    root.left = left
                    result.append(root)
            else:
                for left in lefts:
                    for right in rights:
                        root = TreeNode(rt)
                        root.left = left
                        root.right = right
                        result.append(root)

        return result


#这个题有个坑，他其实只是要求返回结果的 root 的 list