# https://leetcode.com/problems/battleships-in-a-board/description/
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
# In computing, a one-pass algorithm is a streaming algorithm which reads its input exactly once
# 思路: 分类讨论三种船 1. horizontal 2. vertical 3. only one poit
# 1. 在船尾时 只有左边有 X 2. 在船尾时只有上面有 X 3. 上下左右都没有 X. (越界也算没有 X) 通过这样的方式遍历一遍可以计算出
#  出错的问题没有考虑到 python 的 [a,b,c][-1] == c 而不是溢出报错
#
class Solution:
    def getShip(self, board, row, col):
        try:
            if row < 0 or col < 0:
                return '.'
            else:
                return board[row][col]
        except:
            return '.'

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        height = len(board)
        length = len(board[0])
        counter = 0
        for row in range(height):
            for col in range(length):
                if self.getShip(board, row, col) != "X":
                    pass
                else:
                    if self.getShip(board, row, col - 1) == "X" and \
                                    self.getShip(board, row, col + 1) == ".":
                        counter += 1
                    elif self.getShip(board, row - 1, col) == "X" and \
                                    self.getShip(board, row + 1, col) == '.':
                        counter += 1
                    elif self.getShip(board, row - 1, col) == "." and \
                                    self.getShip(board, row + 1, col) == '.' and \
                            self.getShip(board, row, col + 1) == '.' and \
                                    self.getShip(board, row, col - 1) == '.':
                        counter += 1
        return counter


s = Solution()
r = s.countBattleships([["X", "X", "X"]])
print(r)
