import copy


# 这里踩了一个经典的皇后问题的坑
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.size = n
        line = ["."] * n
        self.board = [line.copy() for _ in range(self.size)]
        self.visit_row(0)
        return [["".join(l) for l in i] for i in self.result]

    def visit_row(self, line):
        col = 0
        while col < self.size:
            if self.checkValid(line, col):
                self.board[line][col] = "Q"
                if line == self.size - 1:
                    self.printBoard()
                    self.result.append(copy.deepcopy(self.board))
                    self.board[line][col] = "."
                    return
                else:
                    self.visit_row(line + 1)
                self.board[line][col] = "."
            col += 1

    # 搜索空间的上下左右是一个难点
    def checkValid(self, row, col):
        for c in range(self.size):
            # 上下
            if self.board[row][c] == "Q" or self.board[c][col] == "Q":
                return False
            # 左上左下
            # col = row + b => b = col_1 - row_1 => col = row + (col_1 - row_1)
            # col = -row + b => b = col_1 + row_1 => col = - row + (col_1 + row_1)
            # 之后需要考虑边界问题
            for r_1, c_1 in [[c, row + col - c], [c, c + (col - row)]]:
                print(r_1, c_1)
                if r_1 >= 0 and \
                        c_1 >= 0 and \
                        r_1 < self.size and \
                        c_1 < self.size and \
                        self.board[r_1][c_1] == "Q":
                    return False

        return True

    def printBoard(self):
        for col in self.board:
            print(col)
        print("==")


#
s = Solution()
r = s.solveNQueens(4)
print(r)


def test(row, col):
    size = 5
    for c in range(size):
        for r_1, c_1 in [[c, row + col - c], [c, c + (col - row)]]:
            if r_1 >= 0 and c_1 >= 0 and r_1 < size and c_1 < size:
                print(r_1, c_1)


test(1, 0)
