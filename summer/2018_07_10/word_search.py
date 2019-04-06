# https://leetcode.com/problems/word-search/description/
# 属于搜索题
# 自己犯的错误: The same letter cell may not be used more than once. 忘记了条件
# 这里有一个经典的递归的复原写法
# def a(c):
#     print(c)
#     if len(c) == 10:
#         return
#     c.append(len(c))
#     a(c)
#     print("pop", c.pop())
#
#
# def b():
#     a([])
#通过这样的方式在递归结束时能将改动逆向回去


class Solution:
    def search(self, board, row, col, word, used_word_set):
        if (row, col) in used_word_set:
            return False
        if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1:
            return False
        else:
            cell = board[row][col]
            if len(word) == 1:
                return cell == word
            else:
                if word[0] != cell:
                    return False
                else:
                    used_word_set.add((row, col))
                    result = self.search(board, row - 1, col, word[1:], used_word_set) or \
                             self.search(board, row + 1, col, word[1:], used_word_set) or \
                             self.search(board, row, col + 1, word[1:], used_word_set) or \
                             self.search(board, row, col - 1, word[1:], used_word_set)
                    used_word_set.remove((row, col))
                    return result
            return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        result = False
        used_word_set = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if word[0] == board[row][col]:
                    if len(word) == 1:
                        return True
                    used_word_set.add((row, col))
                    result = self.search(board, row - 1, col, word[1:], used_word_set) or \
                             self.search(board, row + 1, col, word[1:], used_word_set) or \
                             self.search(board, row, col + 1, word[1:], used_word_set) or \
                             self.search(board, row, col - 1, word[1:], used_word_set)
                    used_word_set.remove((row, col))
                    if result:
                        return True

        return False


s = Solution()
board = [
    [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["b","c","d","e"]]
]
word = "a"
r = s.exist(board, word)
print(r)
