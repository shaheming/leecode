class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # [col_0, col_1, col_2, col_3] to store result and try to put the queue row by row
        r = []
        path = [None for _ in range(n)]
        self.dfs(path, 0, r, n)
        res = []
        for p in r:
            tmp = []
            for col in p:
                tmp.append("." * col + "Q" + "." * (n - col - 1))
            res.append(tmp)
        return res

    def dfs(self, path, row, res, n):
        if row == n:
            res.append(path)
            return
        for c in range(n):
            if self.isAvailable(row, c, path):
                self.dfs(path[:row] + [c] + path[row+1:], row+1, res, n)

    def isAvailable(self, row, col, path):
        for index, c in enumerate(path):
            if c is not None:
                if index == row or c == col or index - c + col == row or index + c - col == row:
                    return False
        return True
