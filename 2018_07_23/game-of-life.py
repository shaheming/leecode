#思路: 这是一个矩阵序列周围遍历问题，主要考虑四周的相邻的格子的边界问题
#用其他符号保存信息
#需要注意边界 >= 0 的问题
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rLen = len(board)
        cLen = len(board[0])
        direction = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
        for row in range(rLen):
            for col in range(cLen):
                countLive = 0
                for i, j in direction:
                    r = row + i
                    c = col + j
                    if r >= 0 and c >= 0 and r < rLen and c < cLen and (board[r][c] == 1 or board[r][c] == '@'):
                        countLive += 1
                if board[row][col] == 1 and countLive not in [2, 3]:
                    board[row][col] = '@'
                if board[row][col] == 0 and countLive == 3:
                    board[row][col] = '#'
                # print(board,countLive,row,col)
        for row in range(rLen):
            for col in range(cLen):
                if board[row][col] == '#':
                    board[row][col] = 1
                if board[row][col] == "@":
                    board[row][col] = 0
