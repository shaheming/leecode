#解题的思路是遍历一遍
#O(m+n)
class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rLen = len(matrix)
        cLen = len(matrix[0])
        i = 0
        while (i < cLen and rLen - 1 >= 0):
            if matrix[rLen - 1][i] == target:
                return True
            if matrix[rLen - 1][i] < target:
                i += 1
            else:
                rLen -= 1
        return False
