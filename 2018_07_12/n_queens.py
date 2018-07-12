import copy


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
            if self.avaliable(line, col):
                self.board[line][col] = "Q"
                if line == self.size - 1:
                    self.result.append(copy.deepcopy(self.board))
                    self.board[line][col] = "."
                    return
                else:
                    self.visit_row(line + 1)
                self.board[line][col] = "."
            col += 1

    def avaliable(self, row, col):
        for c in range(self.size):
            if self.board[row][c] == "Q" or self.board[c][col] == "Q":
                return False
            for r_1, c_1 in [[1 * c + row, 1 * c + col],
                             [1 * c + row, -1 * c + col],
                             [-1 * c + row, 1 * c + col],
                             [-1 * c + row, -1 * c + col]]:

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


s = Solution()
r = s.solveNQueens(4)
print(r)
